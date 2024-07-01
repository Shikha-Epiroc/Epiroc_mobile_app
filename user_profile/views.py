from rest_framework import generics, filters
from django.contrib.auth.models import User
from .models import UserProfile, UserSkill, Skill
from .serializers import UserProfileSerializer, UserSkillSerializer
from django.shortcuts import render, get_object_or_404, redirect

class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['skills__skill__name', 'skills__level']

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserSkillCreate(generics.CreateAPIView):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer

class UserSkillUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer

def profiles_page(request):
    profiles = UserProfile.objects.all()
    return render(request, 'user_profile/profiles.html', {'profiles': profiles})

def edit_competency_page(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    user_skills = UserSkill.objects.filter(user_profile=user_profile)
    return render(request, 'user_profile/edit_competency.html', {'user_skills': user_skills})


def add_skill_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        skill_name = request.POST.get('skill')
        skill_level = request.POST.get('level')
        Skill.objects.create(user=user, name=skill_name, level=skill_level)
        print(f"Skill '{skill_name}' at level '{skill_level}' added for user '{user.username}'")
        return redirect('profiles')
    return render(request, 'user_profile/add_skill.html', {'user': user})



from django.shortcuts import render
from django.db.models import Q
from .models import User, Skill  # Adjust import as per your actual models

# def profiles_view(request):
#     users = User.objects.all()  # Fetch all users
#     user_skills = Skill.objects.all()  # Fetch all skills

#     # Handle skill and level search queries
#     skill_query = request.GET.get('skill', None)
#     level_query = request.GET.get('level', None)

#     if skill_query:
#         user_skills = user_skills.filter(name__icontains=skill_query)

#     if level_query:
#         user_skills = user_skills.filter(level=level_query)

#     context = {
#         'users': users,
#         'user_skills': user_skills,
#     }
#     return render(request, 'user_profile/profiles.html', context)


def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        skill.delete()
        return redirect('profiles')  # Redirect to profiles page after deletion
    return render(request, 'user_profile/delete_skill.html', {'skill': skill})

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        skill.name = request.POST.get('name')
        skill.level = request.POST.get('level')
        skill.save()
        return redirect('profiles')  # Redirect to profiles page after update
    return render(request, 'user_profile/update_skill.html', {'skill': skill})

# views.py

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import User, Skill  # Adjust import as per your actual models

# def profiles_view(request):
#     skill_query = request.GET.get('skill', '')
#     level_query = request.GET.get('level', '')

#     if skill_query or level_query:
#         user_skills = Skill.objects.all()
#         if skill_query:
#             user_skills = user_skills.filter(name__icontains=skill_query)
#         if level_query:
#             user_skills = user_skills.filter(level__icontains=level_query)
#         user_ids = user_skills.values_list('user_id', flat=True).distinct()
#         users = User.objects.filter(id__in=user_ids)
#     else:
#         users = User.objects.all()

#     context = {
#         'users': users,
#         'skill_query': skill_query,
#         'level_query': level_query,
#     }
#     return render(request, 'user_profile/profiles.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Skill

@login_required
def profiles_view(request):
    skill_query = request.GET.get('skill', '')
    level_query = request.GET.get('level', '')

    if skill_query or level_query:
        user_skills = Skill.objects.all()
        if skill_query:
            user_skills = user_skills.filter(name__icontains=skill_query)
        if level_query:
            user_skills = user_skills.filter(level__icontains=level_query)
        user_ids = user_skills.values_list('user_id', flat=True).distinct()
        users = User.objects.filter(id__in=user_ids)
    else:
        users = User.objects.all()

    context = {
        'users': users,
        'skill_query': skill_query,
        'level_query': level_query,
        'logged_in_user_id': request.user.id,  # Pass the logged-in user's ID to the template
    }
    return render(request, 'user_profile/profiles.html', context)
