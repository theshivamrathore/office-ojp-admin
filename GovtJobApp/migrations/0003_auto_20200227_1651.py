# Generated by Django 2.2.6 on 2020-02-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovtJobApp', '0002_auto_20200227_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='railwayjobsmodel',
            name='total_post',
            field=models.CharField(max_length=100),
        ),
    ]
