# Generated by Django 2.1.3 on 2018-11-29 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 6, 20, 33, 10, 503205), verbose_name='due date'),
        ),
    ]
