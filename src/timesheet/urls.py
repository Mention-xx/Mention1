from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^account/', include('django.contrib.auth.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^timesheet/', include('timesheet.timer.urls')),

    (r'^$', 'timesheet.timer.views.activity_list'),
)

