from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import edit

from .models import product, cartitem ,address ,order


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def singlepost(request):
    return render(request,'singlepost.html')

def shop(request):
    return render(request,'shop.html')


def style(request):
    return render(request,'style.html')

def products(request):
   d = product.objects.all()
   if request.method == 'POST':
      productname = request.POST['productname']
      print(productname)

      price = request.POST['price']
      print(price)

      image=request.FILES['image']
      print(image)

      qty = request.POST['qty']
      print(qty)

      f = product.objects.create(productname=productname, price=price, image=image,qty=qty)
      f.save()
   return render(request, 'product.html', {'e': d})


def viewproduct(request):
   x = product.objects.all()
   return render(request, 'edit.html', {'y': x})

def productedit (request,id):
    a=product.objects.get(id=id)
    if request.method =='POST':
        a.productname=request.POST['productname']
        a.price=request.POST['price']
        a.image=request.FILES['image']
        a.qty=request.POST['qty']
        a.save()
        return redirect('viewproduct')
    return render(request,'editproduct.html',{'b':a})

def productdelete(request, id):
   a = product.objects.get(id=id)
   a.delete()
   return redirect('products')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)

        email = request.POST['email']
        print(email)

        phonenumber = request.POST['phonenumber']
        print(phonenumber)

        dob = request.POST['dob']
        print(dob)

        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        username = request.POST['email']
        user = User.objects.create_user(username, password ,confirmpassword)
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def loginpage(request):
    if request.method =='POST':
        userid=request.POST['email']
        print(userid)

        password=request.POST['password']
        print(password)

        user=authenticate(username=userid,password=password)
        if user is not None:
            login(request, user)
            print('login')

        else:
            print('invalid')
        return redirect('index')
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return render(request,'login.html')

def items(request,id):
    f = product.objects.get(id=id)
    if request.method == 'POST':

        z = cartitem.objects.create(products=f, price=f.price, image=f.image, quantity=1 , user=request.user)
        z.save()

    return render(request, 'items.html', {'o': f})

# Create your views here.

def cart(request):
   d = cartitem.objects.all()
   return render(request, 'cart.html', {'z': d})

def viewcart(request):
   x = cartitem.objects.filter(user=request.user )
   return render(request, 'cart.html', {'y': x})

def cartdelete(request, id):
   e = cartitem.objects.get(id=id)
   e.delete()
   return redirect('cart')

def addres(request):
    j = cartitem.objects.all()
    if request.method == 'POST':

        House_no = request.POST['House_no']
        print(House_no)

        area = request.POST['area']
        print(area)

        pincode = request.POST['pincode']
        print(pincode)

        city = request.POST['city']
        print(city)

        state = request.POST['state']
        print(state)

        contactno = request.POST['contactno']
        print(contactno)

        p = address.objects.create(user=request.user ,  House_no=House_no, area=area, pincode=pincode, city=city ,state = state , contactno=contactno)
        p.save()
        return redirect('buynow')
    return render(request,'addresss.html',{'l': j })


def buynow(request):
    g = cartitem.objects.filter(user=request.user )
    k=address.objects.filter(user=request.user )
    return render(request, 'buynow.html', {'u': g ,'h':k})

def addredit(request):
    n=address.objects.get(user=request.user )
    if request.method=='POST':
        n.House_no =request.POST['House_no']
        n.area = request.POST['area']
        n.pincode = request.POST['pincode']
        n.city = request.POST['city']
        n.state =request.POST['state']
        n.contactno =  request.POST['contactno']
        return redirect('buynow')
    return render(request , 'addredit.html',{'r':n})


def addrdelete(request):
   e = address.objects.all()
   e.delete()
   return redirect('buynow')

def orders(request):
    o = address.objects.get(user=request.user)
    print(o)
    u = cartitem.objects.filter(user=request.user)
    for i in u:
        l=order.objects.create(user=request.user, address=o, product=i.products, price=i.price, quantity=i.quantity)
        l.save()
    u.delete()
    return redirect('buynow')




