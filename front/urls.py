from django.urls import path
from .views import courseList

urlpatterns = [
    path('list/', courseList.as_view(), name='courseList'),
]