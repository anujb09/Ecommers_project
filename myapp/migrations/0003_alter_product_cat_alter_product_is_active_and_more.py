# Generated by Django 5.0.4 on 2024-05-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'shoes'), (2, 'mobile'), (3, 'cloths')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is_availabe'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=200, verbose_name='Details'),
        ),
    ]