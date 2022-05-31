from itertools import product
from django.shortcuts import redirect, render

from .Cart import Cart
from .models import CategoryProd, Product
from .forms import ImageUploadForm, RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.contrib.auth import logout
# Create your views here.



def index(request):
    products= Product.objects.all()
    cart= request.session.get("cart")
    lenCart = 0 if cart is None else len(cart)
    return render(request,"index.html",{"products": products, "lenCart": lenCart })

def newProduct(request):
    category=CategoryProd.objects.all()

    #Incluido para poder tener upload_to al momento de guardar la imagen
    form = ImageUploadForm(request.POST, request.FILES)
    
    ######################################

    if request.method=="POST":
        if form.is_valid():
            image=form.cleaned_data['image']

        if "checkbox" in request.POST:
            categories=request.POST.getlist('checkbox')
        title=request.POST.get("title")
        description=request.POST.get("description")
        #category=request.POST.get("category")
        #image=form.cleaned_data['image']
        price=request.POST.get("price")
        
        new_product=Product(title=title,image=image,description=description,price=price)

        
        try:
            new_product.save()

            for category in categories:
                categ = CategoryProd.objects.get(name=category)
                new_product.categories.add(categ)
                #print(category)


            return redirect("/new_product/?valid")
        except:
            return redirect("/new_product/?error")

    return render(request,"new_product.html",{ "categories":category })

def newCategory(request):

    if request.method=="POST":
        name=request.POST.get("name")

        category = CategoryProd(name=name)
        try:
            category.save()
            return redirect("/new_category/?valid")
        except:
            return redirect("/new_category/?error")


    return render(request,"new_category.html",{ })


@login_required
def addCart(request, idProduct):
    cart=Cart(request)
    product= Product.objects.get(id=idProduct)
    cart.add(product=product)

    return redirect("/")
@login_required
def deductCart(request, idProduct):
    cart=Cart(request)
    product= Product.objects.get(id=idProduct)
    cart.deductProduct(product=product)
    return redirect("/cart")
@login_required
def listCart(request):
    cart= request.session.get("cart")
    #print(type(cart))
    #print(cart)
    totalCart=0
    for key in cart:
        #print(cart[key]['price'])


        totalCart= totalCart + (float(cart[key]['price']) * int(cart[key]['quantity']))

    #print(totalCart)
    return render(request, "cart.html", {"cart": cart, "total_cart": totalCart, "lenCart": len(cart)})
@login_required
def cleanCart(request):
    cart=Cart(request)
    cart.cleanCart()
    return redirect("/")
    
##############################################
######Vistas para registro y logout###########
##############################################

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            try:
                form.save()    
                return redirect("/accounts/login/?valid") 
            except:
                return redirect("/accounts/login/?error")     
            #return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {
        'form': form
        })

def logout(request):
    logout(request)
    return redirect("/accounts/login/")