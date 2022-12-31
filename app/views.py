from django.shortcuts import render

# Create your views here.

def operations1(request):
    d={'a':11}
    return render(request,'operations1.html',d)