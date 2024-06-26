from django.urls import path, include
from . import views
from .views import ProfileView
from rest_framework.routers import DefaultRouter
from home.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profiles/', ProfileView.as_view(), name='profiles'),
    path('', include(router.urls)),
    path('employees/', views.employee_list, name='employee_list'),

]
    
