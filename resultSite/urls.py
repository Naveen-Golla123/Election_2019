from django.urls import path
from . import views

urlpatterns = [
    path('', views.mai, name='main'),
    path('news', views.news, name='news'),
    path('news-desc', views.news_desc, name='news_desc')
]
