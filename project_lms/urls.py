"""
URL configuration for project_lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from login.views import *

# urlpatterns = [
#     path('', home, name='login'),
#     path('admin/', admin.site.urls),
#     path('api/login/', include('login.urls')),
#     path('api/home/', include('home.urls')),
#     path('api/disc_forum/', include('disc_forum.urls')),
#     path('api/learning_vid/', include('learning_vid.urls')),
#     path('', include('home.urls')),
#     path('forum/', include('disc_forum.urls')),
#     path('videos/', include('learning_vid.urls')),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('login.urls')),  # Login app
#     path('forum/', include('disc_forum.urls')),  # Forum app
#     path('videos/', include('learning_vid.urls')),  # Videos app
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('login.urls')),  # Include login app URLs as root
#     path('forum/', include('disc_forum.urls')),  # Include forum app URLs
#     path('home/', include('home.urls')),  # Include home app URLs
#     path('videos/', include('learning_vid.urls')),  # Include videos app URLs
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('disc_forum/', include('disc_forum.urls')),
    path('videos/', include('learning_vid.urls')),
    path('home/', include('home.urls')),
    path('', include('login.urls')),
]
