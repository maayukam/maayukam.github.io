# Generated by Django 2.0 on 2018-05-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exambattle', '0003_signup_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=255)),
            ],
        ),
    ]