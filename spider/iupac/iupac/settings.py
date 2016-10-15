# -*- coding: utf-8 -*-

# Scrapy settings for iupac project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iupac'

SPIDER_MODULES = ['iupac.spiders']
NEWSPIDER_MODULE = 'iupac.spiders'

AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 0.1
RANDOMIZE_DOWNLOAD_DELAY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Power by Scrapy;For research;More info At:(+http://hong.im/about-me)'
