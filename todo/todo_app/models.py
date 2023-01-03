from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# set up database tables

# todo items
class Todo(models.Model):
    NOT_STARTED = 'Not Started'
    ON_GOING = 'Ongoing'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (ON_GOING, 'Ongoing'),
        (COMPLETED, 'Completed')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default=NOT_STARTED)

# string representation of model
    def __str__(self):
        return self.name

# default ordering
    class Meta:
        ordering = ['-updated_timestamp']
