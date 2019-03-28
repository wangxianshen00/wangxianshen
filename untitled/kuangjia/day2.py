import unittest#添加包
import requests

class TestdCaipu(unittest.TestCase):
    def test_Cai(self):

        url="http://apis.juhe.cn/cook/query.php"

        par = {"key":"fb7fec936067e3dab6295891fd144e1e",
               "menu":u"鸡蛋"}


        r=requests.post(url,params=par)
        print(r.status_code)
        print(r.text)



if __name__=="__main__":
     unittest.main()
