# Generated by Django 3.1.5 on 2021-02-01 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210201_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.DecimalField(decimal_places=0, max_digits=6)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Product_Variations',
        ),
    ]
