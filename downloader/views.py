from django.shortcuts import render
from django.http import HttpResponse
import pytube

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download()
        return render(request, 'downloader/index.html', {'message': 'Video downloaded successfully'})
    return render(request, 'downloader/index.html')
