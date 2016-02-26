#coding=utf-8

import os
import globalFile as gf
from qiniu import *

def uploadFile():
    
    #认证信息
    q = gf.q
    bucket_name = gf.bucket_name
    
    #上传文件
    path = os.getcwd()
    parent_path = os.path.dirname(path)    #上级目录
    file_path = os.path.join(parent_path, 'file')
    file_list = os.listdir(file_path)   
    for file_name in file_list:
        localfile = os.path.join(file_path, file_name)
        key = file_name
        mime_type = "image/jpeg"
        params = {'x:a': 'a'}
        
        token = q.upload_token(bucket_name, key)
        ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)    
    
    
if __name__ == "__main__":
    uploadFile()