# Generated by Django 4.0.2 on 2022-09-07 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_rename_alies_inmueble_inmuebles_alias_inmueble_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_moral',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]