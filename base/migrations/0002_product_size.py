# Generated by Django 5.1.1 on 2024-09-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
