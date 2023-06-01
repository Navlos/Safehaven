# Generated by Django 4.1.4 on 2023-05-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accomodation', '0002_alter_accomodation_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='state',
            field=models.CharField(choices=[('', 'what state is the hostel in?'), ('Abia ', 'Abia'), ('Adamawa ', 'Adamawa'), ('Akwa Ibom ', 'Akwa Ibom'), ('Anambra ', 'Anambra'), ('Bauchi ', 'Bauchi'), ('Bayelsa ', 'Bayelsa'), ('Benue ', 'Benue'), ('Borno ', 'Borno'), ('Cross River ', 'Cross River'), ('Delta ', 'Delta'), ('Eboniyi ', 'Eboniyi'), ('Edo ', 'Edo'), ('Ekiti ', 'Ekiti'), ('Enugu ', 'Enugu'), ('Gombe ', 'Gombe'), ('Imo ', 'Imo'), ('Jigawa ', 'Jigawa'), ('Kaduna ', 'Kaduna'), ('Kano ', 'Kano'), ('Katsina ', 'Katsina'), ('Kebbi ', 'Kebbi'), ('Kogi ', 'Kogi'), ('Kwara ', 'Kwara'), ('Lagos ', 'Lagos'), ('Nassarawa ', 'Nassarawa'), ('Niger ', 'Niger'), ('Ogun ', 'Ogun'), ('Ondo ', 'Ondo'), ('Osun ', 'Osun'), ('Oyo ', 'Oyo'), ('Plateau ', 'Plateau'), ('Rivers ', 'Rivers'), ('sokoto ', 'Sokoto'), ('Taraba ', 'Taraba'), ('Yobe ', 'Yobe'), ('Zamfara ', 'Zamfara'), ('Federal Capital Territory', 'Federal Capital Territory')], max_length=30),
        ),
    ]