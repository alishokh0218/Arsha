from django.shortcuts import render
from appfolder.models import *


# Create your views here.
def index(malumot):
    servis = Servis.objects.all()
    portfolioo = Portfolio.objects.all()
    team = Team.objects.all()
    return render(malumot, 'index.html', {"servis": servis, "portfolioo": portfolioo, "team": team})


def inner_page(malumot):
    return render(malumot, 'inner-page.html')


def portfolio(malumot, id):
    portfolioo = Portfolio.objects.get(id=id)
    return render(malumot, 'portfolio-details.html', {"portfolioo": portfolioo})


def contact(malumot):
    if malumot.method == "POST":
        ism = malumot.POST.get('ism')
        email = malumot.POST.get('email')
        yonalish = malumot.POST.get('yonalish')
        malumott = malumot.POST.get('malumot')
        Contact(ism=ism, yonalish=yonalish, malumot=malumott, email=email).save()
    contact = Contact.objects.all()
    return render(malumot, 'index.html', {"contact": contact})
