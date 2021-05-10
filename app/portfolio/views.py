from django.shortcuts import render
from .models import Profile, Skill, Work, Carrer

def index(request):
    profile = Profile.objects.all().last()
    skills = Skill.objects.all()
    works = Work.objects.all().order_by('-published')[:3]
    carrer = Carrer.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'works': works,
        'carrer': carrer,
    }
    return render(request, 'index.html', context)

def works(request):
    works = Work.objects.all().order_by('-published')
    context = {
        'works': works,
    }   
    return render(request, 'works.html', context)
