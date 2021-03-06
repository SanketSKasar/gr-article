# Generated by Django 3.0.2 on 2020-02-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200201_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr',
            name='gr_id',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='unit',
            field=models.CharField(blank=True, choices=[('l', 'litre'), ('yd', 'yard'), ('m', 'metre'), ('kg', 'kilogram')], max_length=2, null=True),
        ),
    ]
