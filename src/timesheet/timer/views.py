from django.shortcuts import render_to_response
from timesheet.timer.models import Activity
from django.template import RequestContext

def activity_timer(request):
    template_data = {}
    return render_to_response('timer/activity_timer.html', template_data,
               context_instance=RequestContext(request))

