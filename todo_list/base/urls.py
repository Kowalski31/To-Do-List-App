from django.urls import path
from .views import index, UpdateTask

urlpatterns = [
    path('', index, name="tasks"),
    path('update_task/<str:pk>', UpdateTask, name="update_task"),

]