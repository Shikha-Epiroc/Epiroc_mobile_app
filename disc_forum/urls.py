# from django.urls import path
# from .views import ForumView
# from . import views


# urlpatterns = [
#     # path('', ForumView.as_view(), name='forum_api'),  # API View
#     path('forum/', ForumView.as_view(), name='forum'),  # Avoid recursion by pointing to the same view
#     path('post_question/', views.post_question, name='post_question'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/<int:pk>/', views.question_detail, name='question_detail'),
    path('post_question/', views.post_question, name='post_question'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
