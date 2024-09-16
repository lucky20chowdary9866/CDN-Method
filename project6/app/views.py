from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request,'basic.html')

def buttons(request):
    return render(request,'buttons.html')

def dummy(request):
    return render(request,'dummy.html')
def home(request):
    return render(request,'home.html')

def carousel(request):
    return render(request,'carousel.html')

def alerts(request):
    return render(request,'alerts.html')