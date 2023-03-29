from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.

def homePage(request):
    return HttpResponse('<h1>Home Page - KBTU</h1>')


# class TodoListApiView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class TodoListApiView(APIView):
    def get(self, request):
        tasks = Todo.objects.all().values()
        return Response({'tasks': list(tasks)})

    def post(self, request):
        newTodo = Todo.objects.create(
            task=request.data['task'],
            completed=request.data['completed'],
            purpose_id=request.data['purpose_id'],
        )

        return Response({'new Todo': model_to_dict(newTodo)})
