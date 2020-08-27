from django.urls import path
from .import views
urlpatterns = [
    path('',views.index , name='index'),
    path('gallery/', views.gallery, name='gallery'),
    
    path('contact/', views.contact, name='contact'),
    path('contactform/', views.contactform, name='contactform'),
    path('select_cat/',views.select_cat, name='select_cat'),
 
    
]
