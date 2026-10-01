from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def facebook(request):
    s = "<h1> This is Facebook Page"
    return HttpResponse(s)

def linkedin(request):
    s = "<h1> This is LinkedIn Page"
    return HttpResponse(s)