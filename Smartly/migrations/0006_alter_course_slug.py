# Generated by Django 5.1.6 on 2025-02-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smartly', '0005_course_slug_alter_course_id_alter_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
