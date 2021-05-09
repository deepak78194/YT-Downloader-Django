from django.shortcuts import render, redirect

from pytube import YouTube
import os
from django.http import FileResponse
import pafy

def home(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')