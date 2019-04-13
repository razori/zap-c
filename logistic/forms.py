from django import forms
from .models import Task, Client, Printer, Cartridge, Employee
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput, RadioSelect

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['process', 'description', 'working_time_1', 'working_time_2',
		 		  'cashsumm', 'get_set', 'employee',
				  'replace', 'payment_method']
		widgets = {
			'process': RadioSelect(attrs={}),
			'description': Textarea(attrs={'cols':80, 'rows':10, 'placeholder':'Описание - например адрес','class':'textarea'}),
			'working_time_1': TextInput(attrs={'type':'time','min':'8:00','max':'19:00','class':'worktime'}),
			'working_time_2': TextInput(attrs={'type':'time','min':'8:00','max':'19:00','class':'worktime'}),
			'cashsumm': NumberInput(attrs={'min':'300','step':'50','placeholder':'300'}),
			'get_set': Select(attrs={}),
			'employee': Select(attrs={}),
			'replace': TextInput(attrs={}),
			'payment_method': Select(attrs={})
		}

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = [ 'name', 'phone', 'adress', 'organisation', 'commentary']

class PrinterForm(ModelForm):
	class Meta:
		model = Printer
		fields = ['name', 'compatibility']

class CartridgeForm(ModelForm):
	class Meta:
		model = Cartridge
		fields = ['code_name', 'simple_name', 'resourse', 'part', 'color']

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['firstname', 'middlename', 'lastname', 'phone', 'function']
