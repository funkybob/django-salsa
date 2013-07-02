
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    (r'^$', 'django.shortcuts.render', {'template_name': 'salsa/console/index.html'}),
)

