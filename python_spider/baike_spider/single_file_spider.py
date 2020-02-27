# -*- coding:utf-8 -*-

import re
import urllib2
import urlparse
from bs4 import BeautifulSoup

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()                                               #构造函数中初始化两个集合
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:                                                     #url为空的话则返回空
            return
        if url not in self.new_urls and url not in self.old_urls:           #如果既不在新的集合，也不再旧的集合，则添加到新的集合中
            self.new_urls.add(url)

    def add_new_urls(self,urls):                                            #同时添加多个列表
        if urls is None or len(urls) == 0:
            return
        for url in urls:                                                    #循环，用单个添加的函数逐个添加
            self.add_new_url(url)

    def has_new_url(self):                                                  #判断是否还有新的url
        return len(self.new_urls) != 0                                      #新集合长度不为0则返回真，否则返回假

    def get_new_url(self):                                                  #从集合中取出一个url并删除原来集合中的记录
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)                                          #把取出的url添加到旧的集合中
        return new_url

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:                                      #http请求返回代码等于200表示请求成功
            return None

        return response.read()                                             #返回下载的内容


#网页解析器
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):                                 #两个参数分别是当前页面url和下载的数据
        new_urls = set()
        #/view/123.htm   匹配这种形式
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))      #在下载的页面数据中正则匹配符合的href标签以及寻找a标签
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)              #利用urlparse模块将完整的url拼接起来
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}

        #url
        res_data['url'] = page_url                                         #赋予字典的键值

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")  #找到百科的名字
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")              #找到百科的具体解释
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:                           #是否为空做判断
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8') #创建BeautifulSoup对象
        new_urls = self._get_new_urls(page_url,soup)                        #获取url信息
        new_data = self._get_new_data(page_url,soup)                        #获取数据信息
        return new_urls,new_data


#输出器
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []                                                     #初始化一个列表

    def collect_data(self,data):                                            #收集数据的函数
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()                                          #构造函数中实例化其他的类
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self,root_url):
        count = 1                                                         #记录当前是第几个url
        self.urls.add_new_url(root_url)                                   #将入口url添加到url管理器
        while self.urls.has_new_url():                                    #url管理器中已经有了待爬取的url，启动爬虫的循环
            try:
                new_url = self.urls.get_new_url()                         #获取一个待爬取的url
                print 'craw %d : %s' % (count,new_url)                    #打印当前是第几个url，并且打印url内容
                html_cont = self.downloader.download(new_url)             #启动下载器下载这个页面
                new_urls,new_data = self.parser.parse(new_url,html_cont)  #解析器开始，传入两个参数（当前爬取的url和爬取的页面数据）
                self.urls.add_new_urls(new_urls)                          #将解析后的url添加到url管理器
                self.outputer.collect_data(new_data)                      #收集数据

                if count == 1000:
                    break

                count = count + 1
            except:
                print "craw failed"

        self.outputer.output_html()                                      #输出收集好的数据



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"                   #传入入口url
    obj_spider = SpiderMain()                                            #实例化主函数
    obj_spider.craw(root_url)                                            #调用主函数的craw方法
