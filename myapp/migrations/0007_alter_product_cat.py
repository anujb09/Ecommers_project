# Generated by Django 5.0.4 on 2024-05-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'shoes'), (2, 'mobile'), (3, 'cloths'), (4, 'Watch'), (5, 'Sports')], verbose_name='Category'),
        ),
    ]
