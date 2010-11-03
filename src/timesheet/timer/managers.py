from django.db.models import Manager, Q
import models
import datetime

class ActivityManager(Manager):
    def today(self):
#        return super(ActivityManager, self).get_query_set().filter(
#            Q(started_original__date=datetime.datetime.today().date())
#        )

        todays_date = datetime.datetime.today().date()

        return super(ActivityManager, self).get_query_set().filter(
            Q (
                started_original__year = todays_date.year,
                started_original__month = todays_date.month,
                started_original__day = todays_date.day,
             ) | Q (
                finished_original__year = todays_date.year,
                finished_original__month = todays_date.month,
                finished_original__day = todays_date.day,
             )
        )

