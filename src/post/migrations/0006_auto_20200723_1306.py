# Generated by Django 2.1.4 on 2020-07-23 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200723_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='next_pst',
            new_name='next_post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='previous_pst',
            new_name='previous_post',
        ),
    ]
