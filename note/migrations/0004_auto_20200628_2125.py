# Generated by Django 3.0.4 on 2020-06-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200618_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(unique=True),
        ),
    ]
