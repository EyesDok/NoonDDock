# Generated by Django 4.2.2 on 2023-08-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noonddockApp', '0009_post_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.IntegerField(blank=True, null=True, verbose_name='테마'),
        ),
    ]
