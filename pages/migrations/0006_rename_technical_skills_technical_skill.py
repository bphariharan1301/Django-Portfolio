# Generated by Django 3.2.4 on 2021-06-29 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_technical_skills_experience_level'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Technical_Skills',
            new_name='Technical_Skill',
        ),
    ]
