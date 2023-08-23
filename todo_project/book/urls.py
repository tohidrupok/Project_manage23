from django.urls import path
from .import views
urlpatterns = [
    
    path('', views.BookformView.as_view(), name ='storebook' ),  
    path('show_books/', views.BooklistView.as_view(), name ='show_books' ),  
    path('edit_book/<int:pk>',views.BookUpdateView.as_view() , name='edit_book'),
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'),
    path('complete_book/<int:pk>', views.completeBookView.as_view(), name='complete_book'),
]
