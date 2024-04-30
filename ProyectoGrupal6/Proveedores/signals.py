from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from Proveedores.models import Proveedores

@receiver(post_migrate)
def create_groups(sender, **kwargs):

    # creacion de grupos
    operadores_group, _ = Group.objects.get_or_create(name='Operadores')
    consultores_group, _ = Group.objects.get_or_create(name='Consultores')
    vendedores_group, _ = Group.objects.get_or_create(name='Vendedores')
    administradores_group, _ = Group.objects.get_or_create(name='Administradores')

    content_type = ContentType.objects.get_for_model(Proveedores)

    # operadores permisos
    perm_operadores = Permission.objects.filter(content_type__app_label='Proveedores')

    # admin
    perm_administradores = Permission.objects.filter(content_type__app_label='admin')

    # vendedores
    perm_vendedores = Permission.objects.filter(content_type__model='session')

    # consultores

    perm_consultores = Permission.objects.filter(content_type__model='permission')

    # asignar permisos
    operadores_group.permissions.set(perm_operadores)
    administradores_group.permissions.set(perm_administradores)
    consultores_group.permissions.set(perm_consultores)
    vendedores_group.permissions.set(perm_vendedores)
