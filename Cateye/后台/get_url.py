import time
from selenium import webdriver
import re

driver_path = r"C:\Users\ASUS\AppData\Local\Programs\Python\Python37\chromedriver.exe"
binary_location = r'C:\Users\ASUS\AppData\Local\Google\chrome\App\Chrome-bin\chrome.exe'

# 传递一个有电影列表的html，返回电影的url列表
options = webdriver.ChromeOptions()
# 隐藏窗口
options.add_argument("--headless")
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
# 指定Chrome浏览器路径
options.binary_location = r'C:\Users\ASUS\AppData\Local\Google\chrome\App\Chrome-bin\chrome.exe'

# 设置为开发者模式，防止被各大网站识别出来使用了Selenium
brosver = webdriver.Chrome(driver_path, options=options)

# 修改window.navigator.webdriver关键字返回结果
brosver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
                """
})
for page in range(67):
    url = "https://www.maoyan.com/films?showType=3&offset={}".format(page * 30)
    brosver.get(url)
    html = brosver.page_source
    hrefs = re.findall('<a href="(.*?)" target="_blank" data-act="movies-click" data-val=".*?">', html)
    # return herfs
    list_url = ['https://maoyan.com{}'.format(href_) for href_ in hrefs]
    url_list = '\n'.join(list_url)
    with open('untils/url_list.txt', 'a', encoding='utf-8') as f:
        f.write(url_list + "\n")
    time.sleep(5)
    page += 1
    print('正在爬取第' + str(page) + '页')
brosver.close()
