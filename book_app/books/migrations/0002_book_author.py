# Generated by Django 3.1 on 2020-08-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
