from django.http import HttpResponse
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.urls import reverse
from .models import Post, CountryData
from .form import Detailsform, CreateUserForm, CountryDataForm, finddisease
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def basic(request):
    
    return render(request, 'basic.html')



def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})

def create(request):
    if request.method == "POST":
        # title = request.POST.get('title')
        # body = request.POST.get('body')
        # creates = Post(title=title, body=body)
        # creates.save()
        form = Detailsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog posted successfully!")
            return HttpResponseRedirect("/index")
    else:
        form = Detailsform()

    return render(request,'create.html',{'form':form})
    

def delete(request,pk):
    posts = Post.objects.get(id=pk)
    posts.delete()
    messages.success(request, "Blog deleted successfully!")
    return HttpResponseRedirect("/index")
    
    

def update(request, pk):
    item = Post.objects.get(id=pk)
    context = {item.title:'title', item.body:'body'}
    form = Detailsform(request.POST, instance=item)
    if form.is_valid():
        form.save()
        item = Post.objects.all()
        return HttpResponseRedirect("/index")

    return render(request,'update.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfully!")
            return redirect('loginpage')
        
    context = {'form':form}
    return render(request, 'register.html',context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate( username = username, password = password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/loginpage')


def home(request):
    if request.method == 'POST' :
        form1 = CountryDataForm(request.POST)
        if form1.is_valid():
            form1.save()
        
    else:
        form1 = CountryDataForm()

    return render(request, 'add.html',{'form1': form1})

def see(request):
    if request.method == 'POST' :
        form2 = finddisease(request.POST)
        disease = request.POST.get('disease')
        print(disease)
        data = CountryData.objects.filter(disease = disease).values()
    else:
        form2 = finddisease()
    return render(request, 'home.html',{'form2': form2},{'data':data})
