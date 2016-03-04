#coding=utf-8

from qiniu import *
import os

access_key = 'kMXZldZ8vQ4WFw2Oujn0d9QAAUJtyVBgBmVNmEM_'
secret_key = 'R9Usc3pOZQWRMorEVVxZ6lTe0W0y1odojVF_iDWn'
bucket_domain = '7xr9yr.com1.z0.glb.clouddn.com/'   #公共空间
#bucket_domain = '7xrczn.com1.z0.glb.clouddn.com/'   #私有空间
bucket_name = 'helloworld'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)

photo_path = os.path.join(os.path.dirname(os.getcwd()), 'file')
