# Generated by Django 3.2.13 on 2022-07-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_customerinfo_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
