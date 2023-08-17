from django.shortcuts import render, redirect
from . import models
def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, "home.html",{'data':student})

def delet_student(request,roll):
    std= models.Student.objects.get(pk= roll).delete()
    print(std)
    return redirect("homepage")

