# Generated by Django 4.2.1 on 2023-10-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_rename_country_merchant_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchant',
            old_name='count',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='merchant',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
