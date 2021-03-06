# Generated by Django 3.2 on 2021-05-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credibility_score', models.FloatField()),
                ('relevancy_score', models.FloatField()),
                ('opinion_score', models.FloatField()),
                ('sattire_score', models.FloatField()),
                ('sensational_score', models.FloatField()),
                ('topic', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
    ]
