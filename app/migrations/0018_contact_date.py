# Generated by Django 4.1.4 on 2022-12-27 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_diagnosis_diagnosis_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]