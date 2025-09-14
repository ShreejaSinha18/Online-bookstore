from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import* 

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
def log(request):
    a=request.GET['ud']
    b=request.GET['pwd']
    c=request.GET['rpwd']
    if customer.objects.filter(uname=a,pwd=b,rpwd=c):
        return render(request,'shop.html')
    else:
        return render(request,'login.html')
        print('wrong userID or password!! please try again')

def signup(request):
    return render(request,'signup.html')
def sig(request):
    u=customer()
    u.uname=request.GET['ud']
    u.pwd=request.GET['pwd']
    u.rpwd=request.GET['rpwd']
    u.save()
    return render(request,'login.html')

def delete(request):
    u=customer.objects.all()
    return render(request,'delete_ac.html',{'a':u})
    
def dele(request,id):
    d=customer.objects.get(id=id)
    d.delete()
    return redirect('../delete')

def about(request):
    return render(request,'about.html')

def categories(request):
    return render(request,'categories.html')

def best(request):
    return render(request,'best_selling.html')

def authors(request):
    a=author.objects.all()
    return render(request,'author.html',{'t':a})
def disp(request):
    a=author.objects.all()
    return render(request,'author.html',{'t':a})
def au(request):
    a=author()
    a.name=request.GET['name']
    a.save()
    return redirect('../disp')
def delet(request,id):
    a=author.objects.get(id=id)
    a.delete()
    return redirect('../disp')

def shop(request):
    b=books.objects.all()
    return render(request,'shop.html',{'k':b})
def hop(request):
    b=books.objects.all()
    return render(request,'shop.html',{'k':b})
def boo(request):
    b=books()
    b.bname=request.GET['name']
    b.author=request.GET['auth']
    b.price=request.GET['cost']
    b.qty=request.GET['qty']
    b.save()
    return redirect('../hop')
def remove(request,id):
    b=books.objects.get(id=id)
    b.delete()
    return redirect('../hop')

def car(request):
    return render(request,'cart.html')

def buy(request):
    m=buyer()
    m.name=request.GET['name']
    m.email=request.GET['email']
    m.phone=request.GET['phone']
    m.date=request.GET['dop']
    m.mode=request.GET['a1']
    m.save()
    return render(request,'cart.html')

def admin(request):
    a=buyer.objects.all()
    return render(request,'admin.html',{'t':a})

def contact(request):
    return render(request,'contact_us.html')
