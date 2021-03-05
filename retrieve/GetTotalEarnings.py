
import sys
from collections.abc import Mapping

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account
cred = credentials.Certificate('./service-account-key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()


for row in sys.stdin:
    id = row.strip()
    sub = db.document(u'db_pilot_test', id).get()
    print(f'{sub.id}, {sub.to_dict().get("totalEarnings") or 0}')
