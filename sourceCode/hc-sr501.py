import RPi.GPIO as GPIO
import time
 
#��ʼ��
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18,GPIO.IN)
    GPIO.setup(21,GPIO.OUT)
    pass
 
#���������к���
def beep():
    while GPIO.input(26):
        GPIO.output(21,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(0.5)
#��Ӧ����⺯��
def detct():
    #��Ϊ�ǽ������飬����ֻ����ѭ������100��
    while True:
        #�����Ӧ��������ΪTrue�����ӡ��Ϣ��ִ�з���������
        if GPIO.input(26) == True:
            print "Someone isclosing!"
            beep()
        #���򽫷���������ŵ�ƽ����ΪHIGH
        else:
            GPIO.output(21,GPIO.HIGH)
            print "Noanybody!"
        time.sleep(2)
 

init()
detct()
#�ű��������ִ��������
GPIO.cleanup()