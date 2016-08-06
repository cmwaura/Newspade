from __future__ import unicode_literals


from django.db import models
from django.db.models.signals import pre_delete
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.dispatch import receiver
# Create your models here.



class NewsWebsite(models.Model):
	

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)



class BBCNews(models.Model):
	

	news_website = models.ForeignKey(NewsWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="BBC News", max_length=100)
	featured = models.BooleanField(default=False)
	tags = models.CharField(max_length=40, null=True, blank=True)
	image = models.ImageField()

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "BBCNews"



class NewsAdItem(DjangoItem):
	'''
	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
	django database.
	'''

	django_model = BBCNews


class ReutersWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class ReutersNews(models.Model):

	news_website = models.ForeignKey(ReutersWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Reuters", max_length=100)
	featured = models.BooleanField(default=False)
	image = models.ImageField()
	tags = models.CharField(max_length=30, default="US")
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "ReutersNews"

class ReutersAdItem(DjangoItem):

	django_model = ReutersNews

class AljazeeraWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class AljazeeraNews(models.Model):

	news_website = models.ForeignKey(AljazeeraWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Aljazeera", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "AljazeeraNews"

class AljazeeraAdItem(DjangoItem):

	django_model = AljazeeraNews

class PoliticoWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class PoliticoNews(models.Model):

	news_website = models.ForeignKey(PoliticoWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Politico", max_length=100)
	featured = models.BooleanField(default=False)
	tags = models.CharField(default="Politics", max_length=30)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Politico News"

class PoliticoAdItem(DjangoItem):

	django_model = PoliticoNews


class Economist(models.Model):
	

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)




class EconomistNews(models.Model):
	

	news_website = models.ForeignKey(Economist)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Economist", max_length=100)
	featured = models.BooleanField(default=False)
	

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Economist News"



class EconomistAdItem(DjangoItem):
	'''
	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
	django database.
	'''

	django_model = Economist

class WikiWebsite(models.Model):
	
	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class WikiNews(models.Model):
	

	news_website = models.ForeignKey(WikiWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Wiki", max_length=100)
	featured = models.BooleanField(default=False)
	

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Wiki News"



class WikiAdItem(DjangoItem):
	

	django_model = WikiNews

class ChristianScienceMonitorWebsite(models.Model):
	

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name = "Christian Science Website"

class ChristianScienceMonitor(models.Model):
	

	news_website = models.ForeignKey(ChristianScienceMonitorWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Christian Science Monitor", max_length=100)
	featured = models.BooleanField(default=False)
	

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Christian Science Monitor News"



class ChristianScienceMonitorAdItem(DjangoItem):
	'''
	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
	django database.
	'''

	django_model = ChristianScienceMonitor


class APWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	class Meta:
		
		verbose_name_plural = "Associated Press Website"


class APNews(models.Model):

	news_website = models.ForeignKey(APWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Associated press", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Associated Press News"

class APAdItem(DjangoItem):

	django_model = APNews



class GuardianWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	class Meta:
		
		verbose_name_plural = "Guardian Website"



class GuardianWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	class Meta:
		
		verbose_name_plural = "Guardian Website"



class GuardianNews(models.Model):

	news_website = models.ForeignKey(GuardianWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="The Guardian", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Guardian News"

class GuardianItem(DjangoItem):

	django_model = GuardianNews



class CNNWebsite(models.Model):
	

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	class Meta:
		
		verbose_name_plural = "CNN Website"



class CNNNews(models.Model):

	news_website = models.ForeignKey(CNNWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="CNN", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "CNN News"

class CNNItem(DjangoItem):

	django_model = CNNNews


class HuffpoWebsite(models.Model):
	
	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name_plural = "Huffington Post Website"



class HuffpoNews(models.Model):

	news_website = models.ForeignKey(HuffpoWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Huffington Post", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Huffington Post News"

class HuffingtonItem(DjangoItem):

	django_model = HuffpoNews


class France24Website(models.Model):
	
	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name_plural = "France24 Website"



class France24News(models.Model):

	news_website = models.ForeignKey(France24Website)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(default="description", null=True, blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="France24", max_length=100)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "France24"

class France24Item(DjangoItem):

	django_model = France24News




@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):

	if isinstance(instance, NewsWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()
	if isinstance(instance, BBCNews):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

	if isinstance(instance, GuardianWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()	
	if isinstance(instance, GuardianNews):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

	if isinstance(instance, ReutersWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()	
	if isinstance(instance, ReutersNews):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

	if isinstance(instance, PoliticoWebsite):
		if instance.scraper_runtime:

			instance.scraper_runtime.delete()	

			instance.scraper_runtime.delete()
	if isinstance(instance, PoliticoNews):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

	if isinstance(instance,ChristianScienceMonitorWebsite):
                if instance.scraper_runtime:
                        instance.scraper_runtime.delete()
        if isinstance(instance, ChristianScienceMonitor):
                if instance.checker_runtime:
                        instance.checker_runtime.delete()


pre_delete.connect(pre_delete_handler)
