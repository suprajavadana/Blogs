# Generated by Django 4.1.3 on 2022-11-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=10)),
                ('percentage', models.CharField(max_length=4)),
                ('backlogs', models.IntegerField()),
            ],
        ),
    ]
