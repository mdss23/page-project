# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alimentacion(models.Model):
    fecha = models.DateField()
    id_galpon = models.ForeignKey('Galpones', models.DO_NOTHING, db_column='id_galpon')
    gr_gallina_dia = models.IntegerField(db_column='Gr/Gallina/Dia')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'alimentacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    documento = models.IntegerField()
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DetalleJornada(models.Model):
    fecha = models.DateField()
    id_galpon = models.ForeignKey('Galpones', models.DO_NOTHING, db_column='id_galpon')
    id_jornada = models.ForeignKey('Jornada', models.DO_NOTHING, db_column='id_jornada')
    rotos = models.IntegerField()
    descarte = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_jornada'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estados(models.Model):
    estado = models.AutoField(primary_key=True)
    descrip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estados'


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha_regis = models.DateField()
    num_ficha = models.CharField(max_length=50)
    titulacion = models.CharField(max_length=50)
    estado_ficha = models.ForeignKey(Estados, models.DO_NOTHING, db_column='estado_ficha')

    class Meta:
        managed = False
        db_table = 'ficha'


class Gallinas(models.Model):
    id_galpon = models.ForeignKey('Galpones', models.DO_NOTHING, db_column='id_galpon')
    id_linea = models.ForeignKey('Linea', models.DO_NOTHING, db_column='id_linea')
    fecha_ingreso = models.DateField()
    cantidad_gallinas = models.IntegerField()
    peso_promedio = models.IntegerField()
    edad_sem = models.IntegerField()
    procedencia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gallinas'


class Galpones(models.Model):
    fecha = models.DateField()
    nombre_galpon = models.CharField(max_length=100)
    ancho = models.IntegerField()
    largo = models.IntegerField()
    area = models.IntegerField()
    capac_bebed = models.IntegerField()
    cant_bebed = models.IntegerField()
    capac_comed = models.IntegerField()
    cant_comed = models.IntegerField()
    capac_gall = models.IntegerField()
    cant_gall = models.IntegerField()
    fecha_regis = models.DateField()

    class Meta:
        managed = False
        db_table = 'galpones'


class Jornada(models.Model):
    jornada = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jornada'


class Linea(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'linea'


class MortalidadDescarte(models.Model):
    fecha = models.DateField()
    id_galpon = models.ForeignKey(Galpones, models.DO_NOTHING, db_column='id_galpon')
    cant_muertas = models.IntegerField()
    cant_descarte = models.IntegerField()
    saldo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mortalidad_descarte'


class ProduccionDiaria(models.Model):
    id_detalle_jornada = models.ForeignKey(DetalleJornada, models.DO_NOTHING, db_column='id_detalle_jornada')
    id_tipo_huevo = models.ForeignKey('TiposHuevos', models.DO_NOTHING, db_column='id_tipo_huevo')
    cantidad = models.IntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'produccion_diaria'


class Rol(models.Model):
    tipo_rol = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rol'


class TipoDoc(models.Model):
    tipo_doc = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_doc'


class TiposHuevos(models.Model):
    tipos_huevos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tipos_huevos'


class Usuario(models.Model):
    is_superuser = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    id_tipo_doc = models.ForeignKey(TipoDoc, models.DO_NOTHING, db_column='id_tipo_doc', blank=True, null=True)
    documento = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='id_ficha', blank=True, null=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol', blank=True, null=True)
    password = models.CharField(max_length=100)
    imagen = models.CharField(max_length=60, blank=True, null=True)
    registro = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
