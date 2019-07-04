import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import socket


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('192.168.35.9',12000))

server_socket.listen(0)

client_socket,addr = server_socket.accept()

data = client_socket.recv(65535)

result = data.decode()

print("recieve Data : ",data.decode())

cred = credentials.Certificate('data-collection-e9d72-firebase-adminsdk-6fyka-7aa7fde935.json')

##firebase_admin.initialize_app(cred, {
##    'databaseURL': 'https://data-collection-e9d72.firebaseio.com/'
##})

firebase_admin.initialize_app(cred, {
    'https://living-lab-5aff5.firebaseio.com/'
})

ref = db.reference('data')
users_ref = ref.child('Omega')
users_ref.set({
    'Omega_all' : result,
    'Omega_beacon ':2
})
