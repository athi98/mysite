from __future__ import unicode_literals
from polls.models import Question, Choice
from django.db import models
from django.contrib import admin


admin.site.register(Question)
admin.site.register(Choice)



# Register your models here.
