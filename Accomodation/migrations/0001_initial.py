# Generated by Django 4.1.4 on 2023-04-28 03:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agents', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('state', models.CharField(choices=[('', 'what state is the hostel in?'), ('Abia state', 'Abia'), ('Adamawa state', 'Adamawa'), ('Akwa Ibom state', 'Akwa Ibom'), ('Anambra state', 'Anambra'), ('Bauchi state', 'Bauchi'), ('Bayelsa state', 'Bayelsa'), ('Benue state', 'Benue'), ('Borno state', 'Borno'), ('Cross River state', 'Cross River'), ('Delta state', 'Delta'), ('Eboniyi state', 'Eboniyi'), ('Edo state', 'Edo'), ('Ekiti state', 'Ekiti'), ('Enugu state', 'Enugu'), ('Gombe state', 'Gombe'), ('Imo state', 'Imo'), ('Jigawa state', 'Jigawa'), ('Kaduna state', 'Kaduna'), ('Kano state', 'Kano'), ('Katsina state', 'Katsina'), ('Kebbi state', 'Kebbi'), ('Kogi state', 'Kogi'), ('Kwara state', 'Kwara'), ('Lagos state', 'Lagos'), ('Nassarawa state', 'Nassarawa'), ('Niger state', 'Niger'), ('Ogun state', 'Ogun'), ('Ondo state', 'Ondo'), ('Osun state', 'Osun'), ('Oyo state', 'Oyo'), ('Plateau state', 'Plateau'), ('Rivers state', 'Rivers'), ('Sokoto state', 'Sokoto'), ('Taraba state', 'Taraba'), ('Yobe state', 'Yobe'), ('Zamfara state', 'Zamfara'), ('Federal Capital Territory', 'Federal Capital Territory')], max_length=30)),
                ('school', models.CharField(max_length=70)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Hostel_name', models.CharField(max_length=70)),
                ('Address', models.CharField(max_length=70)),
                ('LGA', models.CharField(max_length=70)),
                ('image_1', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(upload_to='images/')),
                ('image_3', models.ImageField(upload_to='images/')),
                ('image_4', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=4000, validators=[django.core.validators.MinLengthValidator(10)])),
                ('date_time_uploaded', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_public_id', models.CharField(max_length=255)),
                ('Agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Agents.agent')),
                ('amenities', models.ManyToManyField(to='Accomodation.amenity')),
            ],
        ),
    ]
