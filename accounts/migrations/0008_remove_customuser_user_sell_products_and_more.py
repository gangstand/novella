# Generated by Django 4.1.2 on 2022-10-22 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_user_sell_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_sell_products',
        ),
        migrations.RemoveField(
            model_name='products',
            name='user_sell_int',
        ),
    ]
