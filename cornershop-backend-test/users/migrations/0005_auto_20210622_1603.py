# Generated by Django 3.0.8 on 2021-06-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210622_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]
