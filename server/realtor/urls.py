from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='realtor-index'),  # URL for the index view 
    
    # You can add more paths here for other views in the realtor app
    # path('another-view/', another_view, name='another-view'), 
    # path('property/<int:id>/', property_detail, name='property-detail'),
    # etc.  
]