# Generated by Django 4.0.4 on 2022-06-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
            ],
        ),
    ]