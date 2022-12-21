# Generated by Django 3.2.16 on 2022-12-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('name_of_organization', models.CharField(max_length=255)),
                ('number_of_employees', models.IntegerField()),
                ('director_1', models.CharField(max_length=255)),
                ('director_2', models.CharField(max_length=255)),
                ('director_3', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=255)),
                ('country', models.CharField(choices=[('Alg', 'Algeria'), ('Ang', 'Angola'), ('Ben', 'Benin'), ('Bot', 'Botswana')], max_length=3)),
                ('organization_reg_no', models.IntegerField(max_length=255)),
                ('cac_no', models.IntegerField(max_length=255)),
                ('proposal_status', models.BooleanField(default=False)),
                ('correspondence_status', models.BooleanField(default=False)),
                ('receiver_status', models.BooleanField(default=False)),
                ('clearance_status', models.BooleanField(default=False)),
            ],
        ),
    ]
