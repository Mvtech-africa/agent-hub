from django.urls import path
from . import views
from user import views as user_views

app_name = 'realtor'
urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view 
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'), 
    path('properties', views.property_detail, name='property-detail'),  # URL for property detail view
    path('agent', views.agent, name='agent' ),
    path('sign-up', user_views.sign_up, name='sign-up'),
    path('sign-in', user_views.sign_in, name='sign-in'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('upload-apartment', views.upload_apartment, name='upload-apartment')
]