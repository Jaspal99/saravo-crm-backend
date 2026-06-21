from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        # return Todo.objects.filter(user=self.request.user)
        id_value = self.request.query_params.get("id")
        # return Todo.objects.filter(id=id_value)
        return Todo.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
class TodoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        # return Todo.objects.filter(user=self.request.user)
        id_value = self.request.query_params.get("id")
        return Todo.objects.filter(id=id_value)
    
class RootAPIView(APIView):
    def get(self,request):
        return Response({
            "list":reverse("list",request=request)
        })
