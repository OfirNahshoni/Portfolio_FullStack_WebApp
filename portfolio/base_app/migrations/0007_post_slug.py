# Generated by Django 4.1.6 on 2023-03-03 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_alter_post_repo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
