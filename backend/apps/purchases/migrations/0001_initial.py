# Generated by Django 4.1.1 on 2022-10-07 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customUser', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('purchaseName', models.CharField(max_length=200)),
                ('placePurchase', models.CharField(max_length=200, null=True)),
                ('isDetailedPurchase', models.BooleanField()),
                ('purchaseValue', models.FloatField(null=True)),
                ('typePayment', models.CharField(max_length=200, null=True)),
                ('note', models.CharField(max_length=500, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customUser.teammodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DetailedPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('productName', models.CharField(max_length=200)),
                ('amount', models.FloatField(default=1)),
                ('price', models.FloatField()),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.purchase')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customUser.teammodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
