from django.shortcuts import redirect, render
from .models import CategoryProd, Product
from .forms import ImageUploadForm

# Create your views here.
def index(request):
    products= Product.objects.all()
    return render(request,"index.html",{"products": products })

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