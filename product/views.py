from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listProducts(request):
    return render(request, 'listProducts.html')

def formProducts(request):
    return render(request, 'formProducts.html')

def listCategories(request):
    return render(request, 'listCategories.html')

def formCategories(request):
    return render(request, 'formCategories.html')