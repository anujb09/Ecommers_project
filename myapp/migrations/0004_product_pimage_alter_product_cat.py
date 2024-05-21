# Generated by Django 5.0.4 on 2024-05-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_cat_alter_product_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'shoes'), (2, 'mobile'), (3, 'cloths'), (4, 'Watch')], verbose_name='Category'),
        ),
    ]
