# Generated by Django 4.2 on 2023-05-11 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_alter_order_customer_alter_shippingaddress_customer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="customer",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="customer",
            new_name="user",
        ),
    ]