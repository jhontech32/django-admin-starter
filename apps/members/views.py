from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    # pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    # convert reponse data into json
    users = response.json()

    context = {
        'page': 'Members',
        'users': users
    }
    return render(request, 'Members/index.html', context)