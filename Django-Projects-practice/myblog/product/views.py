from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    return HttpResponse("this is product page")

def product_list(request):
    return HttpResponse("this is product list page")


def prod_cat(request):
    return HttpResponse("this is product category page")


def Student_detail(request, id):
    return HttpResponse(f"student id is {id}")


def product_detail(request, name):
    return HttpResponse(f"product name {name}")


def article_by_year(request, year):
    return HttpResponse(f"year: {year}")