from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField(blank=True)
    created_date_time  = models.DateTimeField(auto_now_add=True)
    all_day = models.BooleanField(default=False, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
