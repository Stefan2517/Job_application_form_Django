from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('contact', views.Contact.as_view(), name = 'contact')
]