from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from django.contrib.auth import logout

# Create your views here.
def index (request):
    """
    Render the index page for the realtor app.
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('realtor:property-detail'))
    return render(request, 'index.html',{
        'forms': forms.ContactForm(),
        'user': request.user.is_authenticated
    })


def upload(request):
    return render(request, 'upload.html')

def about(request):
    return render(request, 'about.html')

def property_detail(request):
    """
    Render the property detail page for a specific property.
    """
    # Logic to retrieve property details by id would go here
    return render(request, 'properties.html')



def agent(request):
    
    return render(request, 'agents.html')

def profile(request):
    return render(request, 'profile.html')
    
def logout_view(request):
    logout(request)
    return render(request, 'index.html',{
        'message':'logout'
    })