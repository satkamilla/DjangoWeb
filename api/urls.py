from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet, GetTasksView, EmployersViewSet, GetEmployersView

router = DefaultRouter()
router.register('tasks', TasksViewSet, )
router.register('employers', EmployersViewSet, )


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tasks/filtering', GetTasksView.as_view()),
    path('api/employers/filtering', GetEmployersView.as_view()),
]
