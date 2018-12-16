from django import forms

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

