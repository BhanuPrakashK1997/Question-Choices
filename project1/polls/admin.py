from django.contrib import admin
from .models import Question,Choice


# Register your models her

admin.site.register(Question)
admin.site.register(Choice)