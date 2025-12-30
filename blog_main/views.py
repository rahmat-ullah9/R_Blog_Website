#from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category

def home(request):
    #return HttpResponse("Welcome to the Blog Home Page!")
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)