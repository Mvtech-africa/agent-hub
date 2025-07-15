from django.shortcuts import render

# Create your views here.
def index (request):
    """
    Render the index page for the realtor app.
    """
    return render(request, 'index.html')

def sign_up(request):

    return render(request, 'sign-up.html')

def sign_in(request):
    return render (request, 'sign-in.html')

def upload(request):
    return render(request, 'upload.html')