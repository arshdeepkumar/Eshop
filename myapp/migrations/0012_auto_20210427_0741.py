# Generated by Django 3.1.7 on 2021-04-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210427_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
