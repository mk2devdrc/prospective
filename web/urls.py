
from django.conf.urls import url

from .views import HomeView, NewsDetail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetail.as_view(), name='news-detail'),
]
