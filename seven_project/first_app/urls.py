from django.urls import path 
# from . import views
from first_app.views import home

urlpatterns = [
    path('', home ,name="homepage"),
    #path('show/', showData, name='showData'),
]
