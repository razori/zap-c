from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Cartridge, Client, Printer, Employee

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id','process','client','date','description','working_time_1','working_time_2','cashsumm','get_set','employee','replace','payment_method')
