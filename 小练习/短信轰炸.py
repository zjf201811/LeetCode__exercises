# Author:ZJF
import requests,time,json
import time

class SMSsend_one(object):

    def __init__(self,mobile):
        self.url = "http://bbs.mydigit.cn/registe.php"
        self.header = {
            "Referer":"http://bbs.mydigit.cn/registe.php",
            "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64;rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        self.mobile = mobile

    def get_response(self):
        data = {
            "action":"auth",
            "step":"1",
            "mobile":self.mobile
        }
        try:
            response = requests.post(url=self.url,
                                     data=data,
                                     headers=self.header)
            print("{}:{}>>>发送成功".format(self.url,self.mobile))
        except Exception:
            print("{}:{}>>>发送成功".format(self.url,self.mobile))

    def run(self):
        self.get_response()
if __name__ == "__main__":
    for i in range(2):
        mobile = "15263364040"
        one = SMSsend_one(mobile)
        one.run()

