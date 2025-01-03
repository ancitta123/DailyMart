# Generated by Django 5.1.2 on 2024-12-11 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('usercart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.cart')),
                ('usercheckout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.register')),
            ],
        ),
    ]
