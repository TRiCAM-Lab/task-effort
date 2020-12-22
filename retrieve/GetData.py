from collections.abc import Mapping

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service-account-key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()

trials = db.collection(u'db_pilot_test').document(u'5ad90f90dec767000128a5f4').collection(u'data').stream()

call_function_trials = [trial.to_dict() for trial in trials if trial.to_dict().get("trial_type") == "call_function"]
choice_trials = [
    trial for trial in call_function_trials
    if isinstance(trial.get("value"), Mapping) and trial.get("value").get("subtrial_type") == "choice"
]

no_choice_trials = [
    trial for trial in choice_trials
    if trial.get("value").get("key") == 0
]

print(f"number of choice trials: {len(choice_trials)}")
print(f"number with no key pressed: {len(no_choice_trials)}")
print(f"percent with no key pressed: {100 * (len(no_choice_trials) / len(choice_trials)):.2f}%")
