from itertools import islice
from django import template
register = template.Library()

from web.models import Francais, Lingala


# http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python/22045226#22045226
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

# FRENCH TAGS SECTION
@register.inclusion_tag('web/lingala/fetch_latest_french_news.html')
def fetch_latest_lingala_news():
    news = Lingala.objects.all().order_by('date_creation')[:1]
    return {'news_group_list': list(chunk(news, 1))}

@register.inclusion_tag('web/lingala/all_french_news.html')
def fetch_all_lingala_news():
    news = Lingala.objects.all().order_by('-date_creation')[:4]
    return {'news_group_list': list(chunk(news, 4))}


@register.inclusion_tag('web/lingala/news_list.html')
def fetch_lingala_news():
    news = Lingala.objects.all().filter(categorie__nom_categorie='Politique').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}


@register.inclusion_tag('web/lingala/economie_list.html')
def fetch_lingala_economie_news():
    news = Lingala.objects.all().filter(categorie__nom_categorie='Economie').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}


@register.inclusion_tag('web/lingala/sports_list.html')
def fetch_lingala_sports_news():
    news = Lingala.objects.all().filter(categorie__nom_categorie='Sports').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}


# FRENCH TAGS SECTION
@register.inclusion_tag('web/french/fetch_latest_french_news.html')
def fetch_latest_french_news():
    news = Francais.objects.all().order_by('date_creation')[:1]
    return {'news_group_list': list(chunk(news, 1))}

@register.inclusion_tag('web/french/all_french_news.html')
def fetch_all_french_news():
    news = Francais.objects.all().order_by('-date_creation')[:4]
    return {'news_group_list': list(chunk(news, 4))}


@register.inclusion_tag('web/french/news_list.html')
def fetch_french_news():
    news = Francais.objects.all().filter(categorie__nom_categorie='Politique').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}


@register.inclusion_tag('web/french/economie_list.html')
def fetch_french_economie_news():
    news = Francais.objects.all().filter(categorie__nom_categorie='Economie').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}


@register.inclusion_tag('web/french/sports_list.html')
def fetch_french_sports_news():
    news = Francais.objects.all().filter(categorie__nom_categorie='Sports').order_by('-date_creation')[:3]
    return {'news_group_list': list(chunk(news, 3))}
