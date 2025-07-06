###########################################################
# 🔐 Face Recognition using Firebase
###########################################################

A Python-based real-time face recognition system integrated with Google Firebase.  
It encodes face images, recognizes individuals via webcam, and stores user data in Firebase.

-----------------------------------------------------------
✨ FEATURES
-----------------------------------------------------------
✅ Real-time face detection via webcam  
✅ Face encoding using face_recognition  
✅ Stores encodings in EncodeFile.p  
✅ Firebase Realtime DB integration:
   └── Store user data (name, ID, dept, etc.)
✅ Visual detection with face annotations

🔮 Future Enhancement:
   → Attendance auto-marking with time-logging

-----------------------------------------------------------
🛠️ TECH STACK
-----------------------------------------------------------
- Python 3
- face_recognition
- OpenCV
- Firebase Admin SDK
- Pickle (serialization)

-----------------------------------------------------------
📁 PROJECT STRUCTURE
-----------------------------------------------------------
.
├── AddDataToDatabase.py     # Uploads user data to Firebase
├── EncodeGenerator.py       # Generates face encodings
├── EncodeFile.p             # Saved face encodings
├── main.py                  # Real-time face recognition system
├── Images/                  # Folder of face images (<ID>.jpg/png)
└── README.md

-----------------------------------------------------------
🚀 SETUP & RUN INSTRUCTIONS
-----------------------------------------------------------

# 1️⃣ Clone the repository
$ git clone https://github.com/amanrudra01/face_recognition_using_firebase.git
$ cd face_recognition_using_firebase

# 2️⃣ Install dependencies
$ pip install -r requirements.txt

# (If requirements.txt is missing, do this instead:)
$ pip install face_recognition opencv-python firebase-admin

# 3️⃣ Setup Firebase
>> Go to https://console.firebase.google.com/
>> Create a project
>> Go to Project Settings > Service Accounts > Generate new private key
>> Save the key as serviceAccountKey.json in your project root
>> Enable Firebase Realtime Database (in test mode)

# 4️⃣ Add user face images
>> Place all user face images in the Images/ folder
>> Image file names should follow: <ID>.jpg or <ID>.png

# 5️⃣ Generate face encodings
$ python EncodeGenerator.py
>> This creates EncodeFile.p with all encodings

# 6️⃣ Upload user info to Firebase
$ python AddDataToDatabase.py
>> Ensure metadata (IDs) match image names in Images/

# 7️⃣ Run the face recognition system
$ python main.py
>> Starts webcam and identifies users in real-time
>> (Future enhancement: will mark attendance)

-----------------------------------------------------------
✅ SAMPLE FIREBASE STRUCTURE
-----------------------------------------------------------
Database
├── Users
│   ├── 101
│   │   ├── name: "Aman"
│   │   ├── department: "CSE"
│   │   └── ...
├── Attendance
│   ├── 101
│   │   ├── 2025-07-06: true

-----------------------------------------------------------
📌 NOTES
-----------------------------------------------------------
- Use clear front-facing face images for better accuracy
- Run EncodeGenerator.py again after adding new users

-----------------------------------------------------------
🧑‍💻 AUTHOR
-----------------------------------------------------------
Aman Chand  
GitHub: https://github.com/amanrudra01

-----------------------------------------------------------
⭐ Like this project? Star the repo and share with others!
-----------------------------------------------------------
