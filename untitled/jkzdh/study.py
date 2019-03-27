import requests
import json
import unittest
url = "http://localhost:8080/gouwu/mem.do"
head={

"Cache-Control": "max-age=0",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Accept-Language": "zh-CN",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Upgrade-Insecure-Requests": "1",
"Accept-Encoding": "gzip, deflate",
"Content-Length": "149",
"Host": "localhost:8080",
"Proxy-Connection": "Keep-Alive",
"Pragma": "no-cache"
}
canshu = {
    "memberLever": "2",
    "memberName": "大腿",
    "loginName": "222",
    "loginPwd": "0000",
    "phone": "17603591713",
    "address": "四惠东",
    "zip": "000000",
    "email": "11@qq.com",
    "C_Input": "%D7%A2%B2%E1"
}
r=requests.get(url,headers=head,data=canshu)
print(r.status_code)
print(r.text)