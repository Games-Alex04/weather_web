from django.urls import path
from weatherapp import views

urlpatterns = [

    path('home',views.home, name='home'),
    # path('home_store',views.home_store, name='home_store'),
    
]

