from rest_framework import serializers
from .models import ws, ExamDate, course, studentChoise, College


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


class collegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class wsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ws
        fields = '__all__'
