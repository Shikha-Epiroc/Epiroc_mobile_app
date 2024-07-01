from rest_framework import serializers
from .models import Skill, UserProfile, UserSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = UserSkill
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(source='userskill_set', many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'skills']
