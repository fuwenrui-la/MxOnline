# Generated by Django 2.2 on 2023-06-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_tag',
            field=models.CharField(default='', max_length=25, verbose_name='专业'),
        ),
    ]
