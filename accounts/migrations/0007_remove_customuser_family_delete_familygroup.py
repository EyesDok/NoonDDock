# Generated by Django 4.2.2 on 2023-08-13 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_familygroup_customuser_family'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='family',
        ),
        migrations.DeleteModel(
            name='FamilyGroup',
        ),
    ]
