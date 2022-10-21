from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import loginView, aboutView, collegeList, registerView, donateView, addCourse, printView, deleteView, index, DeleteView

urlpatterns = [
    path('home/', collegeList.as_view(), name='collegeList'),
    path('', index, name='index'),
    path('login/', loginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', registerView.as_view(), name='register'),
    path('about/', aboutView, name='about'),
    path('donate/', donateView, name='donate'),
    path('addcourse/', addCourse, name='addCourse'),
    path('print/', printView.as_view(), name='print'),
    path('delete/', deleteView, name='delete'),
    path('deletee/', DeleteView, name='deletee'),
]
