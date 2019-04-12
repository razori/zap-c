from django.shortcuts import render
from django.utils import timezone
from .forms import DayTasksForm
from .models import DayTasks

# Create your views here.
def main(request):
    date = timezone.now()
    title = "Главная страница"
    add_new_task = DayTasksForm(request.POST or None)
    if add_new_task.is_valid():
        add_new_task.save()
    task_list = DayTasks.objects.filter(date__exact=timezone.now()).order_by('id')
    context = {'date':date,'title':title,'new_task':add_new_task,
               'task_list':task_list}
    return render(request, "main.html", context)

def denis(request):
    date = timezone.now()
    title = "Задания Дениса"
    add_new_task = DayTasksForm(request.POST or None)
    if add_new_task.is_valid():
        add_new_task.save()
    task_list = DayTasks.objects.filter(date__exact=timezone.now(), employee='DENIS').order_by('id')
    context = {'date':date,'title':title,'new_task':add_new_task,
               'task_list':task_list}
    return render(request, "main.html", context)

def vladislav(request):
    date = timezone.now()
    title = "Задания Владислава"
    add_new_task = DayTasksForm(request.POST or None)
    if add_new_task.is_valid():
        add_new_task.save()
    task_list = DayTasks.objects.filter(date__exact=timezone.now(), employee='VLADISLAV').order_by('id')
    context = {'date':date,'title':title,'new_task':add_new_task,
               'task_list':task_list}
    return render(request, "main.html", context)
