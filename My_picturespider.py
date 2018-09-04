import urllib.request as ure
import re
import easygui as g
import sys
import os
#打开网页，发送请求
def open_url(url):
    req = ure.Request(url)
    req.add_header('Referer', url)
    response = ure.urlopen(req)
    html = response.read()
    print(url)#查看访问的网址是否出错
    return html

#得到图片所在的具体位置
def get_img(url):
    html = open_url(url).decode('utf-8')
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    get_address = re.findall(p, html)
    return get_address

#保存图片
def save_img(folder, img_address):
    for each in img_address:
        print(each)
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = open_url(each)
            f.write(img)

#设置图片存放的文件以及开启爬虫
def tieba3(folder='tieba_picture', page=1,primary_url=''):
    os.makedirs(folder, exist_ok=True)
    os.chdir(folder)
    page=int(page)+1
    for i in range(1,page):
        url = primary_url + '?pn=' + str(i)
        img_address = get_img(url)
        save_img(folder, img_address)


if __name__ == '__main__':
#gui程序
    while True:
        title='贴吧图片获取器  version：0.1'
        if g.msgbox('欢迎此图片获取器',title,'下一步'):
            field_list=('网址','所要爬的页数（由第一页开始)','保存的图片的文件路径（建议纯英文路径）')
            value_list=['','1','']
            temp_value=g.multenterbox('请填入下列内容,由于下载图片需要一定时间，请耐心等待，不要在后台关闭程序',title,field_list,value_list)
            primary_url=temp_value[0]
            page=temp_value[1]
            folder=temp_value[2]
            tieba3(folder,page,primary_url)
            rep=g.msgbox('完成',title,'返回')
            if rep=='返回':
                pass
            else:
                sys.exit(0)
        else:
            sys.exit(0)