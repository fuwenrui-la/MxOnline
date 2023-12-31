# Generated by Django 2.2 on 2023-06-12 15:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20230612_1540'),
        ('audits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('last_audit_time', models.DateField(null=True, verbose_name='上次审核时间')),
                ('opinion', models.CharField(default='', max_length=1000, verbose_name='整体修改意见')),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseResource')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
            ],
            options={
                'verbose_name': '文档审核',
                'verbose_name_plural': '文档审核',
            },
        ),
        migrations.CreateModel(
            name='DocumentDetailOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('number', models.IntegerField(verbose_name='序号')),
                ('opinion', models.CharField(default='', max_length=300, verbose_name='细节修改意见')),
                ('document_audit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='audits.DocumentAudit', verbose_name='审核文档')),
            ],
            options={
                'verbose_name': '文档审核细节',
                'verbose_name_plural': '文档审核细节',
            },
        ),
        migrations.CreateModel(
            name='VideoAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('last_audit_time', models.DateField(null=True, verbose_name='上次审核时间')),
                ('opinion', models.CharField(default='', max_length=1000, verbose_name='整体修改意见')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Video')),
            ],
            options={
                'verbose_name': '视频审核',
                'verbose_name_plural': '视频审核',
            },
        ),
        migrations.CreateModel(
            name='VideoDetailOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('timestamp', models.CharField(max_length=10, verbose_name='时间点')),
                ('opinion', models.CharField(default='', max_length=300, verbose_name='细节修改意见')),
                ('video_audit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='audits.VideoAudit', verbose_name='审核视频')),
            ],
            options={
                'verbose_name': '视频审核细节',
                'verbose_name_plural': '视频审核细节',
            },
        ),
        migrations.RemoveField(
            model_name='courseorg',
            name='city',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='org',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='CourseOrg',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
