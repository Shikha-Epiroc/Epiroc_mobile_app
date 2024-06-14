# learning_vid\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.videos, name='videos'),  # Videos view
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
