#coding=utf-8
import os
import time

def recorde_video():
    path = os.path.dirname(os.path.dirname(os.getcwd()))
    video_path = os.path.join(path, 'GunHouse/photo/')    #相册路径
    local_time = time.localtime()
    video_time = time.strftime('%Y_%m_%d_%H_%M_%S',local_time)
    video_name = video_path + video_time + '.h264'

    recorde_video_command = 'raspivid -w 640 -h 480 -t 20000 -o ' + video_name
    os.system(recorde_video_command)





if __name__ == "__main__":
    recorde_video()
