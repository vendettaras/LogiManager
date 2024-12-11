from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Client.views import menu, appartement_ajout,appartement_detail, appartement_effacer, appartement_modifier
from Client.views import chambre_ajout, chambre_modifier, chambre_effacer
from Client.views import ajouter_client, tous_les_clients, client_detail, client_modifier, client_effacer
from Client.views import tous_les_abonnements, abonnement_ajout, abonnement_modifier, abonnement_effacer

urlpatterns=[
    
    path('', menu, name="menu"),
    path('appartement_ajout/', appartement_ajout, name='appartement_ajout'),
    path('chambre_ajout/', chambre_ajout, name='chambre_ajout'),
    path('appartement/<str:pk_test>', appartement_detail, name='appartement'),
    path('ajouter_client/', ajouter_client, name='ajouter_client'),
    path('tous_les_clients/', tous_les_clients, name='tous_les_clients'),
    path('abonnement_ajout/', abonnement_ajout, name='abonnement_ajout'),
    path('tous_les_abonnements/', tous_les_abonnements, name='tous_les_abonnements'),
    path('client/<str:pk_test>', client_detail, name='client'),
    path('modifier_chambre/<str:pk>/', chambre_modifier, name='chambre_modifier'),
    path('appartement_effacer/<str:pk>/',appartement_effacer , name='appartement_effacer'),
    path('appartement_modifier/<str:pk>/', appartement_modifier, name='appartement_modifier'),
    path('abonnement_modifier/<str:pk>/', abonnement_modifier, name='abonnement_modifier'),
    path('client_modifier/<str:pk>/', client_modifier, name='client_modifier'),
    path('abonnement_effacer/<str:pk>/',abonnement_effacer , name='abonnement_effacer'),
    path('chambre_effacer/<str:pk>/',chambre_effacer , name='chambre_effacer'),
    path('client_effacer/<str:pk>/',client_effacer , name='client_effacer'),
]