import django_filters
from .models import *

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'description', 'complete', 'create' ]