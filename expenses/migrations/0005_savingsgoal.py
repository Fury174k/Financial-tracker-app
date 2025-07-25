# Generated by Django 5.2.2 on 2025-06-19 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('target', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saved', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings_goals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
