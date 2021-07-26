# Generated by Django 3.2.5 on 2021-07-26 13:47

import accounts.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='accounts',
            field=djongo.models.fields.ArrayField(default=None, model_container=accounts.models.Account),
        ),
    ]
