from django.urls import path
from . import views

app_name = 'realtor'
urlpatterns = [
    path('', views.index, name='realtor-index'),  # URL for the index view 
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'), 
    path('property', views.property_detail, name='property-detail'),  # URL for property detail view
    path('agent', views.agent, name='agent' )
]