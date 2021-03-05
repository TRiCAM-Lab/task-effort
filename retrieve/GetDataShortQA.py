from collections.abc import Mapping

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service-account-key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()

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

    #find trials where they did not respond
    no_choice_trials = [
        trial for trial in choice_trials
        if trial.get("value").get("key") == 0
    ]

    print(f"number of choice trials: {len(choice_trials)}")
    print(f"number with no key pressed: {len(no_choice_trials)}")
    print(f"percent with no key pressed: {100 * (len(no_choice_trials) / len(choice_trials)):.2f}%")

    #Extract # of trials where they chose the easy balloon
    # involves the choice trials and value: high_effort true vs. false

    high_effort_trials = [
        trial for trial in choice_trials
        if isinstance(trial.get("value"), Mapping) and trial.get("value").get("high_effort")
    ]

    low_effort_trials = [
        trial for trial in choice_trials
        if isinstance(trial.get("value"), Mapping) and trial.get("value").get("high_effort") == False
    ]

    print(f"number of high effort trials: {len(high_effort_trials)}")
    print(f"number of low effort trials: {len(low_effort_trials)}")

    #Extract # of trials where they chose the q trials (vs. p trials)
    q_trials = [
        trial for trial in choice_trials
        if isinstance(trial.get("value"), Mapping) and trial.get("value").get("key") == 81
    ]

    p_trials = [
        trial for trial in choice_trials
        if isinstance(trial.get("value"), Mapping) and trial.get("value").get("key") == 80
    ]

    print(f"number of q trials: {len(q_trials)}")
    print(f"number of p trials: {len(p_trials)}")
