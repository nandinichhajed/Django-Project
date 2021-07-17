from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *

def error_404_view(request,exception):
    return render(request,'404.html')

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = "hello world"
    greeting = "hey how are you"
    fruits = ["apple","mango","banana"]
    num1 , num2 = 10 , 7
    ans = num1 > num2
    #print(ans)
    mydictionary = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render(request,'third.html',context=mydictionary)

def myimagepage(request):
    return render(request,'image.html')


def myimagepage2(request):
    return render(request,'image2.html')

def myimagepage3(request):
    return render(request,'image3.html')

def myimagepage4(request):
    return render(request,'image4.html')

def myimagepage5(request,imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var=True
    elif myimagename == "python":
        var=False
    mydictionary ={
        "var":var
    }
    return render(request,'image5.html',context=mydictionary)

def myform(request):
    return render(request,'myform.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        forms = FeedbackForm(request.POST)
        if forms.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var = str("Form Submited" + str(request.method))
            return HttpResponse(var)
        else:
            mydictionary = {
                "form" : form,
            }
            return render(request,'myform2.html', context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm()    # FeedbackForm(None)
        mydictionary = {
            "form" : form,
        }
        return render(request,'myform2.html', context=mydictionary)