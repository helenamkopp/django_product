from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listProducts', views.listProducts),
    path('formProducts', views.formProducts),
    path('listCategories', views.listCategories),
    path('formCategories', views.formCategories),
]