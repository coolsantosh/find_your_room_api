# Generated by Django 5.0 on 2023-12-31 06:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double')], max_length=10)),
                ('size', models.IntegerField(help_text='Size in square feet')),
                ('amenities', models.TextField(blank=True, null=True)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=15)),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='room_images/')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Pokhara', 'Pokhara')], max_length=100)),
                ('district', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Pokhara', 'Pokhara')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
