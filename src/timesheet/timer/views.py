from django.views.generic.create_update import update_object, delete_object
from django.views.generic.list_detail import object_list
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.urlresolvers import reverse
from django.db.models import Q

from timesheet.timer.forms import ActivityForm
from timesheet.timer.models import Activity
import datetime

# TODO: Can I retreive this through the URL resolution methods?
def _get_current_time_string():
    current_time = datetime.datetime.now()

    return current_time.strftime('%A, %B ') + ordinal(current_time.strftime('%d')) + current_time.strftime(' %I:%M:%S %p')

@login_required(login_url='/account/login/')
def activity_list(request, *args, **kwargs):
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'timesheet/list.html'

    if 'queryset' not in kwargs:
        kwargs['queryset'] = Activity.objects.today().filter(delegate=request.user)

    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'activity'

    return object_list(request, *args, **kwargs)

@login_required(login_url='/account/login/')
def create_activity(request, *args, **kwargs):
    if request.user.has_perm('timer.add_activity') is not True:
        raise Http404()

    if request.method == 'POST':
        form = ActivityForm(request.POST)

        form.instance.delegate = request.user

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('timesheet-activity-list'))
        else:
            form = ActivityForm(request.POST)
    else:
        form = ActivityForm()

    extra_context = {
        'current_time': _get_current_time_string,
        'todays_activities': Activity.objects.today().filter(delegate = request.user),
        'form': form,
    }

    return render_to_response('timesheet/create.html', extra_context, context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def update_activity(request, *args, **kwargs):
    if request.user.has_perm('timer.change_activity') is not True:
        raise Http404()

    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'timesheet/update.html'

    if 'form_class' not in kwargs:
        kwargs['form_class'] = ActivityForm

    if 'post_save_redirect' not in kwargs:
        kwargs['post_save_redirect'] = reverse('timesheet-activity-list')

    return update_object(request, *args, **kwargs)

@login_required(login_url='/account/login/')
def delete_activity(request, *args, **kwargs):
    if request.user.has_perm('timer.delete_activity') is not True:
        raise Http404()

    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'timesheet/delete.html'

    if 'post_delete_redirect' not in kwargs:
        kwargs['post_delete_redirect'] = reverse('timesheet-activity-list')

    if 'model' not in kwargs:
        kwargs['model'] = Activity

    return delete_object(request, *args, **kwargs)

@login_required(login_url='/account/login/')
def activity_timer(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            this_activity = Activity.objects.get(delegate=request.user, finished_original=None)
            this_activity.finished_original = datetime.datetime.now()

        except Activity.DoesNotExist:
            this_activity = Activity()
            this_activity.started_original = datetime.datetime.now()

        if this_activity.delegate is None:
            this_activity.delegate = request.user

        this_activity.save()

        # Delete activities that don't consist of at least 15 minutes. TODO: Verify that we want this.
        if this_activity.started == this_activity.finished:
            this_activity.delete()

        return HttpResponseRedirect('/')

    try:
        this_activity = Activity.objects.get(delegate=request.user, finished_original=None)
        clock_in = False

    except Activity.DoesNotExist:
        clock_in = True

    template_data = {
        'current_time': _get_current_time_string,
        'todays_activities': Activity.objects.today().filter(delegate = request.user),
        'clock_in': clock_in
    }

    return render_to_response('timesheet/activity_timer.html', template_data,
               context_instance=RequestContext(request))

