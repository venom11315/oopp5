from firebase import firebase
import firebase_admin
from firebase_admin import credentials
import json
from firebase_admin import db
firebase = firebase.FirebaseApplication('https://library-system-c45f5.firebaseio.com/', None)

cred = credentials.Certificate('cred/library-system-c45f5-firebase-adminsdk-5ar18-7f7c1f0c15.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://library-system-c45f5.firebaseio.com'
})
root = db.reference()

result = firebase.get('/ls', None)
for x in range(1,21):
    new_user = firebase.post('/mynum', {
        "bn"+str(x): x
    })
