from __future__ import unicode_literals

from dynamic_scraper.spiders.django_spider import DjangoSpider
from mysites.models import BBCNews, NewsWebsite, NewsAdItem 
from mysites.models import ReutersNews, ReutersWebsite, ReutersAdItem
from mysites.models import AljazeeraNews, AljazeeraWebsite, AljazeeraAdItem
from mysites.models import PoliticoNews, PoliticoWebsite, PoliticoAdItem
from mysites.models import Economist, EconomistNews, EconomistAdItem
from mysites.models import WikiWebsite, WikiNews, WikiAdItem
from mysites.models import ChristianScienceMonitor, ChristianScienceMonitorWebsite, ChristianScienceMonitorAdItem
from mysites.models import GuardianWebsite, GuardianNews, GuardianItem
from mysites.models import HuffpoWebsite, HuffpoNews, HuffingtonItem
from mysites.models import France24Website, France24News, France24Item

class NewsSpider(DjangoSpider):

	name = 'news_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(NewsWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = BBCNews
		self.scraped_obj_item_class = NewsAdItem
		super(NewsSpider, self).__init__(self, *args, **kwargs)

class ReuterSpider(DjangoSpider):

	name = 'reuters_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(ReutersWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = ReutersNews
		self.scraped_obj_item_class = ReutersAdItem
		super(ReuterSpider, self).__init__(self, *args, **kwargs)

class AljazeeraSpider(DjangoSpider):

	name = 'aljazeera_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(AljazeeraWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = AljazeeraNews
		self.scraped_obj_item_class = AljazeeraAdItem
		super(AljazeeraSpider, self).__init__(self, *args, **kwargs)

class PoliticoSpider(DjangoSpider):

	name = 'politico_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(PoliticoWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = PoliticoNews
		self.scraped_obj_item_class = PoliticoAdItem
		super(PoliticoSpider, self).__init__(self, *args, **kwargs)


class EconomistSpider(DjangoSpider):

	name = 'economist_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(Economist, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = EconomistNews
		self.scraped_obj_item_class = EconomistAdItem
		super(EconomistSpider, self).__init__(self, *args, **kwargs)

class WikiSpider(DjangoSpider):

	name = 'wiki_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(WikiWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = WikiNews
		self.scraped_obj_item_class = WikiAdItem
		super(WikiSpider, self).__init__(self, *args, **kwargs)

class ChristianSpider(DjangoSpider):
	name = 'christian_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(ChristianScienceMonitorWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = ChristianScienceMonitor
		self.scraped_obj_item_class = ChristianScienceMonitorAdItem
		super(ChristianSpider, self).__init__(self, *args, **kwargs)

class GuardianSpider(DjangoSpider):
	name = 'guardian_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(GuardianWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = GuardianNews
		self.scraped_obj_item_class = GuardianItem
		super(GuardianSpider, self).__init__(self, *args, **kwargs)


class HuffpoSpider(DjangoSpider):
	name = 'huffpo_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(HuffpoWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = HuffpoNews
		self.scraped_obj_item_class = HuffingtonItem
		super(HuffpoSpider, self).__init__(self, *args, **kwargs)

class France24Spider(DjangoSpider):
	name = 'france_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(France24Website, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = France24News
		self.scraped_obj_item_class = France24Item
		super(France24Spider, self).__init__(self, *args, **kwargs)

