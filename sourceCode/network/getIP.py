#coding=utf-8
import re
import urllib2
import socket
from pushMessage import pushMessage

def getIP():
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
    print message
    pushMessage(event_name, message)
    
#    print lan_address
#    print IP_address
    
def visit(url):
    opener = urllib2.urlopen(url)
    if url == opener.geturl():
        str = opener.read()
    return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)
    
if __name__ == "__main__":
    getIP()
