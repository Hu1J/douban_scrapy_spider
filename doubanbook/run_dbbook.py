from scrapy import cmdline
import sys
import os

os.chdir("/home/guixuan/Documents/py/Python-spyder/doubanbook/doubanbook")
print("Running at --->:  "+os.getcwd())
cmdline.execute("scrapy crawl dbbook".split())