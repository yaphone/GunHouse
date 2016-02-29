#coding=utf-8

from qiniu import *
from listAllFile import listAllFile
import requests
import globalFile as gf

def downloadFile():
    #认证信息
    q = gf.q       
    
    bucket = BucketManager(q)
    
    bucket_domain = "7xr9yr.com1.z0.glb.clouddn.com/"
    file_list = listAllFile()
    for image_name in file_list:
        base_url = "http://%s%s" % (bucket_domain, image_name)
        response = requests.get(base_url)
        image = response.content
        save_dir = "C:/Users/Administrator/Desktop/tmp/"
    
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