# Generated by Django 4.1.1 on 2022-09-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchaseValue',
            field=models.FloatField(null=True),
        ),
    ]
