# Generated by Django 5.0.1 on 2024-02-10 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_remove_portfolio_users_portfolio_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_price',
            name='quantity',
        ),
    ]
