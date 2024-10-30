from django.urls import path
from .views import *

urlpatterns = [
    path('register',TeacherStudentRegister.as_view(),name='register'),
    path('login',Login.as_view(),name='login'),
    path('student',Student.as_view(),name='student_list'),
    path('student-teachers',StudentTeachersView.as_view(),name='student_teachers')
]
