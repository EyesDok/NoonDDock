# Generated by Django 4.2.2 on 2023-08-16 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noonddockApp', '0011_post_location_post_parking_post_reservation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='postImages/')),
                ('post', models.ForeignKey(limit_choices_to={'images__count__lte': 3}, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='noonddockApp.post')),
            ],
        ),
    ]