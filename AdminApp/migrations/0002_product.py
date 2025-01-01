# Generated by Django 5.1.2 on 2024-11-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='null.jpg', upload_to='images')),
            ],
        ),
    ]