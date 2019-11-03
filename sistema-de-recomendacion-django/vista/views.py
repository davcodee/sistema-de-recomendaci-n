from django.shortcuts import render

# Create your views here.

def recomendaciones(request):
    return render(request,'index.html')
