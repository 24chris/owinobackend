# Generated by Django 3.2.13 on 2022-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slider_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
