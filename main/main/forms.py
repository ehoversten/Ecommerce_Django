from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class ContactForm(forms.Form):
	fullname  = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={"class":"form-control"}))
	email	  = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"form-control"}))
	content	  = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Tell us how we can help ..."}))

	# define better email validation !*!*!*!*!
	def clean_email(self):
		email= self.cleaned_data.get("email")
		if not ".com" in email:
			raise forms.ValidationError("Must be valid email")
			return email

class LoginForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password	= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email 		= forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password 	= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2	= forms.CharField(label='Comfirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))


	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs       = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs       = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		return email

	def clean(self):
		data      = self.cleaned_data
		password  = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')

		if password2 != password:
			raise forms.ValidationError("Passwords must match")
		return data
