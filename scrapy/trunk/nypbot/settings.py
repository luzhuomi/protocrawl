#Scrapy settings for nypbot project

BOT_NAME = 'nypbot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['nypbot.spiders']
NEWSPIDER_MODULE = 'nypbot.spiders'
DEFAULT_ITEM_CLASS = 'nypbot.items.Website'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['nypbot.pipelines.FilterWordsPipeline']

RANDOMIZE_DOWNLOAD_DELAY=False
DOWNLOAD_DELAY=1.0
#CONCURRENT_REQUESTS_PER_IP=40
