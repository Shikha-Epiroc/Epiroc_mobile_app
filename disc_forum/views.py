from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# API View for discussion forum
class ForumView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Welcome to the discussion forum!"})

# Function-based view for rendering forum HTML page
def forum(request):
    return render(request, 'disc_forum/forum.html')
