#coding=utf-8
import urllib
import urllib2

def push_to_server_chan(text, desp):
    server_chan_url = "http://sc.ftqq.com/SCU987T18d3592a473f1827d1effb64251c9a0956d9177b290b4.send?"
    text = text  #发送标题
    desp = desp  #发送内容
    url = server_chan_url + "text=" + text + '&' + "desp=" + desp
    print url
    
    res = urllib.urlopen(url)

    
if __name__ == "__main__":
    text = "HelloWorld"
    desp = "\"![logo](http://sc.ftqq.com/static/image/bottom_logo.png)\""
#    desp = "http://7xrczn.com1.z0.glb.clouddn.com/2.png?e=1457175281&token=kMXZldZ8vQ4WFw2Oujn0d9QAAUJtyVBgBmVNmEM_:B75h5myWLfSKOJMVcT4FuWkqrxw="
    push_to_server_chan(text, desp)