#!/usr/bin/env python 

import os
import time
import multiprocessing

def processors():
	os.system('scrapy crawl news_spider -a id=1 -a do_action=yes')
	print "sleeping"
	time.sleep(60)

	os.system('scrapy crawl politico_spider -a id=1 -a do_action=yes')
	print "sleeping"
	time.sleep(60)
	
	os.system('scrapy crawl reuters_spider -a id=1 -a do_action=yes')
	print "sleeping"
	time.sleep(60)
	
	os.system('scrapy crawl christian_spider -a id=1 -a do_action=yes')
	print "sleeping"
	time.sleep(60)
	
	os.system('scrapy crawl guardian_spider -a id=1 -a do_action=yes')
        print "sleeping"
        time.sleep(60)

	os.system('scrapy crawl wiki_spider -a id=1 -a do_action=yes')
        print "sleeping"
        time.sleep(60)

	os.system('python manage.py rebuild_index')
	os.system('Y')
	print "Finished tasks"
	
def main():
	p = multiprocessing.Process(target=processors)
	p.start()

main()
