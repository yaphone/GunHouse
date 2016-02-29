#coding=utf-8


from instapush import Instapush, App

App_ID = "56d428bb5659e36b6be7ddf2"
App_secret = "ac45c1173fb2a7a1822e9ebbb06e3736"

def pushMessage(event_name, message):
    
    '''
    Args:
        event_name: 发送到instapush对应的App名称
        message: 要推送的信息, dict类型，{key1:value1, key2:value2},对应于instapush相应的trackers
    '''
    
    app = App(appid=App_ID, secret=App_secret)
    app.notify(event_name=event_name, trackers=message)    
    

if __name__ == "__main__":
    pushMessage('getip', {'IP_address': '113.251.168.74', 'lan_address': '192.168.56.1'})