# Generated by Django 3.0.5 on 2020-10-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_joinus'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinus',
            name='direction',
            field=models.CharField(default='不清楚', max_length=130, verbose_name='方向'),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='Class',
            field=models.CharField(max_length=130, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='institute',
            field=models.CharField(max_length=130, verbose_name='学院'),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='name',
            field=models.CharField(max_length=130, verbose_name='姓名'),
        ),
    ]