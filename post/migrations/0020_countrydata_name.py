# Generated by Django 4.2.1 on 2023-06-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_alter_countrydata_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrydata',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
