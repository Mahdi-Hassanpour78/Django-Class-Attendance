from rest_framework import serializers
from .models import Semester, Class


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'name', 'start_date', 'end_date']


class ClassSemester(serializers.ModelSerializer):
    professor_username = serializers.ReadOnlyField(source='professor.username')


    class Meta:
        model = Class
        fields = ['id', 'name', 'code', 'start_date', 'end_date', 'professor', 'professor_username', 'semester', 'is_active']