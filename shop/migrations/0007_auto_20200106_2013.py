# Generated by Django 3.0 on 2020-01-06 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20191226_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
