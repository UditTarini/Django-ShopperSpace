# Generated by Django 3.0.2 on 2020-01-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('Trending', 'trending'), ('New', 'new'), ('50%', '50%')], default='New', max_length=16),
        ),
    ]
