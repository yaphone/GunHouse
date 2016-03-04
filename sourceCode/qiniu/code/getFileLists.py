#coding=utf-8
import globalFile as gf
from qiniu import *

def get_qiniu_file_lists():
    q = gf.q
    
    bucket_name = gf.bucket_name 
    bucket = gf.bucket
    key = '1.png'
    ret, info = bucket.stat(bucket_name, key)
    print(info)
    print ret
    assert 'hash' in ret  
    
if __name__ == "__main__":
    get_qiniu_file_lists()