# Generated by Django 4.2.4 on 2023-09-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparison', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comparison',
            old_name='type',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='comparison',
            name='image',
            field=models.ImageField(upload_to='comparison/images'),
        ),
    ]