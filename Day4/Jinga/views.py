from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def testpaper(request):
    que ="Who developed Python?"
    a = "Dennis Ritchie"
    b = "Guido van Rossum"
    c = "James Gosling"
    d = " Bjarne Stroustrup"
    context = {
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    template = loader.get_template('testpaper.html')
    res = template.render(context,request)
    return HttpResponse(res)

def info(request):
    name = "Alisha Khan"
    dept = "CSE-AI&DS"
    age = 19
    context = {
        'name':name,
        'dept':dept,
        'age':age
    }
    template = loader.get_template('info.html')
    res = template.render(context,request)
    return HttpResponse(res)
def add(request):
    a = 12
    b = 14
    c = a + b
    context = {
        'a':a,
        'b':b,
        'c':c
    }
    template = loader.get_template('add.html')
    res = template.render(context,request)
    return HttpResponse(res)

def result(request):
    context = {
        'name':"Alisha Khan",
        'marks':82
    }
    return render(request,'result.html',context)

def vote(request):
    context = {
        'name':"Alisha Khan",
        'age':19,
        'country':"India"
    }
    return render(request,'vote.html',context)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')