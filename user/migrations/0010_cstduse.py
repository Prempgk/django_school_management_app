# Generated by Django 4.0.3 on 2022-03-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_std10_std11_std12_std3_std4_std5_std6_std7_std8_std9'),
    ]

    operations = [
        migrations.CreateModel(
            name='cstduse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_standard', models.CharField(max_length=20)),
            ],
        ),
    ]
