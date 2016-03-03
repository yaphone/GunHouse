#coding=utf-8

from qiniu import *
import os

access_key = 'kMXZldZ8vQ4WFw2Oujn0d9QAAUJtyVBgBmVNmEM_'
secret_key = 'R9Usc3pOZQWRMorEVVxZ6lTe0W0y1odojVF_iDWn'
bucket_name = 'gunhouse'
q = Auth(access_key, secret_key)

photo_path = os.path.join(os.path.dirname(os.getcwd()), 'file')
print photo_path