# Generated by Django 4.1.3 on 2022-12-15 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0015_remove_customer_name_remove_customer_userpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='emailaddress',
        ),
    ]