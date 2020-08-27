from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('login_form/',views.login_form, name='login_form'),  
    path('myadmin/',views.admin , name='admin'),
    path('addcategory/',views.addcategory , name='addcategory'),
    path('add/',views.add , name='add'),
    path('addcat/',views.addcat , name='addcat'),
    path('delete_cat/',views.delete_cat , name='delete_cat'),
    path('delete_photo/', views.delete_photo , name='delete_photo'),
    path('contactme/',views.contactme , name='contactme'),
    path('delete_con/',views.delete_con , name='delete_con'),
]
