from django.shortcuts import render,redirect
from.models import*
from UserApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def adminindex(request):
    category=Category.objects.all().count
    product=Product.objects.all().count
    contact=Contact.objects.all().count
    register=Register.objects.all().count
    order=Checkout.objects.all().count
    return render(request,'adminindex.html',{'category':category,'product':product,'contact':contact,'register':register,'order':order})

def addcategory(request):
    return render(request,'addcategory.html')

def categorydata(request):
    if request.method=='POST':
        name=request.POST['name']   
        image=request.FILES['image']
        data=Category(name=name,image=image)
        data.save()
    return redirect('addcategory')

def viewcategory(request):
    data=Category.objects.all()
    return render(request,'viewcategory.html' ,{'data':data})

def addproduct(request):
    data=Category.objects.all()
    return render(request,'addproduct.html',{'data':data})

def productdata(request):
    if request.method=='POST':
        name=request.POST['name'] 
        description=request.POST['description'] 
        category=request.POST['category'] 
        price=request.POST['price'] 
        image=request.FILES['image']
        data=Product(name=name,description=description,category=category,price=price,image=image)
        data.save()
    return redirect('addproduct')

def viewproduct(request):
    data=Product.objects.all()
    return render(request,'viewproduct.html',{'data':data})

def editc(request, id):
    data=Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})

def update(request,id):
    if request.method=='POST':
        name=request.POST['name']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).image
        Category.objects.filter(id=id).update(name=name,image=file)
        return redirect ('viewcategory')

def delete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('viewcategory')

def editpro(request, id):
    data=Category.objects.all()
    pro=Product.objects.filter(id=id)
    return render(request,'editproduct.html',{'data':data,'pro':pro})

def updates(request,id):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description'] 
        category=request.POST['category']
        price=request.POST['price']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).image
        Product.objects.filter(id=id).update(name=name,description=description,category=category,price=price,image=file)
        return redirect ('viewproduct')

def deletes(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('viewproduct')

def contacttable(request):
    data=Contact.objects.all()
    return render(request,'contacttable.html',{'data':data})

def registertable(request):
    data=Register.objects.all()
    return render(request,'registertable.html',{'data':data})

def vieworder(request):
    data=Checkout.objects.all()
    return render(request,'vieworder.html',{'data':data})

def register(request):
    return render(request,'register.html')
