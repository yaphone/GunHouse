#coding=utf-8
import re
import time
import urllib
import urllib2
import socket
from pushMessage import pushMessage


def check_network():
    while True:
        try:
            result=urllib.urlopen('http://baidu.com').read()
            print "Network is Ready!"
            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           time.sleep(5)
    getIP()

def getIP():                           #获取IP地址并发送
    try:
        lan_address = socket.gethostbyname(socket.gethostname())
        IP_address = visit("http://www.bliao.com/ip.phtml")
    except:
        try:
            IP_address = visit("http://www.ip138.com/ip2city.asp")
        except:
            try:
                IP_address = visit("http://www.whereismyip.com/")
            except:
                IP_address = "So sorry!!!"   
                
    event_name = "getip"
    message = {"lan_address":lan_address, "IP_address":IP_address}
    pushMessage(event_name, message)
    
   
def visit(url):                             #没啥说的
    opener = urllib2.urlopen(url)
    if url == opener.geturl():
        str = opener.read()
    return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)
    
if __name__ == "__main__":
    check_network()
