# Generated by Django 4.2.4 on 2023-08-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0002_rename_emp_id_add_by_user_rdp_emp_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_rdp",
            name="IP_Address",
            field=models.BigIntegerField(),
        ),
    ]
