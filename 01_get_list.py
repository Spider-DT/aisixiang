# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         01
# Description:
# Author:       Administrator
# Date:         2020/8/23
#-------------------------------------------------------------------------------

import requests
from lxml import etree
class AiSiXiang(object):

    def __init__(self,name):
        """
         初始化请求头，输入搜素对象
        :param name: 搜索对象
        """
        self.name = name
        self.url = 'http://www.aisixiang.com/thinktank/{}.html'.format(self.name)
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) '
        }

    def get_data(self,url):
        """
        获取响应源码
        :param url: 目标地址
        :return: 返回源码，并设置 data 接收
        """
        response = requests.get(url,headers = self.headers)
        return response.content

    def parse_list_page(self,data):
        # 将获取的响应源码转化成 element
        html = etree.HTML(data)
        # 提取响应页面的每条信息，xpath定位
        el_list = html.xpath('//table//tbody[1]//tr[5]//td[2]//a')
        # 创建提取对象列表
        data_list = []
        i = 0
        # 循环提取，索引0为名称；索引1为link
        for el in el_list:
            temp = {}
            #  提取当前行中的文字
            temp['title'] = el.xpath('./text()')[0]
            #  提取当前行中的链接
            temp['link'] = 'http://www.aisixiang.com/' + el.xpath('./@href')[0]
            data_list.append(temp)
            i = i + 1
            # return data_list
        print(data_list)
        print('*' * 50)
        print("共找到资料 {} 篇".format(i))
        result2txt = str(data_list)
        with open('list.txt','a',encoding='utf-8') as f:
            f.writelines(result2txt)
            f.close()

    def run(self):
        """
        执行函数
        """
        #  获取源码响应，并返回解析结果
        data = self.get_data(self.url)
        #  数据提取
        self.parse_list_page(data)
        #  数据写入txt
        # data1 = self.parse_list_page(data)
        # self.text_save(data1)

if __name__ == '__main__':
    # aisixiang = AiSiXiang('gejianxiong')
    aisixiang = AiSiXiang('qianliqun')
    # aisixiang = AiSiXiang('leige')
    aisixiang.run()
