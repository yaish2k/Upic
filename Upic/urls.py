from django.conf.urls import patterns, include, url
import upic_app.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/v1/', include(upic_app.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
