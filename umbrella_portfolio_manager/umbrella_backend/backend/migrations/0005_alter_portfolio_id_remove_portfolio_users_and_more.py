# Generated by Django 5.0.1 on 2024-02-07 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_portfolio_users_id_portfolio_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='users',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]