# Generated by Django 3.1.5 on 2021-02-03 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product_detail'),
        ),
    ]
