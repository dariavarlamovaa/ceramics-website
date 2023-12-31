# Generated by Django 4.2.4 on 2023-09-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('price', models.CharField(max_length=5)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
