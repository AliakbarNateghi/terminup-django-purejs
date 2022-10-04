from django.urls import path
from .views import courseList, mainList, loginView, idView, collegeList

urlpatterns = [
    path('list/', courseList.as_view(), name='courseList'),
    # path('', mainList.as_view(), name='mainList'),
    path('', collegeList.as_view(), name='collegeList'),
    path('login/', loginView, name='login'),
    path('id/', idView, name='id')
]
