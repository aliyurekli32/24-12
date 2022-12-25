from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view() # default GET
def home(request):
    return Response({'home':'This is api page..'})

#http methods ---------------->
#--GET (DB den veri çağırma, public)
#--POST (DB de değişiklik, create, private)
#--PUT (DB de kayıt değişiklik, update, private)
#--DELETE (DB de Silme, delete, private)
#--PATCH (DB de kısmi kayıt değişiklik, update, private)

@api_view(['GET'])
def students_list(request):
     students=Student.objects.all()
     #! print(students)
     serializer = StudentSerializer(students, many=True)
     #! print(serializer.data)
     return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "message": f'Student updated succesfully...'
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_detail(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)    