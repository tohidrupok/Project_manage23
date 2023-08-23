from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import ListView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#store_book
class BookformView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm 
    success_url = reverse_lazy('show_books')
    

##show list
class BooklistView(ListView):
    model = BookStoreModel
    template_name =  'show_book.html'
    context_object_name = 'data'
    ordering=['id']
#edit     
class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
#delet  
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_books') 
    
#complete    
class completeBookView(DeleteView):
    model = BookStoreModel
    template_name = 'complete.html'
    success_url = reverse_lazy('show_books')  
    
