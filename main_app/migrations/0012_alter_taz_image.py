# Generated by Django 4.1.4 on 2023-01-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_taz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taz',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
