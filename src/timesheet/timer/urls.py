from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^activity/list/$|^$', views.activity_list, name='timesheet-activity-list'),
    url(r'^activity/create/$', views.create_activity, name='timesheet-activity-create'),
    url(r'^activity/(?P<object_id>\d+)/update/$', views.update_activity, name='timesheet-update-activity'),
    url(r'^activity/(?P<object_id>\d+)/delete/$', views.delete_activity, name='timesheet-delete-activity'),
)

