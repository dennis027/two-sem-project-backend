# Generated by Django 4.1.4 on 2023-03-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='drug',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]