from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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


def about(request):
    return render(request, 'about.html')

@login_required
def property_detail(request):
    """
    Render the property detail page for a specific property.
    """
    # Logic to retrieve property details by id would go here
    return render(request, 'properties.html')

@login_required
def upload_apartment(request):
    if request.method == 'POST':
        apartment = ""    
    return render(request, 'upload-apartment.html')

@login_required
def agent(request):
    return render(request, 'agents.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def view_property(request):
    
    return render (request, 'view_properties.html')  

  
def logout_view(request):
    logout(request)
    return render(request, 'index.html',{
        'message':'logout'
    })