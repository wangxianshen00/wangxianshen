import unittest
from shijian.common.HtmlRunner import HTMLTestRunner


# case_dir:是用例存放的路径，由外到里编写
# pattern：匹配规则“test*.py”指的是匹配所有以test开头的py文件
sdir = r'C:\users\t\PycharmProjects\untitled\shijian\case'  #这里为我程序的目录
rule = "test*.py"                       #这行值引用所有的case中的py文件

discover = unittest.defaultTestLoader.discover(sdir,rule)
print(discover)

#生成高级报告
fp = open("result.html","wb")
runer = HTMLTestRunner(fp,title="报告的标题，这个是我的项目",
                        description="报告如下：")
runer.run(discover)
fp.close()