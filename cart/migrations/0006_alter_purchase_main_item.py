# Generated by Django 4.2.4 on 2023-09-14 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_item_color_alter_item_height_alter_item_length_and_more'),
        ('cart', '0005_purchase_main_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='main_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item'),
        ),
    ]
