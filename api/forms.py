from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)
	# phone_number = PhoneNumberField(null=False, blank=False, unique=True)
	class Meta:
		model = Customer
		fields = ("name","email","password", "confirm_password")

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user