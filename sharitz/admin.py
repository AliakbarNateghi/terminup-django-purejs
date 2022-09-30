from django.contrib import admin
from .models import WeeklySchedule, ExamDate, course, studentChoise, College

# admin.site.register(Student)
admin.site.register(WeeklySchedule)
admin.site.register(ExamDate)
admin.site.register(course)
admin.site.register(studentChoise)
admin.site.register(College)

