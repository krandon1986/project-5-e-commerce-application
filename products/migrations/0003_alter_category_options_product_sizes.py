# Generated by Django 5.0.6 on 2024-07-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
