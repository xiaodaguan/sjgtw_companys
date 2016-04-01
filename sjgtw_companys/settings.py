# -*- coding: utf-8 -*-

# Scrapy settings for sjgtw_companys project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
DOWNLOAD_DELAY = 1
BOT_NAME = 'sjgtw_companys'

SPIDER_MODULES = ['sjgtw_companys.spiders']
NEWSPIDER_MODULE = 'sjgtw_companys.spiders'

# Retry many times since proxies often fail
RETRY_TIMES = 3
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
     'sjgtw_companys.middlewares.RandomProxy': 100,
     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

ITEM_PIPELINES={
    # 'Lianjia.pipelines.pipelines.LianjiaJsonPipeline':300,
    'sjgtw_companys.pipelines.SjgtwCompanysPipeline':800
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sjgtw_companys (+http://www.yourdomain.com)'

PROXY_LIST = 'proxys.txt'