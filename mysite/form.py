from django import forms

class UserForm(forms.Form):
    num1=forms.CharField(label="Value 1",widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2=forms.CharField(label="Value 2",widget=forms.TextInput(attrs={'class': 'form-control'}))
    ans=forms.CharField(label="Output",disabled=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control'}))