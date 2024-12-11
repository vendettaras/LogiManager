from django.db import models
from django.urls import reverse


class Appartement(models.Model) :
    nom_du_cite = models.CharField(max_length=30, null=True)
    adresse = models.CharField(max_length=60, null=True)
    appart_image = models.ImageField(blank=True, upload_to='media/images/', null=True)

    def __str__(self):
        return self.nom_du_cite

class Chambre(models.Model) :
    numero_du_chambre = models.CharField(max_length=30, null=True)
    prix_de_location = models.FloatField(null=True)
    status = models.CharField(max_length=30, null=True)
    addresse = models.ForeignKey(Appartement, on_delete=models.CASCADE, related_name='chambres')
    chambre_image = models.ImageField(blank=True, upload_to='media/images/', null=True)

    def __str__(self):
        return self.numero_du_chambre

class Client(models.Model) :
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    contact = models.CharField(max_length=30, null=True)
    cin = models.CharField(max_length=12, null=True)
    profession = models.CharField(max_length=30, null=True)
    sexe = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nom

class Abonnement(models.Model) :
    debut = models.DateField()
    fin = models.DateField()
    dateDePayement = models.DateField(null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.dateDePayement
