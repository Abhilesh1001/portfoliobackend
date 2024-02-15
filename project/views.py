from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Project
from .searilizer import ProjectSerilizer

# Create your views here.

def index(request):
    pro = Project.objects.all()
    print(pro)
    return HttpResponse('Portfolio backend')


class ProjcetView(APIView):
    def get_queryset(self):
        return Project.objects.all()

    def get(self, request, pk=None, format=None):
        pro = self.get_queryset()
        serilizer = ProjectSerilizer(pro,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
