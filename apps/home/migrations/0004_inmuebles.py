# Generated by Django 3.2.6 on 2022-09-05 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_remove_p_fisica_user_remove_p_moral_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='inmuebles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alies_inmueble', models.CharField(blank=True, max_length=30, null=True)),
                ('renta', models.CharField(blank=True, max_length=30, null=True)),
                ('valor_inmueble', models.CharField(blank=True, max_length=30, null=True)),
                ('clave_catastral', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo_inmueble', models.CharField(blank=True, max_length=30, null=True)),
                ('uso_inmubele', models.CharField(blank=True, max_length=30, null=True)),
                ('estatus', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=30, null=True)),
                ('municipio_alcaldia', models.CharField(blank=True, max_length=30, null=True)),
                ('colonia', models.CharField(blank=True, max_length=30, null=True)),
                ('calle', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, max_length=30, null=True)),
                ('numeroExterior', models.CharField(blank=True, max_length=30, null=True)),
                ('numeroInterior', models.CharField(blank=True, max_length=30, null=True)),
                ('calle1', models.CharField(blank=True, max_length=30, null=True)),
                ('calle2', models.CharField(blank=True, max_length=30, null=True)),
                ('n_baños', models.CharField(blank=True, max_length=30, null=True)),
                ('n_recamaras', models.CharField(blank=True, max_length=30, null=True)),
                ('garaje', models.CharField(blank=True, max_length=30, null=True)),
                ('terrenoTotal', models.CharField(blank=True, max_length=30, null=True)),
                ('terrenoContruido', models.CharField(blank=True, max_length=30, null=True)),
                ('jardin', models.CharField(blank=True, max_length=30, null=True)),
                ('estacionamiento', models.CharField(blank=True, max_length=30, null=True)),
                ('mascotas', models.CharField(blank=True, max_length=30, null=True)),
                ('caracteristicasExtra', models.CharField(blank=True, max_length=30, null=True)),
                ('internet', models.CharField(blank=True, max_length=30, null=True)),
                ('electricidad', models.CharField(blank=True, max_length=30, null=True)),
                ('televisionCable', models.CharField(blank=True, max_length=30, null=True)),
                ('lineaTelefonica', models.CharField(blank=True, max_length=30, null=True)),
                ('camarasSeguridad', models.CharField(blank=True, max_length=30, null=True)),
                ('drenaje', models.CharField(blank=True, max_length=30, null=True)),
                ('aguaPotable', models.CharField(blank=True, max_length=30, null=True)),
                ('gas', models.CharField(blank=True, max_length=30, null=True)),
                ('serviciosExtra', models.CharField(blank=True, max_length=30, null=True)),
                ('fotosInmueble', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Inmuebles',
            },
        ),
    ]
