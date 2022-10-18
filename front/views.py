from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy, reverse
from sharitz.models import studentChoise, course, College, ExamDate
from . import custom
from .custom import WeeklyChoise, ExamChoise
from .forms import CreateUserForm


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'message': ' با موفقیت وارید شدید '})

    return HttpResponseRedirect(reverse('collegeList'))


def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html', {'message': ' لطفا دوباره متحان کنید '})


class registerView(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = _name = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registerView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(registerView, self).get(*args, **kwargs)


def aboutView(request):
    return render(request, 'about.html')


def donateView(request):
    return render(request, 'donate.html')


def test(request):
    return render(request, 'test.html')


class mainList(LoginRequiredMixin, ListView):
    model = course
    context_object_name = 'courses'
    template_name = 'mainpage.html'


class collegeList(LoginRequiredMixin, ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'mainpage.html'


class CourseDetail(LoginRequiredMixin, DetailView):
    model = course
    context_object_name = 'course'
    template_name = 'course.html'


@login_required(redirect_field_name='index')
@csrf_exempt
def addCourse(request):
    if request.method == 'POST':
        student = request.user
        for a in range(1000):
            course_id = request.POST.get(str(a))
            if course_id != None:
                newCourse = studentChoise(student=student, course_id=course_id)
                newCourse.save()

    return render(request, 'print.html')


@login_required(redirect_field_name='index')
def printView(request):
    fuckingList = {}
    j = 0
    course_id = list(course.objects.all().values('id'))
    listOfED = list(ExamDate.objects.all().values('id'))
    studentChoise_id = list(studentChoise.objects.all().values('course_id'))

    for i in course_id:
        for j in studentChoise_id:
            if i == j:
                title = i['title']

    # context = {
    #     'title': title,
    # }

    # for c in listOfChoise:
    #     for a in listOfCourses:
    #         if a["examDate_id"] == c["id"]:
    #             courseId = a["id"]
    #             title = a["title"]
    #             code = a["code"]
    #             group = a["group"]
    #             unit = a["unit"]
    #             professor = a["professor"]
    #             ps = a["ps"]
    #             examDate_id = a["examDate_id"]
    #
    #             for b in listOfED:
    #                 if b["id"] == examDate_id:
    #                     testDate = b["date"]
    #                     testStart = b["start"]
    #                     j += 1
    #                     fuckingList += {
    #                         'title': title,
    #                         'code': code,
    #                         'group': group,
    #                         'unit': unit,
    #                         'professor': professor,
    #                         'ps': ps,
    #                         'testDate': testDate,
    #                         'testStart': testStart,
    #                         'j': j
    #                     }
                        # return render(request, 'print.html', context)

    # for d in fuckingList:
    #     context = d

    return render(request, 'print.html')
    # return HttpResponseRedirect(reverse('print'))

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = studentChoise
    context_object_name = 'course'
    success_url = reverse_lazy('courses')
