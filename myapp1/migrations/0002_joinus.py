# Generated by Django 3.0.5 on 2020-10-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joinus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('Class', models.CharField(max_length=30, verbose_name='班级')),
                ('institute', models.CharField(max_length=30, verbose_name='学院')),
                ('number', models.IntegerField(verbose_name='学号')),
            ],
        ),
    ]
