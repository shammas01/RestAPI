# Generated by Django 4.2.3 on 2023-07-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_advocate_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advocate',
            name='twitter',
            field=models.URLField(null=True, verbose_name='*args, **kwargs'),
        ),
    ]
