from django.shortcuts import render
from .forms import Add_product
from .models import Product

def add_prod(request):
    if request.method == "POST":
        form = Add_product(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
    
    else:
        form = Add_product()

    return render(request, 'temp/index.html', {'form':form})

def disp_prod(request):
    prod = Product.objects.all()
    return render(request, 'temp/list.html', {'product': prod})
