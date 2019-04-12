from django.db import models
from django.utils import timezone
from django.conf import settings

#клиент
class Client(models.Model):
	id = models.AutoField("ID", primary_key=True, blank = False)
	dateoflisted = models.DateField("Дата регистрации клиента",default=timezone.now, blank=False)
	name = models.CharField("Название или имя", max_length=50, blank=False)
	phone = models.CharField("Контакты", max_length=300, blank=False)
	adress = models.CharField("Адрес", max_length=300, blank=False)
	organisation = models.CharField("Физическое лицо или организация", max_length=20,
									  choices = ((PHYSIC,'физическое лицо'),(COMPANY,'компания'),(NOT_SELECTED,'неизвестно')),
									  default = NOT_SELECTED)
	commentary = models.CharField("Комментарий", max_length=300, blank=False)
	def publish(self):
		self.dateoflisted = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s %s %s %s' % (self.id, self.name,
									  self.phone, self.adress, self.organisation)
# сотрудник
class Employee(models.Model):
	id = models.AutoField(primary_key=True,blank=False)
	firstname = models.CharField("Имя",max_length=20,blank=False)
	middlename = models.CharField("Отчество",max_length=20,blank=False)
	lastname = models.CharField("Фамилия",max_length=20,blank=False)
	phone = models.CharField("Телефон",max_length=100,blank=False)
	function = models.CharField("Должность",choices=((COURIER,'курьер'),(MANAGER,'менеджер'),(ENGINEER, 'инженер')),blank=False)
	def __str__(self):
		return '%s %s %s' % (self.firstname, self.lastname, self.function)

# картридж
class Cartridge(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	code_name = models.CharField("Кодовое название",max_length=20, blank=False)
	simple_name = models.CharField("Бытовое название",max_length=200,blank=True)
	resourse = models.IntegerField()
	part = models.CharField("Тип",choices=((CART,'картридж'),(DRUM,'драм'),(TONER,'туба')))
	color = models.CharField("Цвет",choices=((CYAN,'cyan'),(MAGENTA,'magenta'),(YELLOW,'yellow'),(BLACK,'black')))
	def __str__(self):
		return '%s %s %s %s' % (self.code_name, self.simple_name, self.part, self.color)

# принтер
class Printer(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	name = models.CharField("Название", max_length=20, blank=False)
	compatibility = models.ManyToManyField(Cartridge)
	def __str__(self):
		return self.name

# заявка
class Task(models.Model):
	id = models.AutoField("ID", primary_key=True, blank = False, help_text="Уникальное ID для каждой задачи")
	process = models.CharField("Статус исполнения", max_length=15,
					choices = ((DONE, 'Выполнено'), (NOT_DONE, 'Не выполнено'),(FIRST_CONTACT, 'Первый контакт'),(ERROR,'Срыв процесса'))						   						(FIRST_CONTACT, 'Первый контакт')),
					default = FIRST_CONTACT, blank = False, help_text="Выполнено|Не выполнено|Первый контакт")
	client = models.ForeignKey(Client, models.PROTECT)
	date = models.DateField(default=timezone.now, blank=False) #~
	description = models.CharField("Описание", max_length=300, blank=False) #~
	working_time_1 = models.CharField("Рабочее время. С:",max_length=15, help_text="Со скольки")
	working_time_2 = models.CharField("Рабочее время. ДО:",max_length=15, help_text="До скольки") #~
	cashsumm = models.IntegerField("Сумма денег", help_text="Сумма денег которую надо получить от клиента, если оплата не по безналу") #~
	get_set = models.CharField("Отдать\забрать",
		max_length=7, choices = ((GET_, 'Забрать'),(SET_, 'Отдать'),(NO_,'Самовывоз')),
		default=NO_, help_text="Отдать клиенту, забрать у клиента либо ничего не делать") #~
	employee = models.CharField("Ответственный",
		max_length=10, choices = EMPLOYEE_SELECTOR,
		default=SERVICE, help_text="Исполнитель данной задачи. Курьер, либо работа не требует доставки") #~
	replace = models.CharField("Подменка", max_length=50, default = 'без подменки', help_text="Модель подменного картриджа, если он необходим") #~
	CASH = 'Нал'
	CASHLESS = 'Безнал'
	NO_MONEY = 'Без оплаты'
	PAYMENT_METHOD_SELECTOR = ((CASH, 'Нал'), (CASHLESS, 'Безнал'),
							   (NO_MONEY, 'Без оплаты'),)
	payment_method = models.CharField("Нал\Безнал", max_length=11,
									  choices = PAYMENT_METHOD_SELECTOR,
									  default = NO_MONEY, help_text="Метод оплаты. Наличный расчет, безналичный либо оплата не требуется") #~

	def publish(self):
		self.date = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s %s %s %s' % (self.id, self.date,
								   self.client, self.cashsumm,
								   self.employee)
