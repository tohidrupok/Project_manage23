from django.urls import path , include
from . import views

urlpatterns = [
    path('course/',views.course),
    path('feedback/',views.feedback),
    
]