import datetime
import itertools
from itertools import izip_longest



from django.shortcuts import render, Http404

from .models import BBCNews, ReutersNews, AljazeeraNews, PoliticoNews, GuardianNews, HuffpoNews

from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

yesterday = datetime.date.today()-datetime.timedelta(2)
	
def featured_news(request):
	
	# qs1 =  BBCNews.objects.order_by("-date").first()
	qs1 =  BBCNews.objects.filter(date__gte=yesterday).order_by("-date","-id")
	qs2 = ReutersNews.objects.filter(date__gte=yesterday).order_by("-date","-id")
	qs3 = PoliticoNews.objects.filter(date__gte=yesterday).order_by("-date","-id")
	qs4 =  GuardianNews.objects.filter(date__gte=datetime.date.today).order_by("-id")
	qs5 = HuffpoNews.objects.filter(date__gte=datetime.date.today).order_by("-id")
	try:			
		queryset = [x for x in itertools.chain.from_iterable(izip_longest(qs5,qs1, qs2, qs3, qs4))]
		
		for items in queryset:
			if items is None:
				queryset.remove(items)

		context = {"featured":queryset}
		template_name = 'news/featured.html'
		return render(request, template_name, context)
	except:
		raise Http404

def politics(request):
	
	queryset  = PoliticoNews.objects.filter(date__gte=yesterday).order_by("-date","-id")
	context = {"featured": queryset}
	template_name = 'news/featured.html'
	return render(request, template_name, context)

