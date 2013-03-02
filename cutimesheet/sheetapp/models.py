from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#sheet can have one user, multiple weeks
class Sheet(models.Model):
    submitted = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User)

    def __unicode__(self):
        #return self.person + self.submitted.strftime('%m/%d/%Y')
        return self.submitted.strftime('%m/%d/%Y')

#week can have one sheet, multiple days
class Week(models.Model):
    sheet = models.ForeignKey(Sheet)

class Day(models.Model):
    #name = models.CharField(max_length=10)

    week = models.ForeignKey(Week)

    SUNDAY = 'SUN'
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    DAY_OF_WEEK_CHOICES = (
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday')
    )
    weekday = models.CharField(max_length=3,
                              choices=DAY_OF_WEEK_CHOICES,
			      default=SUNDAY)

    start_time = models.TimeField()
    end_time = models.TimeField()
    start_time2 = models.TimeField()
    end_time2 = models.TimeField()

    def __unicode__(self):
        return self.weekday

