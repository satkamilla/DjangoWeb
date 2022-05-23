from rest_framework.serializers import ModelSerializer
from .models import Tasks, Employers


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class EmployersSerializer(ModelSerializer):
    class Meta:
        model = Employers
        fields = '__all__'