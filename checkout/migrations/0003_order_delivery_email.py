# Generated by Django 4.2.6 on 2023-10-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_order_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_email',
            field=models.EmailField(default='DEFAULT VALUE', max_length=254),
        ),
    ]
