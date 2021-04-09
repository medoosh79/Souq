# Generated by Django 3.1.7 on 2021-03-29 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productalternative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CatImg',
            field=models.ImageField(upload_to='category/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CatName',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CatParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CatParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
    ]