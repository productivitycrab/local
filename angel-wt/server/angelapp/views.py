from django.shortcuts import render

def index(request):
    print("leading index")
    return render(request, 'index.html')

