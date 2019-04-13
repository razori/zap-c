from django.shortcuts import render
from django.utils import timezone
from .forms import TaskForm, CartridgeForm, ClientForm, PrinterForm, EmployeeForm
from .models import Task, Cartridge, Client, Printer, Employee
from .serializers import TaskSerializer
from rest_framework import viewsets

# Create your views here.
def main(request):
    date = timezone.now()
    title = "Главная страница"
    form_task = TaskForm(request.POST or None)
    if form_task.is_valid():
        form_task.save()
    form_client = ClientForm(request.POST or None)
    if form_client.is_valid():
        form_client.save()
    task_list = Task.objects.filter(date__exact=timezone.now()).order_by('id')
    context = {'date':date,'title':title,'form_task':form_task,'form_client':form_client,
               'task_list':task_list}
    return render(request, "main.html", context)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
