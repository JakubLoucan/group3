# Generated by Django 4.2.2 on 2023-08-23 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='obrazek',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='kategorie',
            name='nadkategorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='podkategorie', to='eshop.kategorie'),
        ),
        migrations.AlterField(
            model_name='kategorie',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='znacka',
            name='logo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='znacka',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
