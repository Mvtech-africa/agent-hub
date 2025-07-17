from django.shortcuts import render
from .forms import SignUpForm, SignInForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:sign-in')
        else:
            print(form.errors)  # show why it failed
    else:
        form = SignUpForm()
    return render(request, 'pages/sign-up.html', {'form': form})


    
def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('realtor:index'))
            else:
                return render(request, 'pages/sign-in.html', {
                    'message': 'Invalid credentials',
                    'signin_form': form
                })
    else:
        form = SignInForm()

    return render(request, 'pages/sign-in.html', {'signin_form': form})

def logout_view(request):
    logout(request)
    return render(request, 'pages/index.html',{
        'message':'logout'
    })
