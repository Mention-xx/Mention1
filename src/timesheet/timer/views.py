from django.shortcuts import render_to_response
from timesheet.timer.models import Activity
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import ordinal
from django.db.models import Q
import datetime

# TODO: Can I retreive this through the URL resolution methods?
@login_required(login_url='/account/login')
def activity_timer(request, *args, **kwargs):
    current_time = datetime.datetime.now()

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
        'current_time': current_time.strftime('%A, %B ') + ordinal(current_time.strftime('%d')) + current_time.strftime(' %I:%M:%S %p'),
        'todays_activities': Activity.objects.today().filter(delegate = request.user),
        'clock_in': clock_in
    }

    return render_to_response('timer/activity_timer.html', template_data,
               context_instance=RequestContext(request))

