# Generated by Django 3.1.1 on 2020-09-11 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaidik_admin', '0002_auto_20200911_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='image',
            new_name='thumbnail',
        ),
    ]