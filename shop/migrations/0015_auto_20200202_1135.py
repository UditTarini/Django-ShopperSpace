# Generated by Django 3.0.2 on 2020-02-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200202_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(max_length=100),
        ),
    ]
