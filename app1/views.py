from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import RDPRegistration
from .models import user_rdp
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
# from .forms import MyForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


#User Reistrarion Form

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'app1/signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('addandshow')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'app1/login.html')




# Create your views here.
def add_show(request):
    """This function will add item and show all items"""
    if request.method=="POST":
        fm=RDPRegistration(request.POST)
        if fm.is_valid():
            Emp_id=fm.cleaned_data['Emp_Id']
            ip_add=fm.cleaned_data['IP_Address']
            user_name=fm.cleaned_data['Username']
            passw=fm.cleaned_data['Password']
            sta=fm.cleaned_data['Status']
            regis=user_rdp(Emp_Id=Emp_id,IP_Address=ip_add,Username=user_name,Password=passw,Status=sta) #Stroring Data into database
            regis.save()
             
    else: 
        fm=RDPRegistration()
    stud=user_rdp.objects.all()
    return render(request,'app1/addandshow.html',{'form':fm,'stu':stud})

def LogoutPage(request):
    return render(request,'app1/logout.html')




def update_data(request,id):
    if request.method=='POST':
        pi=user_rdp.objects.get(pk=id)
        fm=RDPRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            
    else:
        pi=user_rdp.objects.get(pk=id)
        fm=RDPRegistration(instance=pi)
    return render(request,'app1/update.html',{"form":fm})
        

@csrf_exempt
def delete_item(request,id):
    if request.method=="POST":
        pi=user_rdp.objects.get(pk=id)
        pi.delete()
        return redirect('/')
        


