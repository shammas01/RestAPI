# Generated by Django 4.2.3 on 2023-07-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_advocate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
