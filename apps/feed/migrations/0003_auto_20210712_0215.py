# Generated by Django 3.2.5 on 2021-07-11 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='liked_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='liked_by',
            new_name='created_by',
        ),
    ]
