import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://trashbotfacerec-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "2022002974":
        {
            "name": "Aman Chand",
            "department": "CSE",
            "year": "3rd",
            "sem": "5th",
            "contact": "+91 63XXXXXXXX",
            "e-mail": "2022002974.aman@ug.sharda.ac.in"

        },
    "2022003852":
        {
            "name": "Elon Musk",
            "department": "CSE",
            "year": "3rd",
            "sem": "5th",
            "contact": "+1 109XXXXXX",
            "e-mail": "2022003852.elon@pg.sharda.ac.in"
        },
    "2022445249":
        {
            "name": "Shubham Jaswar",
            "department": "CSE",
            "year": "3rd",
            "sem": "5th",
            "contact": "+91 96XXXXXXXX",
            "e-mail": "2022445249.shubham@ug.sharda.ac.in"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
