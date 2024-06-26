from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('employee_list/<int:id>/', views.employee_update, name='employee_update'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('home/', views.home, name='home'),
    path('forum_redirect/', views.forum_redirect, name='forum_redirect'),
    path('videos/', views.videos_redirect, name='videos_redirect'),
    path('login/', views.user_login, name='user_login'),
]
