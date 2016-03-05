#coding=utf-8

import os
import globalFile as gf
from doload import *
from qiniu import *
from listAllFile import listAllFile
from pushToServerChan import *
import time

#认证信息
q = gf.q
bucket_name = gf.bucket_name

def uploadFile():
    #上传文件
    path = os.getcwd()
    file_path = gf.photo_path
    while True:
        file_list = os.listdir(file_path)
        server_file_lists = listAllFile()    #空间文件列表
        for file_name in file_list:
            if file_name not in server_file_lists:
                localfile = os.path.join(file_path, file_name)
                key = file_name
                mime_type = "image/jpeg"
                params = {'x:a': 'a'}
    
                token = q.upload_token(bucket_name, key)
                ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    #            print dir(info)
    #            print info
                status_code = info.status_code
                if status_code == 200:                   #文件上传成功
                    upload_file_name = ret['key']   #上传成功的文件名
                    text = upload_file_name
                    desp = download_single_file(file_name)
                    push_to_server_chan(text, desp)
                    print "OK"
        time.sleep(10)

def upload_single_file(file_name):                         #上传单个文件
    path = os.getcwd()
    file_path = gf.photo_path
    file_list = os.listdir(file_path)
    localfile = os.path.join(file_path, file_name)
    key = file_name
    mime_type = "image/jpeg"
    params = {'x:a': 'a'}

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    status_code = info.status_code
    if status_code == 200:                   #文件上传成功
        upload_file_name = ret['key']   #上传成功的文件名
        text = upload_file_name
        desp = download_single_file(file_name)
        push_to_server_chan(text, desp)
        print "OK"





if __name__ == "__main__":
    uploadFile()
#    upload_single_file('4.jpg')
