from django.urls import path, include
from .views import index, sign_in, sign_up, upload

urlpatterns = [
    path('', index, name='realtor-index'),  # URL for the index view 
    path('sign-up', sign_up, name='sign-up'),
    path('sign-in', sign_in, name='sign-in'),
    path('upload', upload, name='upload')
    # You can add more paths here for other views in the realtor app
    # path('another-view/', another_view, name='another-view'), 
    # path('property/<int:id>/', property_detail, name='property-detail'),
    # etc.  
]