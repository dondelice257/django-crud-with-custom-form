# Generated by Django 4.2.1 on 2023-10-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
