# Generated by Django 2.2.2 on 2019-06-13 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transition', '0004_auto_20190613_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='state_id',
            new_name='state',
        ),
    ]
