from django.shortcuts import render

# Create your views here.from django.shortcuts import render,redirect
from .models import Courses
from .models import contactData,FeedbackData
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
import datetime as dt
data1=dt.datetime.now()

@login_required(login_url='login')
def homePage(request):
    return render(request,'homePage.html')

@login_required(login_url='login')
def contactPage(request):
    if request.method=='GET':
        data= contactData.objects.all()
        return render(request,'contactPage.html')
    else:
         contactData(
            frist_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            location= request.POST['location']
           ).save()
    return redirect(contactPage)

def servicePage(request):
    courses=Courses.objects.all()
    return render(request,'servicePage.html', {'courses':courses})

def feedbackPage(request):
    if request.method=='GET':
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})
    else
        FeedbackData(
        content=request.POST['feedback'],
        date=data1
        ).save()
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})


def galleryPage(request):
    return render(request,'galleryPage.html')


def loginPage(request):
    if request.method=='GET':
                return render(request,'loginpage.html')

       

    else:
        user=request.POST['user']
        password=request.POST['password']
        user=authenticate(username=user,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid details")

def  registerPage(request):
    if request.method=='GET':
        form =RegistrationForm()
        return render(request,'registerPage.html',{'form':form})

    else:
         form=RegistrationForm(request.POST)
         if form.is_valid():
             user=form.save(commit=False)
             user=user.set_password(user.password)
             form.save()
             return redirect('login')
         else:
             return HttpResponse('invalidform')

