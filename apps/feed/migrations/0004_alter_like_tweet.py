# Generated by Django 3.2.5 on 2021-07-11 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210712_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.tweet'),
        ),
    ]
