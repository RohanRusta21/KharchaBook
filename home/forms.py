from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Expense, Profile

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class AddExpenseForm(forms.ModelForm):
	id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Expense

		fields = ['name', 'amount', 'date','id']
		widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
				
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['income']
