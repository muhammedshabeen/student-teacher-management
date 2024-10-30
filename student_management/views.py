from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, TeacherStudentSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from .models import LoginLog, User
from django.db import transaction


class TeacherStudentRegister(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Login(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                LoginLog.objects.create(user_name=user.username, user_type=user.user_type)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key, "message": "Login successful!"})
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Student(APIView):
    def get(self,request):
        students = User.objects.filter(user_type='student')
        student_list = [{"id": student.id, "username": student.username} for student in students]
        return Response({"students": student_list}, status=status.HTTP_200_OK)
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            new_user = User(username=username, user_type='student')
            new_user.set_password(password)
            new_user.save()
        return Response({"message": "Student added successfully!"}, status=status.HTTP_201_CREATED)
    
    
    def put(self, request):
        student_id = request.data.get("student_id")
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not student_id or not isinstance(student_id, int):
            return Response({"error": "A valid student ID must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = User.objects.get(id=student_id, user_type='student')
        except User.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        if username:
            student.username = username
        
        if password:
            student.set_password(password)
        
        student.save()

        return Response({"message": "Student updated successfully!"}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        student_id = request.data.get("student_id")
        
        if not student_id or not isinstance(student_id, int):
            return Response({"error": "A valid student ID must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.get(id=student_id, user_type='student').delete()
        except User.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Student deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
    

class StudentTeachersView(APIView):

    def get(self, request):
        student_id = request.data.get('student_id')
        if student_id:
            try:
                student = User.objects.prefetch_related('student_teachers__teacher').get(id=student_id, user_type='student')
                teacher_list = [{'id': ts.teacher.id, 'username': ts.teacher.username} for ts in student.student_teachers.all()]

                return Response({'teachers': teacher_list}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Student id required"}, status=status.HTTP_404_NOT_FOUND)
    



    

    