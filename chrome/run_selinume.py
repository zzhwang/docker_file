import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

Type = 0
while True:
    try:
        requests.get('http://192.168.1.88:4444/wd/hub/status')
        break
    except:
        Type += 1
        time.sleep(1)
    if Type >= 10:
        raise Exception()

# 设置为无头形式
options = webdriver.ChromeOptions()
# 取消图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.headless = True
driver = webdriver.Remote(
    command_executor='http://192.168.1.88:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'},
    options=options
    )

driver.get('https://www.baidu.com')
html = driver.page_source
print(html)
