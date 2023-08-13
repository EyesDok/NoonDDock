# Generated by Django 4.2.2 on 2023-08-13 15:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noonddockApp', '0005_rename_user_post_family_rename_user_save_family_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='family',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='save',
            old_name='family',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='save',
            unique_together={('user', 'post')},
        ),
    ]