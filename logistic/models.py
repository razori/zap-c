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
	#------
	PHYSIC = 'PH'
	COMPANY = 'CO'
	NOT_SELECTED = 'NO'
	#------
	organisation = models.CharField("Физическое лицо или организация", max_length=20,
									  choices = ((PHYSIC, 'физическое_лицо'),(COMPANY,'компания'),(NOT_SELECTED,'неизвестно')),
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
	#------
	COURIER = 'CO'
	MANAGER = 'MA'
	ENGINEER = 'EN'
	#------
	function = models.CharField("Должность",choices=((COURIER,'курьер'),(MANAGER,'менеджер'),(ENGINEER, 'инженер')), max_length=10, blank=False)
	def __str__(self):
		return '%s %s %s' % (self.firstname, self.lastname, self.function)

# картридж
class Cartridge(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	code_name = models.CharField("Кодовое название",max_length=20, blank=False)
	simple_name = models.CharField("Бытовое название",max_length=200,blank=True)
	resourse = models.IntegerField()
	#------
	CART = 'CART'
	DRUM = 'DRUM'
	TONER = 'TONER'
	#------
	part = models.CharField("Тип",choices=((CART,'картридж'),(DRUM,'драм'),(TONER,'туба')),max_length=10)
	#------
	CYAN = 'CYAN'
	MAGENTA = 'MAGENTA'
	YELLOW = 'YELLOW'
	BLACK = 'BLACK'
	#------
	color = models.CharField("Цвет",choices=((CYAN,'cyan'),(MAGENTA,'magenta'),(YELLOW,'yellow'),(BLACK,'black')),max_length=10)
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
	#------
	DONE = 'DONE'
	NOT_DONE = 'NOT_D'
	FIRST_CONTACT = 'FIRST'
	ERROR = 'ERROR'
	#------
	process = models.CharField("Статус исполнения", max_length=15,choices = ((DONE, 'Выполнено'), (NOT_DONE, 'Не выполнено'),(FIRST_CONTACT, 'Первый контакт'),(ERROR,'Срыв процесса')),
					default = FIRST_CONTACT, blank = False, help_text="Выполнено|Не выполнено|Первый контакт")
	client = models.ForeignKey(Client, models.PROTECT)
	date = models.DateField(default=timezone.now, blank=False) #~
	description = models.CharField("Описание", max_length=300, blank=False) #~
	working_time_1 = models.CharField("Рабочее время. С:",max_length=15, help_text="Со скольки")
	working_time_2 = models.CharField("Рабочее время. ДО:",max_length=15, help_text="До скольки") #~
	cashsumm = models.IntegerField("Сумма денег", help_text="Сумма денег которую надо получить от клиента, если оплата не по безналу") #~
	#------
	GET_ = 'GET'
	SET_ = 'SET'
	NO_ = 'NO'
	#------
	get_set = models.CharField("Отдать\забрать",
		max_length=7, choices = ((GET_, 'Забрать'),(SET_, 'Отдать'),(NO_,'Самовывоз')),
		default=NO_, help_text="Отдать клиенту, забрать у клиента либо ничего не делать") #~
	employee = models.ForeignKey(Employee, models.PROTECT) #~
	replace = models.ForeignKey(Cartridge, models.PROTECT)
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
class ServiceTask(models.Model):
	id = models.AutoField("ID",primary_key=True)
	task = models.ForeignKey(Task, models.PROTECT)
	cart = models.ForeignKey(Cartridge, models.PROTECT)
	date = models.DateField(default=timezone.now)
	opc = models.BooleanField('фотобарабан',default = False)
	pcr = models.BooleanField('ролик заряда',default = False)
	mag = models.BooleanField('магнит',default = False)
	doc = models.BooleanField('дозирующее',default = False)
	wip = models.BooleanField('ракель',default = False)
	chip = models.BooleanField('чип',default = False)
	fill = models.BooleanField('заправка',default = False)
	new = models.BooleanField('надо новый',default = False)
	trash = models.BooleanField('списать',default = False)
	comment = models.CharField('коментарий',default=' ',max_length=50,blank=True)
	close = models.BooleanField('финиш',default=False)
