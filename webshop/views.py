from django.shortcuts import render

# Create your views here.
def indax(request) :
    return render(request, 'index.html')

def login(request) :
    return render(request, 'login.html')

def classic(request) :
    return render(request, 'classic.html')

def quiter(request) :
    return render(request, 'quiter.html')

def basket(request) :
    return render(request, 'basket.html')

