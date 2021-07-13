from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictonary = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydictonary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'mysecondpage.html')