from django.contrib import admin
from .models import ws, ExamDate, course, studentChoise, College

admin.site.register(ws)
admin.site.register(ExamDate)
admin.site.register(course)
admin.site.register(studentChoise)
admin.site.register(College)

