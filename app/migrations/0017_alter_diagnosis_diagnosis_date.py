# Generated by Django 4.1.4 on 2022-12-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_date_approve_approve_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
