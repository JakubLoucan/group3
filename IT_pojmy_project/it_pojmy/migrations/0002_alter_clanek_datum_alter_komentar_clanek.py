# Generated by Django 4.2.2 on 2023-08-03 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanek',
            name='datum',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='komentar',
            name='clanek',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='komentare_clanku', to='it_pojmy.clanek'),
        ),
    ]