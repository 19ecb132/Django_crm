from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import record

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),label="",required=True)
    last_name = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),label="",required=True)
    email = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'Email','class':'form-control'}),label="",required=True)
    phone = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'Phone number','class':'form-control'}),label="",required=True)
    address = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'Address','class':'form-control'}),label="",required=True)
    state = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'State','class':'form-control'}),label="",required=True)
    city = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'City','class':'form-control'}),label="",required=True)
    pincode = forms.CharField(max_length=200,widget=forms.widgets.TextInput(attrs={'placeholder':'Pincode','class':'form-control'}),label="",required=True)

    class Meta:
        model = record
        exclude = ('user',)

        

