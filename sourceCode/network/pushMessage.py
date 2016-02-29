#coding = utf-8


from instapush import Instapush, App

App_ID = "56d11f995659e3652ec56c64"
App_secret = "00f263a58cd1d408c5cf7ecff08cc9dc"

def pushMessage(event_name, message):
    
    '''
    Args:
        event_name: 要发送到instapush的事件名称
        message: 要推送的信息
    '''
    
    app = App(appid=App_ID, secret=App_secret)
    app.notify(event_name=event_name, trackers={'message':message})    
    

if __name__ == "__main__":
    pushMessage("hello", u"GunHouse")