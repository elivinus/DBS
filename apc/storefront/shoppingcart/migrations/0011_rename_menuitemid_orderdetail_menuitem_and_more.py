# Generated by Django 4.1.3 on 2022-11-24 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0010_alter_order_orderstatus_alter_order_totalamount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='menuItemId',
            new_name='menuItem',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='orderId',
            new_name='order',
        ),
    ]
