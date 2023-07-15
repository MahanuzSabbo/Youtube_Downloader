from django.shortcuts import render
from django.contrib import messages
from pytube import *
# import instaloader
# import models 

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        messages.info(request, 'Video Downloaded..')
        return render(request, 'index.html')
    return render(request, 'index.html')
# ig = instaloader.Instaloader()
# video_url = input("entr")
# ig.download_videos(video_url)

# ig = instaloader.Instaloader()
# req_user = input("enter req")
# user_id = input("entr id")
# user_password = input("entr pass")
# ig.login(user_id, user_password)
# ig.download_profile(req_user)