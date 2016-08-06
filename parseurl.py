import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analyst.settings")

from mysites.models import BBCNews



class BaseParser(object):

	def __init__(self, objects):
		self.objects = objects
		self.d = {}

	def parse_urls(self):
		num = 1
		self.d = {}
		l  = []
		# objects = BBCNews.objects.all()
		for obj in self.objects:

			processed_url = obj.url.split("/")[-1:]
			for url in processed_url:
				self.d[num]= url
				num += 1

		for key, value in self.d.iteritems():	
			value = value.split("-")

			try:
				new_val = value[1]

			except IndexError, e:
				new_val = value[0]
			if new_val == "ns_mchannel=rss&ns_source=PublicRSS20":
				new_val = "us"
			l.append(new_val)
		return l

		

	def last_identifier(self):
		'''
		sanity check to see ordering and make sure the 
		first element in the list is the last element 
		in the db
		'''

		return self.objects[0].id


	def taggit(self, l):

		'''
		di: takes in a dict from the method of reversed_list()
		checks the key matches it with the id of the object in 
		the db. Finally it populates the db with tags based on
		the id.
		'''

		import itertools
		for obj, item in itertools.izip(self.objects, l):
			try:
				obj.tags = item
				obj.save()
			except Exception, e:
				print "error here", e

class BBCParser(BaseParser):

	def __init__(self, objects,**args, **kwargs):
		super(PoliticoParser, self).__init__(self, **args, **kwargs)


class PoliticoParser(BaseParser):
	
	def __init__(self, objects,**args, **kwargs):
		super(PoliticoParser, self).__init__(self, **args, **kwargs)

	def parse_urls(self):



			




p = BBCParser(objects= BBCNews.objects.all())
l =  p.parse_urls()
print l[0]
# li = p.reverse_list(l)
# p.taggit(l)