# Generated by Django 5.1 on 2024-09-22 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_insert_menu"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="order",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="product",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
    ]
