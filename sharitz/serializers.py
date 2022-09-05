from rest_framework import serializers
from .models import WeeklySchedule, ExamDate, course, studentChoise


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


# class studentChoiseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = studentChoise
#         fields = '__all__'
