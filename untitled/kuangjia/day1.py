import unittest
from selenium import webdriver
import time

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.d = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
        self.d.get("https://www.baidu.com/")
        print("开始")

    def tearDown(self):
        print("结束")


    def test_1(self):

        dingwei=self.d.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[2]")
        text = dingwei.text
        print(text)
        self.assertEqual("hao123", text, msg="结果错了")



if __name__ == '__main__':
            unittest.main()
