from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):
    # Incio
    home = Home.objects.latest('updated')

    # Acerca de
        #Obteno el ultimo regitro
    about = About.objects.latest('updated')
        #Que me extraiga el ultimo perfil registrado
    profiles = Profile.objects.filter(about=about)

    # Habilidades
    categories = Category.objects.all()

    # Portafolio
    portfolios = Portfolio.objects.all()

    context={
        'home':home,
        'about':about,
        'profiles':profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    

    return render(request, 'index.html', context)
