"""analyst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from articles.views import HomeViews as homeviews
from articles.views import single_view as singleview
from articles.views import UpdateArticle as update_article
from articles.views import article_form_view as article_form_view
from articles.views import ArticleDeletion as delete_article
from articles.views import delete_own_comment as delete_comment
from articles.views import VoteFormView as vote_view
from articles.views import tag_page as tag_page
from articles.views import about as about


from mysites.views import featured_news as featured_news
from mysites.views import politics as politics


from accounts.views import UserProfileDetailView as user_profile
from accounts.views import UserProfileEditView as user_edit
from django.contrib.auth.decorators import login_required as auth
from haystack.query import SearchQuerySet
from haystack.views import SearchView

sqs = SearchQuerySet().order_by('-date')
urlpatterns = [
   
    url(r'^admin/', include(admin.site.urls)),
    #--------------------------------homepage --------------------------------
    url (r'^logs/$', homeviews.as_view(), name='logs'),

    url(r'^$', SearchView(
                               load_all=False,
                               searchqueryset=sqs,
                               ),
                           name='haystack_search',
                           ),

    url(r'^article/submission/$', article_form_view, name="article_form_view"),
    url(r'^article/(?P<slug>[\w-]+)/$', singleview, name="single_view"), 
    url(r'^article/update/(?P<slug>[\w-]+)/$', update_article.as_view(), name="update_article"),
    url(r'^article/delete/(?P<slug>[\w-]+)/$', delete_article.as_view(), name="delete_article"),
    url(r'^comments/delete_own/(?P<id>.*)/$', delete_comment, name='delete_comment'), 
    url(r'^article/tag/(?P<tag>[\w-]+)/$', tag_page, name="tag_page"),
    url(r'^vote/$', auth(vote_view.as_view()), name="vote"),
    url(r'^about/$',about, name="about"),


    #-------------------------------Account handling --------------------------
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^users/(?P<slug>[\w-]+)/$', user_profile.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(user_edit.as_view()), name="edit_profile"),
    

    #------------------------------Commenting Section---------------------------
    url(r'^comments/', include('django_comments.urls')),
    

    #----------------------------------News views --------------------------------

    

    url(r'^news/featured-news/$', featured_news, name='featured_news'),
    url(r'^news/politics/$', politics, name='politics'),


    #----------------------------------Django in apps-----------------------------
    
    url(r'^markdownx/', include('markdownx.urls')),
    #----------------------------------production Deletables ---------------------
    
    
]


