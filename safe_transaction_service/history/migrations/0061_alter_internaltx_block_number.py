# Generated by Django 3.2.13 on 2022-05-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0060_add_eip1559_fields_20220419_0955"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internaltx",
            name="block_number",
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
