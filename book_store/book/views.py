from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView ,ListView,DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'store_book.html')

# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')
#     else:
#          book = BookStoreForm()
#     return render(request, 'store_book.html', {'form':book})
#############by class

class BookformView(FormView):
    template_name = 'store_book.html'
    form_class = BookStoreForm 
    success_url = reverse_lazy('show_books')
    
    def form_valid(self, form):
        return redirect('Form Submitted')
#shortcut_class_vies#######
class BookformView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm 
    success_url = reverse_lazy('show_books')
    
   
   
   
# def store_book(request):
#     book = BookStoreForm()
#     return render(request , 'store_book.html',{'form':book}) 

# def show_books(request):
#     book = BookStoreModel.objects.all() 
#     print(book)
#     return render(request, 'show_book.html',{'data':book})


########class based view#########

class BooklistView(ListView):
    model = BookStoreModel
    template_name =  'show_book.html'
    context_object_name = 'data'
    
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id = '32') 
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'data': BookStoreModel.objects.all().order_by('author')}
    #     return context
    ordering=['id']
    
    
##Normal viewes
# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance = book)
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST, instance = book)
#         if form.is_valid():
#             form.save()
#             return redirect('show_books')
#     return render(request, 'store_book.html', {'form':form})
    
###################class views###########################
    
class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
    
###################Delet views###########################
    
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_books')  
    
    
    
    
    
    
    
    
    ######classbasedview#########

class MyTemplateview(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'rahim',  'age':21 }
        context.update(kwargs)
        print(kwargs)
        
        return context
        
        
        
        
        
########### Details of book  #################

class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    