        var firebaseConfig = {
          apiKey: "AIzaSyBWV5Ev50dpREYxJha9oCmvy5La77pVXps",
          authDomain: "testonesignal-681c3.firebaseapp.com",
          projectId: "testonesignal-681c3",
          storageBucket: "testonesignal-681c3.appspot.com",
          messagingSenderId: "836567093330",
          appId: "1:836567093330:web:333bd11c58de9dd8aecf8b",
          measurementId: "G-CRKLDXN01K"
        };

        // Initialize Firebase
        firebase.initializeApp(firebaseConfig);
        firebase.analytics();

        const messaging = firebase.messaging();
        console.log('==>', messaging.getToken())
        messaging.getToken({ vapidKey: 'BPEuJhMlSC4FAOQuRfN8rHB0cBb_Hted83-QBANjaHAfIiaWLHemx9FM_syqT-cnx-zTY3HoLlgyDEOvLdEefVQ' }).then((currentToken) => {
        if (currentToken) {
          console.log('TokenId', currentToken)
        } else {
          console.log('No registration token available. Request permission to generate one.');

        }
      }).catch((err) => {
        console.log('An error occurred while retrieving token. ', err);
      });


        messaging
         .requestPermission()
         .then(function () {
           console.log("Notification permission granted.");
           return messaging.getToken()
         })
         .catch(function (err) {
         console.log("Unable to get permission to notify.", err);
       });


        messaging.onMessage((payload) => {
        console.log('Message received. ', payload);

      });

