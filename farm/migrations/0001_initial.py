# Generated by Django 4.2.9 on 2024-02-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earing_number', models.CharField(max_length=50)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
    ]