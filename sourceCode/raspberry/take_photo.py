#coding=utf-8
import os
import time

def takePhoto():
    path = os.path.dirname(os.path.dirname(os.getcwd()))
    photo_path = os.path.join(path, 'photo/')    #相册路径
    photo_time = time.ctime()
    photo_name = photo_path + photo_time

    take_photo_command = 'raspistill -o ' + photo_name
    os.system(take_photo_command)





if __name__ == "__main__":
    takePhoto()

