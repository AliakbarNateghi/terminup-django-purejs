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
        return render(request, 'login.html', {'message': ' لطفا دوباره امتحان کنید '})


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


listOfUsed = []


@login_required(redirect_field_name='index')
@csrf_exempt
def addCourse(request):
    if request.method == 'POST':
        student = request.user
        for a in range(1000):
            choiseId = request.POST.get('id-' + str(a))
            title = request.POST.get('title-' + str(a))
            code = request.POST.get('code-' + str(a))
            professor = request.POST.get('professor-' + str(a))
            group = request.POST.get('group-' + str(a))
            unit = request.POST.get('unit-' + str(a))
            ps = request.POST.get('ps-' + str(a))
            examDate = request.POST.get('examDate-' + str(a))
            examStart = request.POST.get('examStart-' + str(a))

            if choiseId is not None:
                listOfUsed.append(choiseId)
                newChoise = studentChoise(student=student,
                                          title=title,
                                          code=code,
                                          professor=professor,
                                          group=group,
                                          unit=unit,
                                          ps=ps,
                                          examDate=examDate,
                                          examStart=examStart)
                newChoise.save()

    return HttpResponseRedirect(reverse('collegeList'))


class printView(LoginRequiredMixin, ListView):
    model = studentChoise
    context_object_name = 'choises'
    template_name = 'print.html'


@login_required(redirect_field_name='index')
def deleteView(request):
    if request.method == 'POST':
        choiseId = request.POST.get('id')
        deleteItem = studentChoise.objects.get(id=choiseId)
        deleteItem.delete()

        for i in listOfUsed:
            if i == choiseId:
                listOfUsed.remove(i)

    return HttpResponseRedirect(reverse('print'))
