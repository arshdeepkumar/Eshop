# Generated by Django 3.1.7 on 2021-04-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210427_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
