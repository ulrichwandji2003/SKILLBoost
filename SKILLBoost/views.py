from django.shortcuts import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from Login.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def index(request):


    return render(request, 'index.html')

def inscription(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        institut = request.POST.get('institut')
        photo = request.FILES.get('photo')
        cv = request.FILES.get('cv')

        user = User(
            username=username,
            email=email,
            password=password,
            institut=institut,
            role='stagiaire',
            photo=photo,
            cv=cv
        )
        user.save()
        if user:
            return redirect("connexion")
        return render(request, 'connexion/connexion.html')


    return render(request, 'inscription/inscription.html')


def connexion(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
       

        if not username or not password:
            # Vérification des champs vides
            messages.error(request, 'Veuillez remplir tous les champs.')
            return render(request, 'inscription/inscription.html') 
        

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            print(username, password)
            login(request, user)
            
            return redirect('dashboard')  # Redirection vers le tableau de bord
        else:
            # Identifiants invalides
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')

    return render(request, 'connexion/connexion.html')


@login_required
def dashboard(request):


    return render(request, 'dashboard/dashboard.html')