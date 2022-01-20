from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Studentmodel
from . serializers import studentserializer
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request): # when pk is in url student_api(request,pk=None)
    if request.method == 'GET':
       id = request.data.get('id') #id=pk when in url <int:pk>
       if id is not None:
           stu = Studentmodel.objects.get(id=id)
           serializer = studentserializer(stu)
           return Response(serializer.data)

       stu = Studentmodel.objects.all()
       serializer = studentserializer(stu,many=True)
       return Response(serializer.data)

    if request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id =request.data.get('id') #id=pk when in url <int:pk>
        stu = Studentmodel.objects.get(pk=id)
        serializer = studentserializer(stu, data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = request.data.get('id') #id=pk when in url <int:pk> remove partial=True
        stu = Studentmodel.objects.get(pk=id)
        serializer = studentserializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = request.data.get('id') #id=pk when in url <int:pk>
        stu = Studentmodel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Delete'},status=status.HTTP_202_ACCEPTED)
