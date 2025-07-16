from django import forms
from django.core .validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,11}$',
    message="Enter Phone Number in this format: +2348012345678"
)

class SignUpForm(forms.Form):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}),required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}), required=True)
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Enter Username"}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password','id':"password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'id':"password"}))
    phone = forms.CharField(validators=[phone_regex], max_length=15, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Password do not match")