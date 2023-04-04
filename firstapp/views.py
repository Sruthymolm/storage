from django.shortcuts import render

# Create your views here.
def loadfirstpage(request):
    return render(request,'first.html')
#to render second file
def loadsecondpage(request):
    return render(request,'second.html')
