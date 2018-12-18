from rest_framework import serializers
from .models import Student,LANGUAGE_CHOICES,STYLE_CHOICES




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
