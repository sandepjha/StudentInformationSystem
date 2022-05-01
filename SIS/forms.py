from .models import User
from django import forms

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=True,attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['name','email','password']