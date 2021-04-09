# Generated by Django 3.1.7 on 2021-03-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VerName', models.CharField(max_length=50)),
                ('VerDesc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
    ]