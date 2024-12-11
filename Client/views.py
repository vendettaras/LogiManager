from django.shortcuts import render, redirect, get_object_or_404
from Client.forms import *
from Client.models import Abonnement, Client, Chambre, Appartement
from django.db.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request) :
    appartements = Appartement.objects.annotate(nombre_chambres=Count('chambres'))
    return render(request, 'Client/menu.html', context={"appartements": appartements})

def appartement_ajout(request):
    form = AppartementForm()
    if request.method == 'POST':
        form = AppartementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')

    return render(request,'Client/appartement/appartement_ajout.html',context = {'form': form})

def chambre_ajout(request):
    form = ChambreForm()
    if request.method == 'POST':
        form = ChambreForm(request.POST, request.FILES)
        if form.is_valid():
            chambre = form.save(commit=False)
            chambre.addresse_id = request.POST.get('addresse')
            chambre.save()
            return redirect('menu')

    return render(request,'Client/chambre/chambre_ajout.html',context = {'form': form})

def appartement_detail(request, pk_test ):
    appartement = Appartement.objects.get(id=pk_test)
    return render(request, 'Client/appartement/appartement_detail.html', context={"appartement": appartement})

def ajouter_client(request):
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    contact = request.POST.get("contact")
    profession = request.POST.get("profession")
    cin = request.POST.get("cin")
    sexe = request.POST.get("sexe")
    client = Client(nom=nom, prenom=prenom, contact=contact, profession=profession, cin=cin, sexe=sexe)
    # form = ClientForm()
    if request.method == 'POST':
        # form = ClientForm(request.POST)
        if client :
            client.save()
            return redirect('tous_les_clients')

    return render(request,'Client/client/ajouter_client.html')

def tous_les_clients(request) :
    clients = Client.objects.all()
    return render(request, 'Client/client/tous_les_clients.html', context={"clients": clients})

def abonnement_ajout(request):
    clients = Client.objects.all()
    appartements = Appartement.objects.all()
    chambres = Chambre.objects.raw("SELECT VENDETTE.client_chambre.id, VENDETTE.client_chambre.numero_du_chambre as chambres_dispo FROM VENDETTE.client_chambre WHERE VENDETTE.client_chambre.status = 'Non Occupé';")
    # form = AbonnementForm()

    if request.method == 'POST':
        debut = request.POST.get("debut")
        fin = request.POST.get("fin")
        client_name = request.POST.get("client")
        chambre_name = request.POST.get("chambre")
        appartement_name = request.POST.get("appartement")
        status = request.POST.get("status")
        
        # form = AbonnementForm(request.POST)
        client = Client.objects.get(nom=client_name)
        chambre = Chambre.objects.get(numero_du_chambre=chambre_name)
        appartement = Appartement.objects.get(nom_du_cite=appartement_name)
        abonnement = Abonnement(debut=debut, fin=fin, client=client, chambre=chambre, appartement=appartement, status=status)
        if abonnement :
            abonnement.save()
            return redirect('tous_les_abonnements')

    return render(request,'Client/abonnement/abonnement_ajout.html', context={"appartements": appartements, "chambres" : chambres, "clients" : clients})

def tous_les_abonnements(request) :
    from django.db import connection

    query = """
    SELECT SUM(client_chambre.prix_de_location) AS somme_prix_de_location
    FROM client_chambre
    INNER JOIN client_abonnement ON client_chambre.id = client_abonnement.chambre_id
    WHERE client_abonnement.status = 'Payé'
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    somme_prix_de_location = result[0] if result else 0

    query2 = """
    SELECT SUM(client_chambre.prix_de_location) AS somme_prix_de_location_n
    FROM client_chambre
    INNER JOIN client_abonnement ON client_chambre.id = client_abonnement.chambre_id
    WHERE client_abonnement.status = 'Non Payé'
    """

    with connection.cursor() as cursor:
        cursor.execute(query2)
        result = cursor.fetchone()

    somme_prix_de_location1 = result[0] if result else 0

    nombre_lignes = Client.objects.count()

    abonnements = Abonnement.objects.all()
    return render(request, 'Client/abonnement/tous_les_abonnements.html', context={"abonnements": abonnements, "somme_prix_de_location": somme_prix_de_location, "somme_prix_de_location1" : somme_prix_de_location1, "nombre_lignes": nombre_lignes})

def client_detail(request, pk_test ):
    client = Client.objects.get(id=pk_test)
    abonnements = client.abonnement_set.all()
    return render(request, 'Client/client/detail_client.html', context={"client": client, "abonnements":abonnements})

def chambre_modifier(request, pk):

    chambre = Chambre.objects.get(id=pk)
    form = ChambreForm(instance=chambre)

    if request.method == 'POST':
        form = ChambreForm(request.POST, instance=chambre)
        if form.is_valid():
            form.save()
            return redirect('menu')

    return render(request, 'Client/chambre/chambre_modifier.html', context={'form': form})


def appartement_effacer(request, pk):
    appartement = Appartement.objects.get(id=pk)
    if request.method == 'POST':
        appartement.delete()
        return redirect('menu')
    return render(request, 'Client/appartement/appartement_effacer.html', context={'item':appartement})

def appartement_modifier(request, pk):

    appartement = Appartement.objects.get(id=pk)
    form = AppartementForm(instance=appartement)

    if request.method == 'POST':
        form = AppartementForm(request.POST, instance=appartement)
        if form.is_valid():
            form.save()
            return redirect('menu')

    return render(request, 'Client/appartement/appartement_modifier.html', context={'form': form})

def abonnement_modifier(request, pk):

    abonnement = Abonnement.objects.get(id=pk)
    form = AbonnementForm(instance=abonnement)

    if request.method == 'POST':
        form = AbonnementForm(request.POST, instance=abonnement)
        if form.is_valid():
            form.save()
            return redirect('menu')

    return render(request, 'Client/abonnement/abonnement_modifier.html', context={'form': form})

def client_modifier(request, pk):

    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('menu')

    return render(request, 'Client/client/client_modifier.html', context={'form': form})

def abonnement_effacer(request, pk):
    abonnement = Abonnement.objects.get(id=pk)
    if request.method == 'POST':
        abonnement.delete()
        return redirect('menu')
    return render(request, 'Client/abonnement/abonnement_effacer.html', context={'item':abonnement})

def chambre_effacer(request, pk):
    chambre = Chambre.objects.get(id=pk)
    if request.method == 'POST':
        chambre.delete()
        return redirect('menu')
    return render(request, 'Client/chambre/chambre_effacer.html', context={'item':chambre})

def client_effacer(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('menu')
    return render(request, 'Client/client/client_effacer.html', context={'item':client})


    