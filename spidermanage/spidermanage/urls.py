"""spidermanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.conf.urls import include, url
import route.mainroute as route
from django.views.generic import RedirectView
urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^nmaptool/', include('nmaptoolbackground.urls',namespace='nmaptool')),
    url(r'^admin/', admin.site.urls),
    url(r'^status',route.indexpage,name='status'),
    url(r'^test/$', route.test, name='test'),
    url(r'^testdata/$', route.testdata, name='testdata'),
    url('^search/', include('fontsearch.urls',namespace='fontsearch')),
    url('^', include('fontsearch.urls',namespace='fontsearch'))
 
]
