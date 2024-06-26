from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from home.models import Employee
from login.serializers import EmployeeSerializer


@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def about(request):
    return render(request, 'home/about.html')


@login_required
def contact(request):
    return render(request, 'home/contact.html')

class ProfileView(View):
    def get(self, request):
        return render(request, 'home/profiles.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'home/employee_list.html', {'employees': employees})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['skills__name', 'skill_levels__name']

