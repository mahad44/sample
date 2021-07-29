# Generated by Django 3.0.8 on 2021-07-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('sod', models.IntegerField()),
                ('region', models.CharField(max_length=200)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('cost', models.IntegerField()),
                ('modeules', models.CharField(choices=[('Ticketing', 'Web Ticketing'), ('Appointment', 'Appointment'), ('Queue', 'Queue Management'), ('Others', 'Others')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='table1',
        ),
    ]