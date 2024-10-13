from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),

    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>', views.project_detail, name='project_detail'),
    path('create_project/', views.create_project, name='create_project'),
    path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),

    path('task/', views.task, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('toggle_task_done/<int:task_id>', views.toggle_task_done, name='toggle_task_done'),
]
