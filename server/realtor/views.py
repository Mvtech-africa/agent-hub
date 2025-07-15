from django.shortcuts import render

# Create your views here.
def index (request):
    """
    Render the index page for the realtor app.
    """
    return render(request, 'index.html')

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