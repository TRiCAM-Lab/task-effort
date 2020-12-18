import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service-account-key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()

docs = db.collection(u'db_pilot_test').document(u'test').collection(u'data').stream()

for doc in docs:
    # output each doc into a file
    print(f'{doc.id} => {doc.to_dict()}')
