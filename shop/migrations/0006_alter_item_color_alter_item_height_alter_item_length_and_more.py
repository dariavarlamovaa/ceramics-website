# Generated by Django 4.2.4 on 2023-09-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_diameter_item_length_remove_item_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='length',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
