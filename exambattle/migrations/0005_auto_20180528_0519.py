# Generated by Django 2.0 on 2018-05-28 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exambattle', '0004_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Question',
            new_name='question',
        ),
    ]