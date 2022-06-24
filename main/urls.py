
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('api/',views.HomeClass.as_view(),name='apihome'),

]
