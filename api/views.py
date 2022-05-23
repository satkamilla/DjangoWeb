from rest_framework.viewsets import ModelViewSet
from .serializers import TasksSerializer, EmployersSerializer
from .models import Tasks, Employers
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q

class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class GetTasksView(ListAPIView):
    queryset = Tasks.objects.filter( Q(progress='Выполнено') | Q(progress='В процессе'))
    serializer_class = TasksSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['progress']


class EmployersViewSet(ModelViewSet):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer

class GetEmployersView(ListAPIView):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'salary']