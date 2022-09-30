from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('course-list/', views.courseList, name='course-list'),
    path('college-list/', views.collegeList, name='college-list'),
    path('course-detail/<str:pk>/', views.courseDetail, name='course-detail'),
    path('course-create/', views.courseCreate, name='course-create'),
    path('course-update/<str:pk>/', views.courseUpdate, name='course-update'),
    path('course-delete/<str:pk>/', views.courseDelete, name='course-delete'),
]
