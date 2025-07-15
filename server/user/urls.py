from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.sign_up, name='sign-up'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('agent-signup',  views.agent_sign_up, name='agent-signup')
]