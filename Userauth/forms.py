from django import forms
from django.contrib.auth.models import User

class Register(forms.Form):
	first_name = forms.CharField(max_length=100,label='first_name',required=False,help_text='optional')
	last_name = forms.CharField(max_length=100,label='last_name',required=False,help_text='optional')
	username = forms.CharField(max_length=100,label='username',required=True)
	password1 = forms.CharField(max_length=20,label='password1',required=True,widget=forms.PasswordInput)
	password2 = forms.CharField(max_length=20,label='password2',required=True,widget=forms.PasswordInput)
	email_id = forms.CharField(label='email',max_length=50,required=True)
	

	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2','email_id')

		def clean_username(self):
			user = self.cleaned_data.get('username').lower()
			check = User.objects.filter(username=user)
			if check.count()>0:
				raise forms.ValidationError('choose a different username')
			else:
				return user

		def clean_password2(self):
			user = self.cleaned_data.get('password1')
			user = self.cleaned_data.get('password2')
			if password1 != password2 :
				raise forms.ValidationError('enter the same password')
			if not(password1) and not(password2):
				raise forms.ValidationError('please enter the passwords')
			if len(password1)<8:
				raise forms.ValidationError('password should be atleast 8 characters')
				return True

		def clean_email_id(self):
			email = self.cleaned_data.get('email')
			check = User.objects.filter(email=email)
			if check.count()>0:
				raise forms.ValidationError('email already exists')
			return email;

		def save(self):
			user = User.objects.create_user(
				username=self.cleaned_data.get('username'),
				password=self.cleaned_data.get('password1'),
				email=self.cleaned_data.get('email'),
				first_name=self.cleaned_data.get('first_name'),
				last_name=self.cleaned_data.get('last_name'),
				

				)








