from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myinfo(request):
    n = "<h1>Name: Alisha Khan </h1> <br> <h1>Roll no: 0187AS241019</h1> <br> <h1>"
    return HttpResponse(n)

def clginfo(request):
    clg = "<h1> Sagar Institute of Science and Technology Gandhinagar"
    return HttpResponse(clg)