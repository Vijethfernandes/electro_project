# Generated by Django 4.2.6 on 2023-11-15 16:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electro_app', '0002_alter_customer_request_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customer_request',
            new_name='Contact',
        ),
    ]