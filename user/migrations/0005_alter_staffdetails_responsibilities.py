# Generated by Django 4.0.3 on 2022-03-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_staffnmae_staffdetails_staffname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='responsibilities',
            field=models.CharField(max_length=1000),
        ),
    ]