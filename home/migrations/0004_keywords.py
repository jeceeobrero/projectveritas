# Generated by Django 3.2 on 2021-05-23 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_article_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.article')),
            ],
        ),
    ]
