# Generated by Django 3.0.4 on 2020-09-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200923_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_2',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
