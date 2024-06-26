from django.db import models

class SkillLevel(models.TextChoices):
    BEGINNER = 'Beginner'
    PROFICIENT = 'Proficient'
    EXPERT = 'Expert'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    skills = models.JSONField()  # List of skills
    skill_levels = models.JSONField()  # List of skill levels corresponding to skills
    total_work_experience = models.IntegerField(help_text="Total years of work experience")
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
