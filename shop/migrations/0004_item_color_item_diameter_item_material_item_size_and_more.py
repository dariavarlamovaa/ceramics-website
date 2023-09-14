# Generated by Django 4.2.4 on 2023-09-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='diameter',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.IntegerField(default='1'),
        ),
    ]
