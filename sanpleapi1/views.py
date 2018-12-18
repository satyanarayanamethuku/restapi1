from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from  rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_list_or_404
from rest_framework .response import Response
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
class studentList(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field ='id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
           return self.list(request)

    def put(self, request, id=None):
        return self.update(request,id)
    def post(self,request):
        return self.create(request)

    def delete(self, request,id=None):
        return self.destroy(request,id)

"""class studentList(APIView)

    def get(self,request):
        student1=Student.objects.all()
        serializer=StudentSerializer(student1,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)



    def put(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)"""



"""def get(self,request):
     student1=Students.objects.all()
      serializer=StudentSerializer(student1,many=True)
      return Response(serializer.data)
    def post(self,request):
     serializer=StudentSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data,status=status.HTTP_400_BAD_REQUSt)  """
"""def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)"""
"""class studentList(generic.ListCreateAPIView):
 queryset=Students.objects.all()
 serializer_class=StudentSerializer
 class StudentDetail(generic.RetrieveUpdateDestroyAPIView):
     queryset=Student.objects.all()
      serializer_class=StudentSerializer"""
