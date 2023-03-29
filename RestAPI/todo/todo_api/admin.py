from django.contrib import admin

# Register your models here.

from .models import Todo, Purpose

admin.site.register(Todo)
admin.site.register(Purpose)
