from ast import Pass
from dataclasses import fields
from msilib.schema import Error
from django import forms
from Client.models import Client, Appartement, Chambre, Abonnement

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class AbonnementForm(forms.ModelForm) :
    class Meta:
        model = Abonnement
        fields = '__all__'

class AppartementForm(forms.ModelForm):
    class Meta:
        model = Appartement
        fields = '__all__'

        labels = {
        'nom_du_cite': '',
        'adresse': '',
        'appart_image': '',
        }

        widgets = {
            'nom_du_cite': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du cité...'}),
            'adresse': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Addresse...'}),
        }

class ChambreForm(forms.ModelForm):
    addresse = forms.ModelChoiceField(queryset=Appartement.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Chambre
        fields = '__all__'

        labels = {
        'numero_du_chambre': 'Numero du Chambre',
        'prix_de_location': 'Prix de location',
        'status': 'Status',
        'addresse': 'Nom appartemant',
        'chambre_image': '',
        }

        widgets = {
            'numero_du_chambre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numéro du chambre'}),
            'prix_de_location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prix en Ariary'}),
            'status' : forms.TextInput(attrs={'class':'form-control', 'value':'Non Occupé', 'type':'text'}) 
        }