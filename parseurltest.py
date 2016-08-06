import os
import sys

import unittest
from parseurl import Parser
from mysites.models import BBCNews

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analyst.settings")

class TestParser(unittest.TestCase):
	def setUp(self):
		self.p = Parser(objects= BBCNews.objects.all())
		self.objects = BBCNews.objects.all()
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_parseurl(self):
		final_result = "us"
		l = self.p.parse_urls()[0]
		l1 = self.p.parse_urls()[299]
		l2 = self.p.parse_urls()[1]
		self.assertEqual(l, "us")
		self.assertEqual(l1, final_result)
		self.assertEqual(l2, "arts")
	
	def test_taggit(self):
		import itertools
		li = ["us", "arts", "us", "environment", "us","us", "us", "us"]
		for l, obj in itertools.izip(li, self.objects[:8]):
			self.assertEqual(l,obj.tags)

if __name__ == '__main__':
	unittest.main()