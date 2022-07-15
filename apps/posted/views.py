from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    # pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # convert reponse data into json
    posts = response.json()

    context = {
        'page': 'Posted',
        'posts': posts
    }
    return render(request, 'Posted/index.html', context)
