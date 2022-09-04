from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy
from sharitz.models import studentChoise, course
from . import custom
from .custom import WeeklyChoise, ExamChoise


def list(request):
    return render(request, 'list.html')


class CourseList(ListView):
    model = course
    context_object_name = 'courses'


class CourseDetail(DetailView):
    model = course
    context_object_name = 'course'
    template_name = 'course.html'


def CourseAdd(request):
    if request.method == 'POST':
        student = request.user
        title = request.POST.get('title')
        code = int(request.POST.get('code'))
        professor = request.POST.get('professor')
        weeklySchedule = WeeklyChoise(student)
        examDate = ExamChoise(student)
        college = request.POST.get('college')
        group = int(request.POST.get('group'))
        unit = int(request.POST.get('unit'))

        newCourse = studentChoise(
            student=student,
            title=title,
            code=code,
            professor=professor,
            weeklySchedule=weeklySchedule,
            examDate=examDate,
            college=college,
            group=group,
            unit=unit)

        newCourse.save()


class CourseDelete(DeleteView):
    model = studentChoise
    context_object_name = 'course'
    success_url = reverse_lazy('courses')
