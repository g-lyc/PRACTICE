# -*- coding:utf-8 -*-
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        count = 1                                                         #记录当前是第几个url
        self.urls.add_new_url(root_url)                                   #将入口url添加到url管理器
        while self.urls.has_new_url():                                    #url管理器中已经有了待爬取的url，启动爬虫的循环
            try:
                new_url = self.urls.get_new_url()                         #获取一个待爬取的url
                print 'craw %d : %s' % (count,new_url)                      #打印当前是第几个url，并且打印url内容
                html_cont = self.downloader.download(new_url)             #启动下载器下载这个页面
                new_urls,new_data = self.parser.parse(new_url,html_cont)   #解析器开始，传入两个参数（当前爬取的url和爬取的页面数据）
                self.urls.add_new_urls(new_urls)                          #将解析后的url添加到url管理器
                self.outputer.collect_data(new_data)                      #收集数据

                if count == 1000:
                    break

                count = count + 1
            except:
                print "craw failed"

        self.outputer.output_html()                                      #输出收集好的数据

        

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)