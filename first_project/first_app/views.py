from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("Hello,this is my first django apps.")

def about(request):
   return HttpResponse("Hello about apps,this is my first django  page.")