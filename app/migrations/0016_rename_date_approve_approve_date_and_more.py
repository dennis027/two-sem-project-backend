# Generated by Django 4.1.4 on 2022-12-27 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_date_diagnosis_diagnosis_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approve',
            old_name='date',
            new_name='approve_date',
        ),
        migrations.RenameField(
            model_name='testimonies',
            old_name='date',
            new_name='testimony_date',
        ),
        migrations.RenameField(
            model_name='testimonies',
            old_name='location',
            new_name='testimony_location',
        ),
        migrations.RenameField(
            model_name='testimonies',
            old_name='message',
            new_name='testimony_message',
        ),
        migrations.RenameField(
            model_name='testimonies',
            old_name='subject',
            new_name='testimony_subject',
        ),
    ]
