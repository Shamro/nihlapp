from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^/$', 'nihlapp.core.views.stats.summary'),
    (r'^/seeding$', 'nihlapp.core.views.stats.seeding'),
    (r'^/season$', 'nihlapp.core.views.stats.season'),
    (r'^/playoffs$', 'nihlapp.core.views.stats.playoffs'),
    (r'^/tournament$', 'nihlapp.core.views.stats.tournament'),
)