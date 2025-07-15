from django.shortcuts import render

# Create your views here.

def sign_up(request):
    return render(request, 'pages/sign-up.html')

def sign_in(request):
    return render(request, 'pages/sign-in.html')

def agent_sign_up(request):
    return render(request, 'pages/agent-signup.html')