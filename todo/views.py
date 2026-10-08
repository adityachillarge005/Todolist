from django.shortcuts import render
from .models import Todo
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Todos(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serailizer = TodoSerializer(data = request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer,status=status.HTTP_201_CREATED)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)

class TodosDetails(APIView):
    permission_classes =[IsAuthenticated]
    def get_todo(self,id):
        todo = get_object_or_404(Todo,id=id)
        return todo
    
    def get(self,request,id):
        todo  = self.get_todo(id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def put(self,request,id):
        todo = self.get_todo(id)
        serializer = TodoSerializer(todo,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        todo = self.get_todo(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    