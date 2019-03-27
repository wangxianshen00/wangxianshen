import requests
import unittest
import json




'''
# 下面代码是get方法无参
url = "http://www.tgbus.com"
r = requests.get(url)
print(r.status_code)
# print(r.text)结果为乱码，因为电玩巴士主页非纯text，所以使用r.text看html会出现乱码
print(r.content)
'''
'''
# 下面代码是get方法无参
url ="http://www.tgbus.com"
r=requests.get(url)
print(r.status_code)
# print(r.text)结果为乱码，因为电玩巴士主页非纯text，所以使用r.text看html会出现乱码
print(r.content)
'''
'''
# 下面代码是get带参数
url = "http://apis.juhe.cn/cook/query.php"
canshu ={
    "key":"fb7fec936067e3dab6295891fd144e1e",
    "menu":u"白菜"
        }

r = requests.get(url,params=canshu)
print(r.status_code)
print(r.text)
'''

# 下面代码是post带参数,使用data格式传参
url = "http://localhost:8080/gouwu/mem.do;jsessionid=9F2655348032B3E8C64997FA4E5B6CA8?method=reg "
head={
"Referer": "http://localhost:8080/gouwu/mem.do;jsessionid=C31796AD94C5B2B19DB9ED7DB836D152?method=reg",
"Cache-Control": "max-age=0",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Accept-Language": "zh-CN",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Upgrade-Insecure-Requests": "1",
"Accept-Encoding": "gzip, deflate",
"Content-Length": "151",
"Host": "localhost:8080",
"Proxy-Connection": "Keep-Alive",
"Pragma": "no-cache",
"Cookie": "JSESSIONID=9F2655348032B3E8C64997FA4E5B6CA8",
}
canshu ={
    "memberLever":"2",
    "memberName":"大腿",
    "loginName": "222",
    "loginPwd":"0000",
    "phone": "17603591713",
    "address":u"四惠东",
    "zip": "000000",
    "email":"11@qq.com",
    "C_Input":"%D7%A2%B2%E1"
        }
r = requests.post(url,headers=head,data=canshu)
print(r.status_code)
print(r.text)

'''
以下为购物的注册，需要加上请求体，购物网站的注册走的是post方法，使用data传参
url = "http://localhost:8080/gouwu/mem.do"

head = {
    "host":"localhost:8080",
    "Content-Length":"136"
}
canshu={
    "method":"reg",
    "memberlevel":"1"
}
r=requests.post(url,headers=head,data=canshu)
print(r.status_code)
print(r.text)
'''
'''
下面代码是post方法中json传值，服务器可能会有两种方法。
1.我们把直接传递json的可以称为"生肉"，把test或其他读取格式的称为"熟肉"
以下为"生肉"，也就是直接传送json值，不需要"翻译"
url="http://localhost:8080/test/mem.do"
head={
    "host":"localhost:8080",
    "Content-Length":"136"
}
canshu={
    "id":3,
    "method":"ajax.updataLevel",
    "params":[3,"3"]
}
r=requests.post(url,headers=head,json=canshu)
print(r.status_code)
print(r.text)
'''
'''
以下为熟肉，也就是需要"翻译"后，在给服务器查看
因为转换json需要用到json库，所以先引入
url="http://localhost:8080/test/mem.do"
head={
    "host":"localhost:8080",
    "Content-Length":"136"
}
canshu={
    "id":3,
    "method":"ajax.updataLevel",
    "params":[3,"3"]
}
shurou=json(canshu)



r=requests.post(url,headers=head,json=shurou)
print(r.status_code)
print(r.text)
'''
'''
当遇上HTTPS的时候，可以将ssl进行忽略操作，verify-False
url ="https://www.baidu.com"
head = {}
can ={}
r=requests.get(url,headers=head,verify=False)
print(r.status_code)
print(r.text)



下面是使用session
例如：先登录，之后将返回的session信息内容赋值给s，之后在用s干什么
url="登录地址"
head={}
can={}
s = requests.session()
r=s.post(url,headers=head,verify=False)
# print(r.json())      这里输出犯规的json格式的内容

在做登录，进行下一步的操作
url2="支付"
can2={}
r2=s.post(url2,data=can2,verify=False)
print(r2.status_code)
print(r2.text)
'''
'''
cokie内容详解
name:cookie的名字
value:cookie名字对应的值，动态生成
domain:服务器域名
expiry:cookie有效终止日期
path:path属性定义了web服务器上哪里路径下的页面可获取服务器设置的cookie
HTTPOnly：防御脚本攻击
secure:在Cookie中标记该变量，表明只有当浏览器和web server之间的通信协议为加密认证协议是，浏览器才向服务器提交相应的cookie，当前这种协议只有一种，即为HTTPS
'''
'''
以下为cookie跳过登录验证
补充：最简单的方法，先登录一下网页，抓取登录后的cookie值，之后直接发送即可。
这里的代理分为两段，第一段接口模拟登录，之后截获值赋值给变量第二段使用变量坐下面的接口

1）登录后，获取cookie
url="登录"
head={}
s=requests.session()
r=s.get(url,header=head,verify=False)
print(s.cookies)     将所有的cookie进行输出

2）添加登录需要的cookie，进行跳过验证
c=requests.cookies.RequestsCookieJar()
c.set('对应的名','对应的值')
c.set('对应的名','对应的值')

s.cookies.update(c)
'''
'''
# 保持登录状态后干什么，例如支付
url2="支付接口"
can={}
r2=s.post(url2,data=can,verify=False)
print(r2.status_code)
print(r2.text)
'''
'''
# 以下是302和需要去跳转的位置显示使用allow_redirects=True
url="http://baidu.com"
head={}
s=requests.session()
r=s.get(url,allow_redirects=True,headers=head,verify=False)
print(r.status_code)
xinxi=r.headers['location']#读取返回头中的指定内容名称，并将这个名称的值进行赋值
print(xinxi)
'''
# toekn有三种方法
# 第一种token放到请求头中

'''
head=()
can=()
s=requests.session()
login_url="接口"
login_ret=s.post(login_url,headers=head,data=can)
# 获取token，上面的请求返回json方法，我们直接提取
token = login_ret.json()["token"]
# 下面模拟带token的请求
post_url="接口地址"
# 添加token到请求头
head["token"]=token
# 这里假设请求头的有其他字段也改变了，例如content-Length，我们可以单写
head["content-Length"]="9"
can1=[]
post_ret=s.post(post_url,headers=head,data=can1)
print(post_ret.content)
'''
'''
第二种token在cookie中的方法
例如token值直接通过抓包抓到，一般为先登录进行抓包，之后记录下cookie值后，在复制

url="网址"
head={

    "Cookie":"csrfToken=值",
    #其他的请求头省略
}
r=requests.get(url,headers=head)
print(r.content)

以下是关联
url="网址"
head={}
can={}
session登录
s=requests.session()
r=s.post(url,json=can,headers=head,verify=False)
print(r.json())
保存草稿
url2="接口地址"
can2={}
r2=s.post(url2,data=can2,verify=False)
# 获取当前地址
print(r2.url)
'''
'''
import re#加载正则表达式的库
p=re.findall(r"postid=(.+?)&",r2,url)
print(p)#显示所有符合正则的值
print(p[0])#提取第一个符合的值
# 关联后在发送一个请求
url3="接口地址"
json3={"p":p[0]}
r3=s.post(url3,json=json3,verify=False)
print(r3.json())
'''
'''
post的坑，例如post请求后，因为重定向，所以cookie会丢失，所以自动跳回了登录页面
解决问题的方案就是禁止重定向，获取重定向的url后，直接发定向后的url，之后把cookie\session\token都带上

例如下面的例子中，重定向后csrtToken，jsessionid,userName会失效，所以可以先将值获取下来，当做变量，
后期直接使用
代码如下：
ctoken="这里写的是最开始的token值，也就是失效前的"
jse="这里写的是最开始的session值，也就是失效前的"
uName="用户名"
url="接口地址"
h1={}
can={}
s=requests.session()
r1=s.post(url,headers=h1,data=can,allow_redirects=False)
print(r1.status_code)
# 下面获取cookie发送，其他的省略，下面可以看做print（%是，jse）%s指的是一个变量值，jse是变量的引用
h2={
    "cookie":"csrfToken=%s,businessUsernama=%s"%(ctoken,jse,uName)
}
r2=s.get(url,headers=h2)
print(r2,content)
'''


