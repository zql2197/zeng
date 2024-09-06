import time
# import json
import re
import urllib.request
import pandas as pd
from lxml import html
from browsermobproxy import Server
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from fontTools.ttLib import TTFont
from PIL import ImageFont, Image, ImageDraw
from io import *
import ddddocr


def get_html_str(url):
    # 开启代理
    server = Server(r'/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    # 指定webdriver路径
    driver_path = r"C:\Users\ASUS\AppData\Local\Programs\Python\Python37\chromedriver.exe"

    # 配置代理启动webdriver
    options = webdriver.ChromeOptions()

    # 隐藏窗口
    options.add_argument("--headless")
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--proxy-server={}'.format(proxy.proxy))

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

    # 获取返回内容
    proxy.new_har("video", options={'captureContent': True})

    # 模拟浏览器
    brosver.get(url)

    time.sleep(2)
    json_data = proxy.har
    # 将json数据存储到本地
    # result_json = json.dumps(json_data,indent=4)
    # with open("eyecat.json", "w", errors="igone") as f:
    # f.write(result_json)

    for entry in json_data['log']['entries']:

        # 根据URL找到数据接口
        # print(entry)
        entry_url = entry['request']['url']
        # print(entry_url)
        strs = ''.join(entry_url)
        # print(strs)
        urls = re.findall('(https://www.maoyan.com/ajax/films.*?webdriver=false).*?', strs, re.S)
        # print(urls)
        for _url in urls:
            # print(_url)
            if "https://www.maoyan.com/ajax/films" in _url:
                _response = entry['response']
                # print(_response)
                _content = _response['content']['text']
                brosver.close()
                # 获取接口返回内容
                return _content


def font(woff_path):
    font_dict = {}
    Font = TTFont(woff_path)
    Font.flavor = 'woff'
    Font.save('font.ttf')
    # 图片宽度和高度
    img_size = 512
    font = TTFont('font/font.ttf')
    font_img = ImageFont.truetype('font.ttf', img_size)
    ocr = ddddocr.DdddOcr()
    for cmap_code, glyph_name in font.getBestCmap().items():
        # print(cmap_code,glyph_name)

        # 实例化一个图片对象
        img = Image.new('1', (img_size, img_size), 255)

        # 绘制图片
        draw = ImageDraw.Draw(img)
        # 将编码读取成字节
        txt = chr(cmap_code)

        x, y = draw.textsize(txt, font=font_img)

        draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font_img, fill=0)
        bytes_io = BytesIO()
        img.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        font_dict[glyph_name] = word
    return font_dict


# 将加密后数据替换为加密前字典内对应数据
def replace_elements(lis, dct):
    for i in range(len(lis)):
        if lis[i] in dct:
            lis[i] = dct[lis[i]]
    return lis


# 处理整数加密数据
def get_num0(str, font_dict):
    strs = []
    str = str.split(';')
    del (str[-1])
    str = [i.upper() for i in str]
    for i in str:
        i = i.replace('*', 'uni')
        strs.append(i)
    strs = replace_elements(strs, font_dict)
    strs = ''.join(strs)
    return strs


# 处理小数点后一位的加密数据
def get_num1(str, font_dict):
    strs = []
    str = str.split(';')
    del (str[-1])
    str = [i.upper() for i in str]
    for i in str:
        i = i.replace('*', 'uni')
        strs.append(i)
    strs = replace_elements(strs, font_dict)
    strs.insert(-1, '.')
    strs = ''.join(strs)
    return strs


# 处理小数点后两位的加密数据
def get_num2(str, font_dict):
    strs = []
    str = str.split(';')
    del (str[-1])
    str = [i.upper() for i in str]
    for i in str:
        i = i.replace('*', 'uni')
        strs.append(i)
    strs = replace_elements(strs, font_dict)
    strs.insert(-2, '.')
    strs = ''.join(strs)
    return strs


# 将字典数据存储到Excel文件中
def save_to_excel(dic, index):
    save_path = r'/Cateye/untils/movie.xlsx'
    if index < 1:
        lis = [dic]
        pf = pd.DataFrame(list(lis))
        # 指定字段顺序
        order = ['movie_name', 'movie_type', 'movie_area', 'movie_duration', 'movie_publish', 'movie_score',
                 'movie_comments', 'movie_booking', 'movie_director']
        pf = pf[order]
        pf.to_excel(save_path, encoding='utf-8', index=False)
        print("第", index + 1, '个数据存入成功')
    else:
        original_data = pd.read_excel(r'D:\PyCharm Community Edition 2021.2.1\Cateye\movie.xlsx')
        lis = [dic]
        pf = pd.DataFrame(list(lis))
        save_data = original_data.append(lis)
        save_data.to_excel(save_path, encoding='utf-8', index=False)
        print("第", index + 1, '个数据追加成功')


def main():
    urls = []
    with open('untils/url_list.txt', 'r') as f:
        for line in f.readlines():
            urls.append(line.strip())
        # print(urls)
    for url in urls:
        item = {}
        index = urls.index(url)
        html_str = get_html_str(url)
        # print(html_str)
        # 下载woff字体文件，找出对应的映射关系
        woff_url = 'http:{}'.format(
            re.findall(r'(//s3plus.meituan\.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/\w+\.woff)', html_str)[0])
        # print(woff_url)
        woff_path = r'/Cateye/font/font.woff'
        # 根据url地址将文件下载到指定路径下
        urllib.request.urlretrieve(woff_url, woff_path)
        print('第', index + 1, '个字体文件成功下载')
        font_dict = font(woff_path)
        # print(font_dict)
        html_str = re.sub(r'&#x', r'*', html_str)
        html_str = html.etree.HTML(html_str)
        # 通过三目运算符进行多重判断可以增加程序的稳定性
        # 电影名称
        movie_name = html_str.xpath('//div[@class="movie-brief-container"]/h1/text()')
        item['movie_name'] = movie_name[0] if len(movie_name) > 0 else None
        # 电影类型
        movie_type = html_str.xpath('//div[@class="movie-brief-container"]/ul/li[1]/a/text()')
        movie_type = movie_type if len(movie_type) > 0 else None
        if movie_type is not None:
            item['movie_type'] = '·'.join([i.strip() for i in movie_type])
        else:
            item['movie_type'] = '类型未知'
        # 上映国家和电影时长
        area_time = html_str.xpath('//div[@class="movie-brief-container"]/ul/li[2]/text()')
        area_time = area_time[0] if len(area_time) > 0 else None
        if area_time is not None:
            area_time = area_time.split('/')
            item['movie_area'] = area_time[0].strip() if len(area_time) > 0 else '上映国家未知'
            item['movie_duration'] = area_time[1].strip() if len(area_time) > 1 else '电影时长未知'
        else:
            item['movie_area'] = '上映国家未知'
            item['movie_duration'] = '电影时长未知'
        # 上映时间
        movie_publish = html_str.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
        movie_publish = movie_publish[0] if len(movie_publish) > 0 else None
        if movie_publish is not None:
            item['movie_publish'] = re.findall(r'([0-9]+-[0-9]+-[0-9]+)', movie_publish)[0]
        else:
            item['movie_publish'] = '上映时间未知'
        # 电影评分
        score = html_str.xpath('//div[@class="movie-index-content score normal-score"]/span/span/text()')
        score = score[0] if len(score) > 0 else None
        if score == '暂无':
            score = None
        if score is not None:
            score = score.replace('.', '')
            movie_score = get_num1(score, font_dict)
            item['movie_score'] = movie_score
        else:
            item['movie_score'] = '电影评分未知'
        # 评分人数
        movie_comments = []
        comments = html_str.xpath('//span[@class="score-num"]/span/text()')
        comments = comments[0] if len(comments) > 0 else None
        if comments is not None:
            if '.' in comments:
                comments = comments.replace('.', '')
                if '万' in comments:
                    comments = comments.replace('万', '')
                    movie_comments = get_num1(comments, font_dict) + '万'
            else:
                if '万' in comments:
                    comments = comments.replace('万', '')
                    movie_comments = get_num0(comments, font_dict) + '万'
                else:
                    movie_comments = get_num0(comments, font_dict)
            item['movie_comments'] = movie_comments
        else:
            item['movie_comments'] = '评分人数未知'
        # 电影票房
        # movie_booking = ()
        booking = html_str.xpath('//div[@class="movie-index-content box"]/span[1]/text()')
        booking = booking[0] if len(booking) > 0 else None
        if booking == '暂无':
            booking = None
        if booking is not None:
            if '.' in booking:
                booking = booking.replace('.', '')
                movie_booking = get_num2(booking, font_dict) + '亿'
            else:
                movie_booking = get_num0(booking, font_dict) + '万'
            item['movie_booking'] = movie_booking
        else:
            item['movie_booking'] = '电影票房未知'
        # 导演
        movie_director = html_str.xpath(
            '//div[@class="celebrity-container clearfix"]//div[1]//ul//li//div[@class="info"]//div['
            '@class="name"]/text()')
        movie_director = movie_director[0] if len(movie_director) > 0 else None
        if movie_director is not None:
            item['movie_director'] = movie_director.strip()
        else:
            item['movie_director'] = '导演未知'
        # print(item)
        print('第', index + 1, '个电影数据获取成功')
        # 将电影数据暂时存储到Excel文件中
        save_to_excel(item, index)


if __name__ == '__main__':
    main()
