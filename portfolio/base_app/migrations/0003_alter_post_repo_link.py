# Generated by Django 4.1.6 on 2023-02-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_post_repo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='repo_link',
            field=models.CharField(default='#', max_length=150),
        ),
    ]