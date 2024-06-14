from django.urls import path
from .views import ForumView

urlpatterns = [
    # path('', ForumView.as_view(), name='forum_api'),  # API View
    path('forum/', ForumView.as_view(), name='forum'),  # Avoid recursion by pointing to the same view
]
