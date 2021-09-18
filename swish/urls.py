from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('index', views.hello),
    path('emp', views.emp),
    path('/redirect/',views.emp),
    path('saveform', views.saveform),
    path('editdetails', views.editdetails),
    path('getEmployee', views.getEmployee),
    path('edit', views.edit),
]
