# Generated by Django 4.2.2 on 2023-08-14 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noonddockApp', '0006_rename_family_post_user_rename_family_save_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Save',
            new_name='Like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='recommend',
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(default=0, verbose_name='LIKE_COUNT'),
        ),
    ]
