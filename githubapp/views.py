# views.py 

from django.shortcuts import render
from githubsearch import gitHubApi
import requests

# Create your views here.

def profile(request):
    data = {}
    if request.method == 'POST':
        gha = gitHubApi(request)
        data = gha.github_search()
    return render(request, 'app/profile.html', {"data":data})