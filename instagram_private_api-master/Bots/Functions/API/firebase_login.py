import firebase_admin

from firebase_admin import credentials

cred = credentials.Certificate('path/to/serviceKey.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://social-kit-23456.firebaseio.com"})

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://social-kit-23456.firebaseio.com'
})