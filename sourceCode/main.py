#coding=utf-8
from network import pushToServerChan
from raspberry import *
from myqiniu.code import upload
import time
#import Rpi.GPIO as GPIO
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
            if current_status == 0 and previous_status==1:     #门刚被打开
                text = u"枪库已打开"
                local_time = time.localtime()
                current_time = time.strftime('%Y:%m:%d_%H:%M:%S',local_time)
                desp = u"枪库于%s被打开,图像抓取程序已启动" %current_time
                pushToServerChan.push_to_server_chan(text, desp)
            while current_status == 0:          #门开
                for i in range(5):
                    take_photo.takePhoto()
                    time.sleep(2)
                recorde_video.recorde_video()
                time.sleep(5)
            previous_status = 1
        except:
            pass
        
        
if __name__ == "__main__":
    try:
        thread_1 = threading.Thread(target=gunHouseMain)
        thread_2 = threading.Thread(target=upload.uploadFile)
#        thread_1.start()
        thread_2.start()
  
    except:
        print u"程序出错"
        text = "程序出错"
        desp = "程序出错，请及时检查"
        pushToServerChan.push_to_server_chan(text, desp)
    
                
            
                
            
        