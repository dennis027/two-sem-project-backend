# Generated by Django 4.1.4 on 2022-12-21 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testimonies',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=60)),
                ('message', models.CharField(blank=True, max_length=300)),
                ('date', models.DateField(null=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]