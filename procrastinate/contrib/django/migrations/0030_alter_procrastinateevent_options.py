# Generated by Django 5.0.8 on 2024-08-08 14:27
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        migrations.AlterModelOptions(
            name="procrastinateevent",
            options={"get_latest_by": "at", "managed": False},
        ),
    ]
    name = "0030_alter_procrastinateevent_options"
    dependencies = [
        ("procrastinate", "0029_add_additional_params_to_retry_job"),
    ]
