from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.contrib.auth.models import User
from . models import MyUser
from django.contrib.auth import authenticate, login as log_in
from django.contrib.auth import logout
from . forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.
@login_required(login_url='/login')
def index(request):
	return render(request, 'index.html')

def login(request):
	if request.method == "GET":
		form = LoginForm()
		print("CHECCCCCCCCCCCCCCCCCCCCCCCK ANO")
		print(request.user)
		print("CHECCCCCCCCCCCCCCCCCCCCCCCK ANO")
		if request.user == 'AnonymousUser':
			return HttpResponseRedirect('/admin2')
		else: 
			return render(request, 'login.html', {'form':form})
	if request.method == "POST":
		print("xxxxxx")
		# form = LoginForm(request.POST)
		# print(form.is_valid())
		# if form.is_valid() :
		# 	form.login(request)
		# 	print(form.login(request.POST))
		# 	print(request.user)
		# 	return HttpResponseRedirect('/admin2')
		# print("fab")
		email = request.POST.get("email")
		password = request.POST.get("pass")
		user = authenticate(request,email=email, password = password)
		print("*****************************************")

		##########check############
		chckLogin = log_in(request, user)
		print(chckLogin)
		if user is not None:
			print(email + password)
			print(request.user)
			with connection.cursor() as cursor:
				sql_sa = cursor.execute("SELECT email, password, is_lock FROM [dbo].[Admin_myuser] where is_admin = 1").fetchall()
				Caches_BP = cache.set('BP_%s' % email, email)
				Caches_BP2 = cache.set('BP2_%s' % email, password)
				Caches_BP3 = cache.set('BP3_%s' % email, sql_sa[0][2])
			return HttpResponseRedirect('/admin2')
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# @login_required(login_url='/login')
def user(request):
	if request.method == "GET":
		ax = request.user
		print("---------------------------")
		print(ax)
		with connection.cursor() as cursor:
			SQL_SelectAllUser = cursor.execute("SELECT * from [dbo].[Admin_myuser]").fetchall()
			ListUser = [ list(x) for x in SQL_SelectAllUser]
			print('ListUser')
		# namecus = str(cache.get('BP_sylv@gmail.com'))
		# namecus2 = str(cache.get('BP2_sylv@gmail.com'))
		# namecus3 = str(cache.get('BP3_sylv@gmail.com'))
		# print(namecus + namecus2 + namecus3)
		# user = MyUser.objects.create_user('sylv@gmail.com', '123456')
		# user.gioi_tinh = 'nam'
		# user.is_lock =True
		# user.name = 'syle'
		# user.date_of_birth ='2006/07/07'
		# user.is_staff = 1
		# user.is_admin = 1
		# user.save()
		return render(request, 'user.html', {'listUser': ListUser})
	else:
		return HttpResponse("ZXs")
# def logout(request):
# 	return render(request, 'login.html')

def  register(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		userName = request.POST.get('firstName')
		print(authenticate(email = email, password = password))
		user = authenticate(email = email, password = password)
		chckLogin = log_in(request, user)
		print(chckLogin)
		if user is  not None:
			return HttpResponse("has exist")
		saveUser = MyUser.objects.create_user(email, password)
		saveUser.user_name = userName
		saveUser.save()
		return HttpResponseRedirect("/login")

	return render(request, 'register.html')