# Generated by Django 5.1.3 on 2025-01-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genrapp', '0017_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
