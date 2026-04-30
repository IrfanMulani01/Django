from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    return HttpResponse("this is product page")

# def product_list(request):
#     return HttpResponse("this is product list page")