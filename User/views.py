from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from . import forms
# Create your views here.



def catalog(request, pk):
    if request.user.is_authenticated:
        book = models.Book.objects.get(pk=pk)
        return render(request, 'User/catalog.html',{'album':book})
    else:
        return HttpResponse("you need to login to access book")

def add_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("book saved")
        else:
            form = forms.BookForm()
        return render(request, 'User/settings.html', {'form': form})
    else:
        return HttpResponse("you need to login to access book")

def add_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("category saved")
        else:
            form = forms.CategoryForm()
        return render(request, 'User/categorysave.html', {'form': form})
    else:
        return HttpResponse("you need to login to access categories")
def settings(request):
    if request.user.is_authenticated:
        return render(request,'User/home.html',{})
    else: 
        return HttpResponse("you need to login to access the page")