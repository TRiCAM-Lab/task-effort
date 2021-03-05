import sys
from collections.abc import Mapping

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service-account-key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()

#potential way to pull ID names from a csv files
#do this instead of getting all subjects
#command call python GetData.py < IDs.csv
# for row in sys.stdin:
#     id = row.strip()
#     sub = db.document(u'db_pilot_test', id).get()

#get all subject collections (just first level)
subs = db.collection(u'db_pilot_test').stream()

#loop through subjects
for sub in subs:
    print(f'{sub.id}, {sub.to_dict()}')

    # Get a collection from anywhere
    trials = db.collection(u'db_pilot_test', sub.id, u'data').stream()

    # Get a document from anywhere
    # trial_foo = db.document(u'db_pilot_test', sub.id, u'data', u'trial_1').get()

    #extract all choice trials
    call_function_trials = [trial.to_dict() for trial in trials if trial.to_dict().get("trial_type") == "call_function"]
    choice_trials = [
        trial for trial in call_function_trials
        if trial.get("code") == 40
        # if isinstance(trial.get("value"), Mapping) and trial.get("value").get("subtrial_type") == "choice"
    ]
