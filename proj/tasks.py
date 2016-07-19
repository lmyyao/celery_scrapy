from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# Ref
# http://docs.celeryproject.org/en/latest/userguide/tasks.html
#

# class DebugTask(Task):
#     abstract = True
#
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         print('Task returned: {0!r}'.format(task_id))
#
#
# @app.task(bind=True, default_retry_delay=10, max_reties=3, base=DebugTask)
# def add(self, x, y):
#     logger.info("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#     logger.info(self.request)
#     try:
#         return x + y
#     except Exception as e:
#         return self.retry(exc=e)
#
#
# @periodic_task(run_every=timedelta(seconds=10), exchange="default", routing_key="default")
# def every_monday_morning():
#     print("This is run every Monday morning at 7:30")
#     return 1


from celery.task import PeriodicTask

from datetime import timedelta


class Lmy(PeriodicTask):
    run_every = timedelta(seconds=60)
    options = {"exchange": "default", "routing_key": "default"}
    name = "xxxxx"

    def run(self):
        import scrapy
        from scrapy.crawler import CrawlerProcess

        URL = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1' \
              '&st=-1&fr=&sf=1&fmq=1468240179138_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=' \
              '&height=&face=0&istype=2&itg=0&uptype=urlsearch&ie=utf-8&word=%E6%9F%B3%E5%B2%A9'

        class LiuYanSpider(scrapy.Spider):
            name = "xxxxx"
            start_urls = [URL]

            def parse(self, response):
                urls = response.selector.re("http://g.hiphotos.baidu.com(.*?)\.jpg")
                for i in urls:
                    print("http://g.hiphotos.baidu.com{}.jpg".format(i))

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            "LOG_ENABLED": False
        })

        process.crawl(LiuYanSpider)
        process.start()
