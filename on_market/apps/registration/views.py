from django.http import HttpResponse
from django.shortcuts import render
from .models import Registration
#from django.core.mail import send_mail

# Create your views here.
def check_form(request):

	users_datas = Registration.objects.filter(login__startswith = request.POST['login'])
	for user in users_datas:
		if user.return_log_passw_mail()[0] == request.POST['login']:
			if user.return_log_passw_mail()[1] == request.POST['password']:
				return render(request, 'autorised_page.html', {'login': request.POST['login']})
			else:
				return HttpResponse("Неверный пароль(")
			
	return render(request, 'isnt_registrated_page.html')
	

def leave_form(request):

	user_data = Registration(login = request.POST['login'], password = request.POST['password'], e_mail = request.POST['e_mail'])#request.POST.get('e_mail', False)
	user_data.save()

	#send_mail('My-market.net', 'Вы успешно зарегистрировались в my-market.net!', 'black_tank2000@mail.ru',
    #[request.POST['e_mail']], fail_silently=False)

	return HttpResponse("Успешная регистрация!!!")


def show_form(request):

	return render(request, 'registration_page.html')