from django.urls import path

from . import views
from .views import courseList, mainList, loginView, idView, collegeList, registerView

urlpatterns = [
    path('list/', courseList.as_view(), name='courseList'),
    # path('', mainList.as_view(), name='mainList'),
    path('', collegeList.as_view(), name='collegeList'),
    path('login/', views.loginView, name='login'),
    path('register/', registerView.as_view(), name='register'),
    path('id/', idView, name='id')
]
