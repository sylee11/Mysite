from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from django.db import connection
from django.contrib.auth.models import User
from . models import MyUser
# Create your views here.

def index(request):
	return render(request, 'index.html')
def table(request):
	return render(request, 'user.html')


def user(request):
	if request.method == "GET":
		with connection.cursor() as cursor:
			SQL_SelectAllUser = cursor.execute("SELECT * from [dbo].[Admin_myuser]").fetchall()
			ListUser = [ list(x) for x in SQL_SelectAllUser]
			print('ListUser')
		user = MyUser.objects.create_user('sylv@gmail.com', '123456')
		# user.gioi_tinh = 'nam'
		# user.lock =True
		# user.name = 'syle'
		# user.date_of_birth ='2006/07/07'
		# user.is_staff = 1
		# user.is_admin = 1
		user.save()
		return render(request, 'user.html', {'listUser': ListUser})
	else:
		return HttpResponse("ZX")