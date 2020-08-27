from django.shortcuts import render,redirect
from capture .models import categories,photos,contactus,adminuser

# Create your views here.
def admin(request):

    c = photos.objects.all()
    cat=categories.objects.all()
    if request.session.has_key('id'):
        return render(request, 'admin.html', {'c' : c , 'cat' : cat})
    else:
        return redirect(login)

   

    
     
    return render(request, 'admin.html', {'c' : c , 'cat' : cat})

def add(request):
    if request.method == 'POST':

        name= request.POST.get('name')
        img=request.POST.get('img')
        image ='pics/' + img
        category_id = request.POST.get('category')
        category = categories.objects.get(id=category_id)
        photos.objects.create(
            name=name,
            img=image,  
            category=category
        )
        return redirect(admin)

        return render(request, 'admin.html' , {'cat':categories.objects.all(), 'msg':'photo added'})
        
       

     
               

    else:
        print("error")
            

           
def delete_photo(request):
     if request.method == 'POST':

        delete_id= request.POST.get('delete_id')
        delete_photo= photos.objects.get(id=delete_id)
        delete_photo.delete()
        return redirect(admin)

     return render(request, 'admin.html')
           

def addcat(request):

    if request.method == 'POST':


        name= request.POST.get('name')
        categories.objects.create(
            name=name
        )
        return redirect(admin)


    return render(request, 'admin.html')




           
def delete_cat(request):
     if request.method == 'POST':

        delete_catid= request.POST.get('delete_catid')
        delete_cat= categories.objects.get(id=delete_catid)
        delete_cat.delete()
        return redirect(addcategory)

     return render(request, 'admin.html')


def addcategory(request):
     cat=categories.objects.all()

     return render(request, 'addcategory.html', {'cat':cat})



def contactme(request):
     con=contactus.objects.all()

     return render(request, 'show_contact.html', {'con':con})

          
def delete_con(request):
     if request.method == 'POST':

        delete_conid= request.POST.get('delete_conid')
        delete_con= contactus.objects.get(id=delete_conid)
        delete_con.delete()
        return redirect(contactme)

     return render(request, 'show_contact.html')





def login_form(request):

    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('pass')

        if adminuser.objects.filter(username=username , password=password).exists():
            request.session['id']=username
            return render(request,'admin.html')
        else:
            return redirect(login)
        

    return render(request, 'login.html')


def login(request):
    
    return render(request,'login.html')

def logout(request):

    if request.method == 'POST':
        request.session.flush()
    return render(request, 'login.html')