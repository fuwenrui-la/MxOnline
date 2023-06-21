# Generated by Django 2.2 on 2023-06-09 16:15

import DjangoUeditor.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='章')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
            ],
            options={
                'verbose_name': '课程章',
                'verbose_name_plural': '课程章',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(default='', max_length=1000, verbose_name='课程描述')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='课程标签')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('end_time', models.DateTimeField(null=True, verbose_name='结束时间')),
                ('if_required', models.BooleanField(default=False, verbose_name='是否必修')),
                ('if_only_department', models.BooleanField(default=False, verbose_name='是否专业必修')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Department', verbose_name='课程专业')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='EvaluteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('evalute_type', models.CharField(max_length=10, verbose_name='评分项')),
            ],
            options={
                'verbose_name': '评分项',
                'verbose_name_plural': '评分项',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='节')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter', verbose_name='章')),
            ],
            options={
                'verbose_name': '课程节',
                'verbose_name_plural': '课程节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('url', models.CharField(max_length=1000, verbose_name='访问地址')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Section', verbose_name='节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('evalute_standard', models.CharField(max_length=30, verbose_name='评分标准')),
                ('proportion', models.IntegerField(default=0, verbose_name='分值占比')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('evalute_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.EvaluteItem', verbose_name='评分项')),
            ],
            options={
                'verbose_name': '评分标准',
                'verbose_name_plural': '评分标准',
            },
        ),
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('tag', models.CharField(max_length=100, verbose_name='标签')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程标签',
                'verbose_name_plural': '课程标签',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('file', models.FileField(max_length=200, upload_to='course/resourse/%Y/%m', verbose_name='下载地址')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Section', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.course',),
        ),
    ]
