from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import mainList, loginView, aboutView, collegeList, registerView, donateView, addCourse, test, printView, deleteView, index

urlpatterns = [
    # path('', mainList.as_view(), name='mainList'),
    path('home/', collegeList.as_view(), name='collegeList'),
    path('', index, name='index'),
    path('login/', loginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', registerView.as_view(), name='register'),
    path('about/', aboutView, name='about'),
    path('donate/', donateView, name='donate'),
    path('addcourse/', addCourse, name='addCourse'),
    path('test/', test, name='test'),
    path('print/', printView.as_view(), name='print'),
    path('delete/', deleteView, name='delete'),
]
