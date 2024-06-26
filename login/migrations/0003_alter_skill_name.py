# Generated by Django 5.0.6 on 2024-06-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_skill_employee_additional_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('python', 'Python'), ('sql', 'SQL'), ('cpp', 'C++'), ('selenium', 'Selenium'), ('k8s', 'Kubernetes'), ('docker', 'Docker'), ('jira', 'JIRA'), ('linux', 'LINUX'), ('django', 'Django'), ('html', 'HTML'), ('css', 'CSS'), ('csharp', 'C#'), ('javascript', 'JavaScript')], max_length=100),
        ),
    ]
