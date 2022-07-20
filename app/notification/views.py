from django.shortcuts import render, redirect

import requests
import json

# env reader
import environ
env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    return render(request, 'Notification/index.html')

def send_notification(
        registration_ids,
        message_title,
        message_desc
):
     fcm_api = env('FCM_SERVER_KEY')
     url = 'https://fcm.googleapis.com/fcm/send'

     headers = {
          "Content-Type": "application/json",
          "Authorization": 'key='+fcm_api
     }

     payload = {
          "registration_ids": registration_ids,
          "priority": "high",
          "notification": {
               "body": message_desc,
               "title": message_title,
               "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
               "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj"
          }
     }

     result = requests.post(url, data=json.dumps(payload), headers=headers)
     print('result notification', result.json())

def send(request):
     registration = [env('FCM_SENDER_ID')]
     print('registration send', registration)
     send_notification(registration, 'Code added a new video', 'Code added a new video')
     return redirect('notification')
