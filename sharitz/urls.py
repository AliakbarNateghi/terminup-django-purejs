from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overwiew'),
    path('course-list/', views.courseList, name='task-list'),
    path('course-detail/<str:pk>/', views.courseDetail, name='task-detail'),
    path('course-create/', views.courseCreate, name='task-create'),
    path('course-update/<str:pk>/', views.courseUpdate, name='task-update'),
    path('course-delete/<str:pk>/', views.courseDelete, name='task-delete'),
]
