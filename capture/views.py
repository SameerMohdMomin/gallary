from django.shortcuts import render,redirect
from .models import categories,photos,contactus
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def index(request):

    c = photos.objects.all()

    return render(request , 'index.html' , {'c':c})

def gallery(request):
    cat=categories.objects.all()
    return render(request, 'gallery.html',{'cat':cat})

def select_cat(request):

    cat=categories.objects.all()

    if request.method == 'POST':

        filter1= request.POST.get('selected_cat')
        category1=photos.objects.filter(category_id=filter1)
    return render(request , 'gallery.html' , {'category1':category1 , 'cat': cat })



def contact(request):
    return render(request,'contact.html')



def contactform(request):
    if request.method == 'POST':

        name= request.POST.get('name')
        msg=request.POST.get('msg')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        contactus.objects.create(
            name=name,
            email=email,
            subject=subject,
            msg=msg
        )
        return redirect(contact)


    return render(request, 'contact.html')

