# Generated by Django 4.1.4 on 2023-01-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_taz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taz',
            name='restrictions',
            field=models.ManyToManyField(blank=True, to='main_app.restriction'),
        ),
    ]
