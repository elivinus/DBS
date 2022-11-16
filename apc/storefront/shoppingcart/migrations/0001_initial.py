# Generated by Django 4.1.3 on 2022-11-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
                ('itemList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.itemlist')),
            ],
        ),
    ]
