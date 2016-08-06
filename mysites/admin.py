from __future__ import unicode_literals
from django.contrib import admin
from .models import BBCNews, NewsWebsite, ReutersNews, ReutersWebsite
from .models import AljazeeraNews, AljazeeraWebsite
from .models import PoliticoNews, PoliticoWebsite
from .models import Economist, EconomistNews
from .models import WikiWebsite, WikiNews 
from .models import ChristianScienceMonitor, ChristianScienceMonitorWebsite

from .models import APNews, APWebsite
from .models import GuardianNews, GuardianWebsite, CNNWebsite, CNNNews

from .models import APNews, APWebsite, GuardianNews, GuardianWebsite
from .models import HuffpoWebsite, HuffpoNews, France24Website, France24News

class NewsWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class NewsAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True



class ReutersWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class ReutersAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)
	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url, title=instance.url)

	url_.allow_tags = True


class AljazeeraWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class AljazeeraAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_', 'company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)
	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url, title=instance.url)

	url_.allow_tags = True



class PoliticoWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class PoliticoAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True



class EconomistWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class EconomistAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True




class WikiWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class WikiAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True


class ChristianWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class ChristianAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True

class APWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{head}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class APAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True

class GuardianWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class GuardianAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True



class HuffpoWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class HuffpoAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True

class CNNWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class CNNAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True

class FranceWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class FranceAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company', 'featured',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True


admin.site.register(France24Website, FranceWebsiteAdmin)
admin.site.register(France24News, FranceAdAdmin)

admin.site.register(HuffpoWebsite, HuffpoWebsiteAdmin)
admin.site.register(HuffpoNews, HuffpoAdAdmin)

admin.site.register(CNNWebsite, CNNWebsiteAdmin)
admin.site.register(CNNNews, CNNAdAdmin)

admin.site.register(GuardianWebsite, GuardianWebsiteAdmin)
admin.site.register(GuardianNews, GuardianAdAdmin)

admin.site.register(NewsWebsite, NewsWebsiteAdmin)
admin.site.register(BBCNews, NewsAdAdmin)

admin.site.register(ReutersWebsite, ReutersWebsiteAdmin)
admin.site.register(ReutersNews, ReutersAdAdmin)

admin.site.register(AljazeeraWebsite, AljazeeraWebsiteAdmin)
admin.site.register(AljazeeraNews, AljazeeraAdAdmin)

admin.site.register(PoliticoWebsite, PoliticoWebsiteAdmin)
admin.site.register(PoliticoNews, PoliticoAdAdmin)

admin.site.register(Economist, EconomistWebsiteAdmin)
admin.site.register(EconomistNews, EconomistAdAdmin)

admin.site.register(WikiWebsite, WikiWebsiteAdmin)
admin.site.register(WikiNews, WikiAdAdmin)

admin.site.register(ChristianScienceMonitorWebsite, ChristianWebsiteAdmin)
admin.site.register(ChristianScienceMonitor, ChristianAdAdmin)

admin.site.register(APWebsite, APWebsiteAdmin)
admin.site.register(APNews, APAdAdmin)
