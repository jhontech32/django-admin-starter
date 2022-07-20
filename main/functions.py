from django.http import HttpResponse

# env reader
import environ
env = environ.Env()
environ.Env.read_env()

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyBWV5Ev50dpREYxJha9oCmvy5La77pVXps",' \
         '        authDomain: "testonesignal-681c3.firebaseapp.com",' \
         '        projectId: "testonesignal-681c3",' \
         '        storageBucket: "testonesignal-681c3.appspot.com",' \
         '        messagingSenderId: "836567093330",' \
         '        appId: "1:836567093330:web:333bd11c58de9dd8aecf8b",' \
         '        measurementId: "G-CRKLDXN01K"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data, content_type="text/javascript")