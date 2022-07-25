from django.urls import path
from .views import index, UpdateTask, DeleteTask

urlpatterns = [
    path('', index, name="tasks"),
    path('update_task/<str:pk>', UpdateTask, name="update_task"),
    path('delete_task/<str:pk>', DeleteTask, name="delete_task"),

]