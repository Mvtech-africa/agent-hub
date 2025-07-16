from django.shortcuts import render
from . import forms

# Create your views here.

def sign_up(request):
    return render(request, 'pages/sign-up.html',{
        'signup_form': forms.SignUpForm()
    })

def sign_in(request):
    return render(request, 'pages/sign-in.html',{
        'signin_form': forms.SignUpForm()
    })
