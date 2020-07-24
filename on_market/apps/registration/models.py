from django.db import models

# Create your models here.
class Registration(models.Model):
	login = models.CharField('логин пользователя', max_length = 100)
	password = models.CharField('пароль пользователя', max_length = 100)
	e_mail = models.EmailField('пароль пользователя', max_length = 50)

	def __str__(self):
		return self.login

	def return_log_passw_mail(self):
		return self.login, self.password, self.e_mail