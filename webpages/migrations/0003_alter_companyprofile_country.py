# Generated by Django 3.2.16 on 2022-12-21 19:43

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_alter_companyprofile_cac_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='Country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]