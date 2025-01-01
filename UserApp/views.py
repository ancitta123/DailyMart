from django.shortcuts import render,redirect
from AdminApp.models import*
from.models import*
from django.db.models.aggregates import Sum

# Create your views here.

def userindex(request):
    data=Category.objects.all()
    new=Product.objects.all()
    return render(request,'userindex.html',{'data':data ,'new':new})

    return render(request,'userindex.html')

def categorycard(request):
    data=Category.objects.all()
    return render(request,'categorycard.html', {'data':data})

def productcard(request,cat):
    if cat=='all':
        data=Product.objects.all()
    else:
        data=Product.objects.filter(category=cat)
    return render(request,'productcard.html',{'data':data})

def singleproduct(request, id):
        data=Product.objects.filter(id=id)
        return render(request,'singleproduct.html', {'data':data})
 
def home(request):
    data=Category.objects.all()
    new=Product.objects.all()
    return render(request,'home.html',{'data':data ,'new':new})

def contact(request):
    return render(request,'contact.html')

def contactdata(request):
    if request.method=='POST':
        name=request.POST['name']   
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        data=Contact(name=name,email=email,phone=phone,message=message)
        data.save()
    return redirect('contact')

def abouts(request):
    return render(request,'abouts.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password']
        email=request.POST['email']
        mobile=request.POST['mobile']
        data= Register(username=username,password=password,email=email,mobile=mobile)
        data.save()
    return redirect('register')

def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(username=username,password=password).exists():
           data = Register.objects.filter(username=username,password=password).values('id','mobile','email').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['mobile'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('home') 
        else:
            return render(request,'login.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('home')

def userlogout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

def cart(request):
    user_id=request.session.get('u_id')
    data=Cart.objects.filter(usercart=user_id,status=0)
    a=Cart.objects.filter(usercart=user_id,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'a':a})

def addtocart(request,id):  
    if request.method == "POST":
        user_id=request.session.get('u_id')
        quantity=request.POST.get('quantity')
        total=request.POST.get('total')
        data=Cart(usercart=Register.objects.get(id=user_id),userpro=Product.objects.get(id=id),quantity=quantity,total=total)
        data.save()
    return redirect('cart')

def deletecart(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')

def checkout(request):
    user_id=request.session.get('u_id')
    data=Cart.objects.filter(usercart=user_id,status=0)
    a=Cart.objects.filter(usercart=user_id,status=0).aggregate(Sum('total'))
    return render(request,'checkout.html',{'data':data,'a':a})

def checkoutdata(request):
    if request.method == "POST":
        checkoutid=request.session.get('u_id')
        address=request.POST.get('address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        data=Cart.objects.filter(usercart=checkoutid,status=0)

        for i in data:
            data = Checkout(usercheckout=Register.objects.get(id = checkoutid),usercart = Cart.objects.get(id=i.id),address = address,country = country,state=state,pincode=pincode)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('checkout')

def success(request):
    user_id=request.session.get('u_id')
    data=Checkout.objects.filter(usercheckout=user_id)
    return render(request,'success.html',{'data':data})