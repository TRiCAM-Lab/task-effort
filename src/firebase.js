import firebase from "firebase";
require("dotenv").config();

const collectionName = "db_pilot_test";
const config = {
  apiKey: process.env.REACT_APP_apiKey,
  authDomain: process.env.REACT_APP_authDomain,
  databaseURL: process.env.REACT_APP_databaseURL,
  projectId: "task-effort",
  storageBucket: process.env.REACT_APP_storageBucket,
  messagingSenderId: process.env.REACT_APP_messagingSenderId,
  appId: process.env.REACT_APP_appId,
  measurementId: process.env.REACT_APP_measurementId,
};
// Get a Firestore instance
const db = firebase.initializeApp(config).firestore();

// Add data to db
const createFirebaseDocument = (patientId) => {
  db.collection(collectionName).doc(patientId).set({
    patientId,
    dateCreated: new Date(),
  });
};

// create a document in the collection with a random id
const createFirebaseDocumentRandom = () => {
  db.collection(collectionName).add({
    dateCreated: new Date(),
  });
};

const addToFirebase = (data) => {
  const patientId = data.patient_id;
  db.collection(collectionName)
    .doc(patientId)
    .collection("data")
    .doc(`trial_${data.trial_index}`)
    .set(data);
};

// Export types that exists in Firestore
// This is not always necessary, but it's used in other examples
const { TimeStamp, GeoPoint } = firebase.firestore;
export {
  db,
  TimeStamp,
  GeoPoint,
  createFirebaseDocument,
  addToFirebase,
  createFirebaseDocumentRandom,
};

export default firebase;