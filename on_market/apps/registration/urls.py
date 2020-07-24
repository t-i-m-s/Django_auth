from django.urls import path
from . import views


app_name = 'registration'
urlpatterns = [
	path('', views.show_form),
	path('success/', views.leave_form, name = 'leave_form')
]