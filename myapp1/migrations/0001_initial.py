# Generated by Django 3.0.5 on 2020-09-12 16:29

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='fs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('track_id', models.CharField(max_length=20)),
                ('is_Delete', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='new_resiger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='resiger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('time', models.DateField(auto_now=True)),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('content', mdeditor.fields.MDTextField()),
                ('column', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='myapp1.ArticleColumn')),
            ],
            options={
                'verbose_name': '我的博客',
                'verbose_name_plural': '我的博客',
            },
        ),
    ]