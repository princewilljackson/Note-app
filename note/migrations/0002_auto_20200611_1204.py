# Generated by Django 3.0.4 on 2020-06-11 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.Topic'),
        ),
    ]
