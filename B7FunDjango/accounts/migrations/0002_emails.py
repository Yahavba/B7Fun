# Generated by Django 2.2.11 on 2020-05-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=500)),
                ('sent', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Emails',
                'db_table': 'Emails',
            },
        ),
    ]
