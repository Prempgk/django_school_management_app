# Generated by Django 4.0.3 on 2022-03-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_cstaffuse'),
    ]

    operations = [
        migrations.CreateModel(
            name='useridpassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('role_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
