# Generated by Django 3.0.2 on 2020-01-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20200130_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
