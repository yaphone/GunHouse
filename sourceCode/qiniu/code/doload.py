#coding=utf-8

from qiniu import *
from listAllFile import listAllFile
import requests
import globalFile as gf

q = gf.q
bucket = BucketManager(q)
bucket_domain = gf.bucket_domain

def downloadFile():
    #认证信息

    file_list = listAllFile()
    for image_name in file_list:
        base_url = "http://%s%s" % (bucket_domain, image_name)
#        private_url = q.private_download_url(base_url, expires=3600)
        response = requests.get(base_url)
        image = response.content
        save_dir = "/Users/zhouyafeng/Desktop/github/GunHouse/download/"
    
        print(u"保存文件到"+save_dir+"\n")
        try:
            with open(save_dir+image_name,"wb") as jpg:
                jpg.write( image)  
                print "OK"
        except IOError:
            print("IO Error\n")
        finally:
            print u"处理完成"
            
def download_single_file(file_name):
    base_url = "http://%s%s" % (bucket_domain, file_name)
#    private_url = q.private_download_url(base_url, expires=3600*24)
    return "![%s](%s)" % (file_name, base_url)
    
    
if __name__ == "__main__":
    downloadFile()