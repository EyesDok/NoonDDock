# Generated by Django 4.2.2 on 2023-08-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noonddockApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/img/defaultImg.png', upload_to='postImage/', verbose_name='IMAGE'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
