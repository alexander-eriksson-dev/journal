# Generated by Django 3.2.1 on 2021-11-16 17:08

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]