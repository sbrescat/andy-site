# Generated by Django 5.0.6 on 2024-06-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_articles_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='banner',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]
