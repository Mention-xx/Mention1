from django.db import models
from django.contrib.auth.models import User

### TODO: Apply i18n translations to this text
ACTIVITY_CHOICES = (
    (1001, 'Project Management'),
    (1002, 'Project Management - Documentation'),
    (2001, 'Consulting'),
    (2002, 'Consulting - Research'),
    (2003, 'Consulting - Analysis'),
    (2004, 'Consulting - Implementation'),
    (3001, 'Development'),
    (3002, 'Development - Coding'),
    (3003, 'Development - Testing'),
    (3004, 'Development - Design'),
    (4001, 'Implementation'),
    (4002, 'Implementation - Training'),
    (4003, 'Implementation - Testing'),
    (9000, 'Additional Cost'),
)

class Activity(models.Model):
    """ A piece of work that has been done within a specific amount of time. """

    class Meta(object):
        verbose_name_plural = 'activities'

    started = models.DateTimeField()
    finished = models.DateTimeField(null=True, blank=True)

    delegate = models.ForeignKey(User, null=True, blank=True)

    activity = models.PositiveIntegerField(
        choices=ACTIVITY_CHOICES,
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)

    def time_taken(self):
        """ Get the amount of time that this project has taken. """

        return self.finished - self.started

    def __unicode__(self):
        """ Get a textual representation of this activity. """

        return '%s, %s "%s" %s' % (
            self.get_activity_display(),
            self.delegate.first_name,
            self.delegate.username,
            self.delegate.last_name
        )

