from django import forms
from .models import DayTasks, Client
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput, RadioSelect

class DayTasksForm(ModelForm):
	class Meta:
		model = DayTasks
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
