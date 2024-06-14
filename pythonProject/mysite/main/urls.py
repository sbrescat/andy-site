from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from main import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    #path('news/', views.news_home, name='news'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

