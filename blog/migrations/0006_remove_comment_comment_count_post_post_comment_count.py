# Generated by Django 4.0.5 on 2022-06-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_user_remove_like_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_count',
        ),
        migrations.AddField(
            model_name='post',
            name='post_comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
