from django.urls import path
from .views import courseList, mainList, loginView, idView

urlpatterns = [
    path('list/', courseList.as_view(), name='courseList'),
    path('main/', mainList.as_view(), name='main'),
    path('login/', loginView, name='login'),
    path('id/', idView, name='id')
]
