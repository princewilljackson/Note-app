# Generated by Django 3.0.4 on 2020-07-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_auto_20200702_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(),
        ),
    ]
