# Generated by Django 4.2.1 on 2023-06-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_caption_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, default=' ', max_length=20000, null=True),
        ),
    ]
