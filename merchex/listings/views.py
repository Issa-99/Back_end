from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band,Annonces

def hello(request):
    bands = Band.objects.all()
    annonces = Annonces.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands':bands,
                   'annonces':annonces
                   })

def about(request):
    return render(request,'listings/about.html')

def contact (request):
     return render(request,'listings/contact.html')