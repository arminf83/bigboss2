# Generated by Django 4.0.3 on 2024-09-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_category_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
