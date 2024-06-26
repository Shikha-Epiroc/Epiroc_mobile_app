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
    path('employee_list<int:id>/', views.signup, name='employee_update'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_delete<int:id>/', views.employee_delete, name='employee_delete'),
    path('home/', views.home, name='home'),
    path('forum_redirect/', views.forum_redirect, name='forum_redirect'),
    path('videos/', views.videos_redirect, name='videos_redirect'),
]



# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('signin/', views.signin_page, name='signin'),
#     path('home/', views.home_page, name='home'),
#     path('', views.signup_page, name='employee_insert'),
#     path('employee_list<int:id>/', views.signup_page, name='employee_update'),
#     path('employee_list/', views.employee_list, name='employee_list'),
#     path('employee_delete<int:id>/', views.employee_delete, name='employee_delete')
# ]