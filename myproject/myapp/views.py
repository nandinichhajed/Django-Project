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
    return render(request,'second.html')

def mythirdpage(request):
    var = "Hello world"
    greeting = "Hey how are you"
    fruits = ["Apple", "Mango", "Banana"]
    num1, num2 = 10, 7
    ans = num1 > num2
    mydictonary = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans,
    }
    return render(request,'third.html', context = mydictonary)

