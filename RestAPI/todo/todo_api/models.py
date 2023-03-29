from django.db import models


# Create your models here.

class Purpose(models.Model):
    id = models
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Todo(models.Model):
    task = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    purpose = models.ForeignKey('Purpose', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.task
