from selenium import webdriver
import unittest
import time
import ddt


@ddt.ddt
class TestMethod(unittest.TestCase):

    def setUp(self):
        self.d = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
        self.d.get("file:\\\d:\coshttp\demo.html")

    def tearDown(self):
        print("关闭")

    @ddt.file_data("aa.json")
    def test_1(self,data):
        c,c1,c2 = tuple(data)
        self.d.find_element_by_id("user").send_keys(c)
        self.d.find_element_by_id("user").send_keys(c1)
        self.d.find_element_by_id("user").send_keys(c2)
if __name__ == '__main__':
    unittest.main()