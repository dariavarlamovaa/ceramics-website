# Generated by Django 4.2.4 on 2023-09-15 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_item_color_alter_item_height_alter_item_length_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='type',
            new_name='category',
        ),
    ]