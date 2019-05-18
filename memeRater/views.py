from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def ListMeme(request):
    memes = Meme.objects.all()
    return render(request, 'MemeList.html', {'memes': memes})


@login_required
def NewMeme(request):
    form = AddForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(ListMeme)
    return render(request, 'MemeAdd.html', {'form': form})


@login_required
def EditMeme(request, id):
    meme = get_object_or_404(Meme, pk=id)
    form = EditForm(request.POST or None, request.FILES or None, instance=meme)
    if form.is_valid():
        form.save()
        return redirect(ListMeme)
    return render(request, 'MemeEdit.html', {'form': form})


@login_required
def DeleteMeme(request, id):
    meme = get_object_or_404(Meme, pk=id)

    if request.method == 'POST':
        meme.delete()
        return redirect(ListMeme)
    return render(request, 'ConfirmDelete.html', {'meme': meme})