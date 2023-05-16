#Importa o módulo admin e os modelos TiquinhoStats e TiquinhoTeams
from django.contrib import admin
from .models import TiquinhoStats
from .models import TiquinhoTeams

#Registrar os modelos na página de admin do Django
admin.site.register(TiquinhoStats)
admin.site.register(TiquinhoTeams)