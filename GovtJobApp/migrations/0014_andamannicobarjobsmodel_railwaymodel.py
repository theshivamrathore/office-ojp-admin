# Generated by Django 2.2.6 on 2020-02-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovtJobApp', '0013_defencejobsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndamanNicobarJobsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.CharField(blank=True, max_length=100)),
                ('recruitment_board', models.CharField(blank=True, max_length=200)),
                ('post_name', models.CharField(blank=True, max_length=300)),
                ('qualification', models.CharField(blank=True, max_length=200)),
                ('advt_no', models.CharField(blank=True, max_length=100)),
                ('last_date', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RailwayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.CharField(blank=True, max_length=100)),
                ('recruitment_board', models.CharField(blank=True, max_length=200)),
                ('post_name', models.CharField(blank=True, max_length=300)),
                ('qualification', models.CharField(blank=True, max_length=200)),
                ('advt_no', models.CharField(blank=True, max_length=100)),
                ('last_date', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
