from django.urls import path
from .views import project_create, project_delete, project_detail, project_list, task_delete, task_detail, task_list, task_create

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('tasks/<int:task_id>/delete/', task_delete, name='task_delete'),
    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/', task_list, name='task_list_by_project'),
    path('projects/<int:project_id>/delete/', project_delete, name='project_delete'),
]
