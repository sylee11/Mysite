from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index'),
	url(r'^admin2/$', views.user, name ='table'),
	url(r'^login/$', views.login, name ='login'),
	url(r'^register/$', views.register, name ='register'),
	url(r'^test/$', views.testDataTable, name ='test'),
	# path('/logout', views.logout, name ='logout')
	url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

]