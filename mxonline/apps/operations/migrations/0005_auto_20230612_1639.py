# Generated by Django 2.2 on 2023-06-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_userallcourse_last_click_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userallcourse',
            name='course_type',
            field=models.CharField(choices=[('not_start', '未开始'), ('progressing', '正在进行'), ('endding', '已结束')], max_length=20, verbose_name='课程类别'),
        ),
    ]
