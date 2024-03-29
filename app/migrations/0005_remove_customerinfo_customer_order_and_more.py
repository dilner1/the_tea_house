# Generated by Django 4.1.1 on 2022-09-28 20:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_newslettersignup_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinfo',
            name='customer_order',
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='company',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='street_address1',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]
