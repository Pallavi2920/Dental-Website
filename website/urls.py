from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index.html',views.index,name="index"),
    path('contact.html',views.contact,name="contact"),
    path('news.html',views.news,name="news"),
    path('patients.html',views.patients,name="patients"),
    path('services.html',views.services,name="services"),
    path('about.html',views.about,name="about"),
    path('appointment.html',views.appointment,name="appointment"),
]
