# Generated by Django 5.0.6 on 2024-06-12 08:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_comments_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
