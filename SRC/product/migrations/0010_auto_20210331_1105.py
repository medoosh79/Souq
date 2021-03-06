# Generated by Django 3.1.7 on 2021-03-31 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_variant'),
        ('product', '0009_auto_20210329_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProImage',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='imge'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PrdBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PrdCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Catogery Name'),
        ),
    ]
