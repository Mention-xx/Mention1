from django.db.models import Manager, Q
import models
import datetime

class ActivityManager(Manager):
    def today(self):
#        return super(ActivityManager, self).get_query_set().filter(
#            Q(started_original__date=datetime.datetime.today().date())
#        )

        return super(ActivityManager, self).get_query_set().filter(
            started_original__year=datetime.datetime.today().year,
            started_original__month=datetime.datetime.today().month,
            started_original__day=datetime.datetime.today().day,
        )

