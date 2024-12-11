from django.contrib import admin
from Client.models import Client, Appartement, Chambre, Abonnement

# Register your models here.

admin.site.register([Client, Appartement, Chambre, Abonnement])

