from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def showproducts (request):
    objects = Category.objects.all()
    return render(request, 'showproducts.html', {'objects':objects})

