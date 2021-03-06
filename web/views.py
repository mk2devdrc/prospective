from django.shortcuts import render
from django.views import generic

from web import models

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'web/french/index.html'

class NewsDetail(generic.DetailView):
    model = models.Francais
    template_name = 'web/french/detailed_news.html'


class LingalaHomeView(generic.TemplateView):
    template_name = 'web/lingala/index.html'


class LingalaNewsDetail(generic.DetailView):
    model = models.Lingala
    template_name = 'web/lingala/detailed_news.html'
