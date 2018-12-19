"""famaeGr10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.map, name="map"),
    # url(r'^city/(?P<city>\w{1,50})$', views.jsonByCity, name="jsonByCity"),
    url(r'^api/all/', views.byCity, name="all"),
    url(r'^api/city/(?P<id>[\s\w]+)$', views.byCity, name="byCity"),
    url(r'^api/search/(?P<search>[\s\w]+)$', views.autocomplete, name="autocomplete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
