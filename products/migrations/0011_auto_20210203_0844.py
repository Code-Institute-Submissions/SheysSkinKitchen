# Generated by Django 3.1.5 on 2021-02-03 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210203_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='parent',
        ),
    ]
