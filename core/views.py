from django.shortcuts import render

# request is used to get user browser info

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
