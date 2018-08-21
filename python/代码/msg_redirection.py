# touch error.py
chinese_msg = {}
chinese_msg[-1] = '用户名错误'

ERR = chinese_msg


# touch url.py
url = {}
url['login'] = '/login'

url_chinese_msg = {}
url_chinese_msg['login'] = '点击登录'

URL = url
URL_MSG = url_chinese_msg


# touch store_view.py
def red_writing_1(msg,addr,msg2):
	return u'<html><font color="red"><h3>%s</h3></font></html><br> <a href="%s"><h3>%s</h3></a>'%(msg,addr,msg2)


# touch store_user.py
from error import *
from url import *
from store_view import *

def checkLogin():
    return -1

def mskeErrRedir(errid, url):
    print(url)
    err_msg = ERR[errid]
    urll = URL[url]
    url_msg = URL_MSG[url]
    return red_writing_1(err_msg,urll,url_msg)


# touch store,py
from bottle import *
from error import *

@route('/')
def index():
    ret = checkLogin()
    for k,v in ERR.items():
        if ret == k:
            return mskeErrRedir(ret,'login')
run(host='127.0.0.1',port='10090',debug=True,reloader=True)