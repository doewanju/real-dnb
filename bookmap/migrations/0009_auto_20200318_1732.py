# Generated by Django 2.2.6 on 2020-03-18 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0008_auto_20200318_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookstore',
            options={'ordering': ['bookstore_id']},
        ),
    ]
