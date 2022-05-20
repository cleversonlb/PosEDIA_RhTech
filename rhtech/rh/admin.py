from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Departamento)
admin.site.register(Colaborador)
admin.site.register(Empresa)
admin.site.register(NF)
admin.site.register(Escolaridade)
admin.site.register(Departamento_Empresa)
admin.site.register(Folha_Pagamento)
admin.site.register(Ponto)
admin.site.register(Cargo)
