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

    template_data = {
        'current_time': current_time.strftime('%A, %B ') + ordinal(current_time.strftime('%d')) + current_time.strftime(' %I:%M:%S %p'),
    }

    if request.method == 'POST':
        return HttpResponseRedirect('/')

    return render_to_response('timer/activity_timer.html', template_data,
               context_instance=RequestContext(request))

