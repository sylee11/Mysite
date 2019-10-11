from django import forms
from . models import MyUser
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
	email = forms.EmailField(max_length = 30)
	password = forms.CharField(widget=forms.PasswordInput())

	def Clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		user = authenticate(email=email, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Email hoặc mật khẩu không chính xác. Please try again.")
		return self.cleaned_data
	def login(self, request):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		print(email + password)
		user = authenticate(request,email=email, password=password)
		return user