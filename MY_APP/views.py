from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'condition.html',d)
def loop(request):
    d={'name':'mahesh babu','age':20,'cls':'python'}
    return render(request,'loop.html',d)