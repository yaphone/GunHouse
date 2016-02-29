#coding=utf-8

from qiniu import *
from listAllFile import listAllFile
import requests
import globalFile as gf

def downloadFile():
    #认证信息
    q = gf.q       
    
    bucket = BucketManager(q)
    
    bucket_domain = "7xrczn.com1.z0.glb.clouddn.com/"
    file_list = listAllFile()
    for image_name in file_list:
        base_url = "http://%s%s" % (bucket_domain, image_name)
        private_url = q.private_download_url(base_url, expires=3600)
        print private_url
        response = requests.get(private_url)
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
    
    
if __name__ == "__main__":
    downloadFile()