# Generated by Django 4.2.6 on 2024-01-21 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_site", "0005_rename_timestamp_post_job_datepost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post_job",
            name="datepost",
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]