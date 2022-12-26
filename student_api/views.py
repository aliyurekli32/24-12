from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet 

#?my imports
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer




#!!!!!!!!!!!!!!!!!!!!!!!!!      FUNCTION BASED VİEWS       !!!!!!!!!!!!!!!!!
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
def student_detail(request, pk):
    student = get_object_or_404(Student, id=pk)
    # student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)
@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student,data=request.data) 
    if serializer.is_valid():
        serializer.save()
        message={
            "message": f'Student succesfully updated...'
        }
        return Response(serializer.data, status=status.HTTP_200_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message={
        "message":"Student succesfully deleted..."
    }
    return Response(message)


@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)
    
    
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!      CLAS BASED VİEWS       !!!!!!!!!!!!!!!!!
    
 #!API view
 
# class StudentListCreate(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {serializer.} updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(APIView):
#     def get_obj(self, pk):
#         return get_object_or_404(Student, id=pk)
#     def get(self, request, pk):
#         student = self.get_obj(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         student

#! GENERICAPIView
class StudentGAV(mixins.ListModelMixin,mixins.CreateModelMixin, GenericAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentDetailGAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, GenericAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
#!CoNCRETE VIEWS

class StudentCV(ListCreateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    
#! ViewSets

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer