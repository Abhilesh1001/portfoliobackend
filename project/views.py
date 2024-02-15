from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from . renderer import UserRenderer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .models import Project,Message
from .searilizer import ProjectSerilizer,MessageSerilizer
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def send_email_to(link,user):
    subject = "This email is for django PasswordReset from AbhleshCart"
    message = link
    from_email = settings.EMAIL_HOST_USER
    receipent_list = [user]
    send_mail(subject,message,from_email,receipent_list)

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
    

class MessageView(APIView):
    renderer_classes=[UserRenderer]
    authentication_classes = []
    permission_classes = [AllowAny] 
    def get_queryset(self):
        
        return Message.objects.all()
    
    def post(self,request,format=None):
        print(request.data)
        
        serilizer = MessageSerilizer(data=request.data)
        
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Message send Successfully'},status=status.HTTP_200_OK)
        
        return Response({'msg':'some error occured'},status=status.HTTP_400_BAD_REQUEST)
