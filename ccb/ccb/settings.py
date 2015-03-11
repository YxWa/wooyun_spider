# -*- coding: utf-8 -*-

# Scrapy settings for ccb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ccb'

SPIDER_MODULES = ['ccb.spiders']
NEWSPIDER_MODULE = 'ccb.spiders'
ITEM_PIPELINES = {
    'ccb.pipelines.CcbPipeline':300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ccb (+http://www.yourdomain.com)'
