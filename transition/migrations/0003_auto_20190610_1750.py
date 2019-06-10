# Generated by Django 2.2.2 on 2019-06-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transition', '0002_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(default='no org. descrition'),
        ),
        migrations.AddField(
            model_name='organization',
            name='external_link',
            field=models.TextField(default='no external link'),
        ),
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.TextField(default='no org. image'),
        ),
        migrations.AddField(
            model_name='organization',
            name='industry',
            field=models.CharField(default='no specified industry', max_length=100),
        ),
        migrations.AddField(
            model_name='organization',
            name='name',
            field=models.CharField(default='no name', max_length=100),
        ),
    ]