from django.urls import path

from portfolio_app import views

urlpatterns = [
    path('',views.contact,name='Home'),

]