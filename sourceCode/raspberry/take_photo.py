#coding=utf-8
import os
import time

def takePhoto():
    path = os.path.dirname(os.path.dirname(os.getcwd()))
    photo_path = os.path.join(path, 'GunHouse/photo/')    #相册路径
    local_time = time.localtime()
    photo_time = time.strftime('%Y_%m_%d_%H_%M_%S',local_time)
    photo_name = photo_path + photo_time + '.jpg'

    take_photo_command = 'sudo raspistill -t 3 -w 640 -h 480 -q 75 -o ' + photo_name
    os.system(take_photo_command)





if __name__ == "__main__":
    takePhoto()

