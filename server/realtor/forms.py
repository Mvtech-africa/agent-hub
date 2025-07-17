from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Enter Your Name",'id':"name"}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email','id':"name"}), required=True)
    message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'placeholder':'Enter Your Message'}), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not email.endswith('@example.com'):
            
            raise forms.ValidationError("Email must be from the domain 'example.com'")
        return email