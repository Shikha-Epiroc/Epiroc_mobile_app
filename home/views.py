from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def about(request):
    return render(request, 'home/about.html')


@login_required
def contact(request):
    return render(request, 'home/contact.html')
