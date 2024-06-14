from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Login or index page
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),  # Add this line for logout
    path('home/', views.home, name='home'),
    path('forum/', views.forum_redirect, name='forum_redirect'),  # Redirect to forum
    path('videos/', views.videos_redirect, name='videos_redirect'),  # Redirect to videos
]
