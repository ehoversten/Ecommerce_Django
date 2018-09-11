from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password	= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email 		= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password 	= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2	= forms.CharField(label='Retype Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs= User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username already exists")
		return username

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("password must match")
		return data
