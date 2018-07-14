#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib, urllib.request,time,datetime
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
SMSAPPID = xxxxxx
SMSAPPKEY = xxxxxxx
TEMPLATE_ID = xxxxxx
PHONE = xxxxxx

def send_sms():
    ssender = SmsSingleSender(SMSAPPID, SMSAPPKEY)
    now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    params = ['网站访问发生异常  当前时间：%s'%now]
    try:
        result = ssender.send_with_param(86, PHONE, TEMPLATE_ID, params)
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    print(result)

def url():
    try:
        url = 'http://114.67.224.92:10080/todo'
        result = urllib.request.urlopen(url)
        return(1)
    except Exception as e:
        return(2) 
        
def monitor(x,time_send):
    ret = url()
    if int(ret) == 2:
        if x == 0:
            print('ret=2,x=0')
            time_now = int(time.time())
            print(time_now,type(time_now))
            time_judge = time_send + 3600
            print(time_judge,type(time_judge))
            if time_judge > time_now:
                x = 1
                monitor(x,time_send)
            send_sms()
            time_send = int(time.time())
            x = 1
            time.sleep(1)
            monitor(x,time_send)
        else:
            print('ret=2,x=1')
            time.sleep(1)
            monitor(x,time_send)                        
    else:
        print('ret=1')
        x = 0
        time.sleep(1)
        monitor(x,time_send)
        
def start():
    x = 0
    time_send = 0
    monitor(x,time_send)
            
if __name__ == '__main__':
    start()
