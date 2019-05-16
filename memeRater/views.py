from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def ListMeme(request):
    memes = Meme.objects.all()
    return render(request, 'MemeList.html', {'memes': memes})


def NewMeme(request):
    form = AddForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(ListMeme)
    return render(request, 'MemeAdd.html', {'form': form})


def EditMeme(request, id):
    meme = get_object_or_404(Meme, pk=id)
    form = EditForm(request.POST or None, request.FILES or None, instance=meme)
    if form.is_valid():
        form.save()
        return redirect(ListMeme)
    return render(request, 'MemeAdd.html', {'form': form})


def DeleteMeme(request, id):
    meme = get_object_or_404(Meme, pk=id)

    if request.method == 'POST':
        meme.delete()
        return redirect(ListMeme)
    return render(request, 'ConfirmDelete.html', {'meme': meme})