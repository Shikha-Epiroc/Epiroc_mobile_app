# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),  # Login or index page
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.logout, name='logout'),  # Add this line for logout
#     path('home/', views.home, name='home'),
#     path('forum_redirect/', views.forum_redirect, name='forum_redirect'),  # Redirect to forum
#     path('videos/', views.videos_redirect, name='videos_redirect'),  # Redirect to videos
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('forum_redirect/', views.forum_redirect, name='forum_redirect'),
    path('videos/', views.videos_redirect, name='videos_redirect'),
]
