from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def videos(request):
    return render(request, 'learning_vid/videos.html')
