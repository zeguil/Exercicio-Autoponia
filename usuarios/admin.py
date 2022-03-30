from django.contrib import admin
from usuarios.models import Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)