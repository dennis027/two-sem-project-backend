# Generated by Django 4.1.4 on 2022-12-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_testimonies_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='approve',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
