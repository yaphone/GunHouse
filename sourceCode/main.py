#coding=utf-8
from network import pushToServerChan
from raspberry import take_photo, recorde_video
from myqiniu.code import upload
import time
import RPi.GPIO as GPIO
import threading

def gunHouseMain():
    GPIO.setmode(GPIO.BOARD)
    GPIO_SWITCH = 12
    GPIO.setup(GPIO_SWITCH, GPIO.IN)

    previous_status = 1
    current_status = 1
    while True:
        try:
            current_status = GPIO.input(GPIO_SWITCH)
            if (current_status == 0 and previous_status == 1):     #门刚被打开
                text = "枪库已打开"
                local_time = time.localtime()
                current_time = time.strftime('%Y年%m月%d日%H时%M分%S秒',local_time)
                desp = "枪库于%s被打开,图像抓取程序已启动" %current_time
                pushToServerChan.push_to_server_chan(text, desp)
                previous_status = 0
                print "枪库被打开"
            if current_status == 0:          #门开
                for i in range(5):
                    take_photo.takePhoto()
                    print "拍照中"
                    time.sleep(2)
                recorde_video.recorde_video()
                print "录像中"
                time.sleep(5)

            if current_status == 1 and previous_status == 0:
                text = "枪库已关闭"
                print text
                localtime = time.localtime()
                current_time = time.strftime('%Y年%m月%d日%H时%M分%S秒', localtime)
                desp = "枪库与%s被关闭" %current_time
                pushToServerChan.push_to_server_chan(text, desp)
                previous_status = 1

        except:
            pass
        time.sleep(1)


if __name__ == "__main__":
    try:
        thread_1 = threading.Thread(target=gunHouseMain)
        thread_2 = threading.Thread(target=upload.uploadFile)
        thread_1.start()
        thread_2.start()

    except:
        print u"程序出错"
#        text = "程序出错"
#        desp = "程序出错，请及时检查"
#        pushToServerChan.push_to_server_chan(text, desp)






