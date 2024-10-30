from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} - ({self.user_type})"
    

class TeacherStudent(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_students',limit_choices_to = {"user_type": "teacher"})
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_teachers',limit_choices_to = {"user_type": "student"})

    def __str__(self):
        return f"{self.teacher.username} - {self.student.username}"
    

class LoginLog(models.Model):
    user_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} ({self.user_type}) at {self.login_time}"