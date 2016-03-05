#coding=utf-8

from qiniu import *
import globalFile as gf

def listAllFile():
    #认证信息
    q = gf.q
    
    bucket = BucketManager(q)
    bucket_name = gf.bucket_name
    file_list = list_all(bucket_name, bucket, prefix=None, limit=None)  #文件列表
    return file_list                                   #返回文件列表
    
def list_all(bucket_name, bucket, prefix=None, limit=None):
    if bucket is None:
        bucket = BucketManager(q)
    marker = None
    eof = False
    while eof is False:
        ret, eof, info = bucket.list(bucket_name, prefix=prefix, marker=marker, limit=limit)
        marker = ret.get('marker', None)

        if eof is not True:
            # 错误处理
            pass    
        file_list = []
        for item in ret['items']:
            file_list.append(item['key'])
        return file_list


    
    
if __name__ == "__main__":
    listAllFile()