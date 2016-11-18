from baike import spider_down,spider_manager,spider_outhtml,spider_parser
class Spidermain(object):
    def __init__(self):
        self.urls = spider_manager.url_manage()
        self.download = spider_down.url_down()
        self.parser = spider_parser.url_parser()
        self.outputer = spider_outhtml.outhtml()


    def crawl(self,rooturl):
        count = 1
        self.urls.add_new_url(rooturl)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('正在抓取第%d个url：%s'%(count,new_url))
                html_cout = self.download.download_url(new_url)
                new_urls,new_data = self.parser.url_parser(new_url,html_cout)
                self.urls.add_new_urls(new_urls)
                self.outputer.collectdata(new_data)
                count+=1
                if count==5000:
                    break
            except:
                print('抓取失败')

        self.outputer.output_html()





if __name__=='__main__':
    rooturl = 'http://baike.baidu.com/item/dota2'
    obj_spider = Spidermain()
    obj_spider.crawl(rooturl)
