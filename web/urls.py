
from django.conf.urls import url

from .views import HomeView, NewsDetail, LingalaNewsDetail, LingalaHomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^lingala-news/$', LingalaHomeView.as_view(), name='ndaku'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news-detail'),
    url(r'^article/(?P<pk>\d+)/$', LingalaNewsDetail.as_view(), name='lingala-news-detail'),
]
