from django.shortcuts import render
from .models import *
from .forms import MemeForm


def ListMeme(request):
    memes = Meme.objects.all()
    return render(request, 'MemeList.html', {'memes': memes})


def NewMeme(request):
    form = MemeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'MemeAdd.html', {'form': form})