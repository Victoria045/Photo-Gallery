from django.urls import path,re_path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name='photos-index'),
    path('search', views.search_results, name='search'),
    re_path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)