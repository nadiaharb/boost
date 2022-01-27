from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wow/<slug:division_slug>/', views.division_details, name='division_details'),
    path('wow/services/<slug:service_name_slug>/', views.services, name='services')
]