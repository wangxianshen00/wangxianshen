
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time#import time
from selenium.webdriver.common.action_chains import ActionChains#移动光标事先定义actionchains




# 如果火狐没有默认路径安装，可以使用下面OS语句指定
# os.environ["webdriver.firefox.driver"] = "d:\Mozilla Firefox.exe"
d = webdriver.Firefox(executable_path="d:\\geckodriver.exe")#驱动火狐
d.get("file:///D:/coshttp/demo.html")#进入demo


# 启动IE浏览器
# d = webdriver.Ie(executable_path="d:\\IEDriverServer")
# 启动谷歌
# d = webdriver.Chrome(executable_path="d:\\chromedriver.exe")

d.find_element_by_id("user").send_keys("456")
d.find_element_by_class_name("baidu").click()
d.back()
d.find_element_by_xpath("/html/body/div/table/tbody/tr[3]/td[2]/div/select/option[3]").click()
d.find_element_by_xpath("/html/body/div/table/tbody/tr[4]/td[2]/div/input[2]").click()
d.find_element_by_xpath("/html/body/div/table/tbody/tr[5]/td[2]/div/input[3]").click()
# d.find_element_by_xpath(".//div[@id='button']/input").click()
# g = d.isDisplayed()
# SystemError(g).click()//置灰

d.find_element_by_class_name("alert").click()
time.sleep(3)#三秒后点击确定
alter = d.switch_to_alert()
alter.accept()#点击确定
d.find_element_by_xpath("/html/body/div/table/tbody/tr[9]/td[2]/div/a").click()
h = d.current_window_handle#新建第一个句柄h
d.switch_to.window(h)    #返回上一个句柄h
# move = d.find_element_by_xpath("/html/body/div/table/tbody/tr[10]/td[2]/div/input")//定义move的位置
# ActionChains(d).move_to_element(move).perform()//ActionChains d方法 move_to指定位置
d.find_element_by_class_name("wait").click()#点击wait




# 截图
# d.get_screenshot_as_file("d:\\a\\tu.jpg")

# d.quit()
# d.close()

# 浏览器后退
# d.back()
# d.forward()
# d.refresh()

# 窗口化
# d.maximize_window()
# d.minimize_window()
# 清空输入框中的内容
# d.find_element_by_id("user").clear()

# 添加cookie
# cookie ={u'domain':u'.cnblogs.com',
# u'name':u'CNBlogsCookie',
#          }