from rest_framework import serializers
from .models import Project,Message
from django.core.mail import send_mail
from django.conf import settings

class ProjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'





class MessageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields ='__all__'
    def create(self, validated_data):
        # Extracting necessary data
        name = validated_data.get('name')
        email = validated_data.get('email')
        message = validated_data.get('message')
        
        subject = "Message from Contact Form"
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.CONTACT_EMAIL]  # Assuming CONTACT_EMAIL is defined in settings.py
        send_mail(subject, message_body, from_email, recipient_list)


        # Create and return the Message instance
        return Message.objects.create(**validated_data)
