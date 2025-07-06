# Face Recognition using Firebase

A Python-based face recognition system integrated with Google Firebase for storing user data and attendance. This project encodes face images, recognizes individuals in real-time via webcam, and updates Firebase with attendance logs and user details.
---
## 🔧 Features

- Face recognition from webcam stream
- Encodes face data using `face_recognition` library
- Stores face encodings in a pickle file
- Firebase Realtime Database integration for:
  - Storing attendance records
  - Managing user profiles (name, ID, etc.)
- Real-time detection with face annotations on the video feed
---
## 🛠️ Technologies Used

- Python 3
- [face_recognition](https://github.com/ageitgey/face_recognition)
- OpenCV
- Firebase Admin SDK
- Pickle (for encoding storage)

## 📁 Project Structure
```
.
├── AddDataToDatabase.py     # Script to add user metadata to Firebase
├── EncodeGenerator.py       # Generates encodings from images and saves them in a pickle file
├── EncodeFile.p             # Serialized face encodings
├── main.py                  # Main script for real-time face recognition and Firebase attendance
├── Images/                  # Folder containing user images (named as <ID>.jpg/png)
└── README.md
```
---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/amanrudra01/face_recognition_using_firebase.git
cd face_recognition_using_firebase
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
#### If requirements.txt is missing, manually install:

```bash
pip install face_recognition opencv-python firebase-admin
```

### 3. Setup Firebase
Go to Firebase Console

- Create a new project

- Go to Project Settings > Service Accounts > Generate new private key

- Save the JSON file as firebase_config.json in the project root

- Ensure your Firebase Realtime Database is enabled

### 4. Add Images for Encoding

- Place face images in the Images/ folder

- Image file name must follow the format: <ID>.jpg or <ID>.png

### 5. Encode Images
```bash

python EncodeGenerator.py
```
This generates EncodeFile.p containing face encodings.

### 6. Add User Metadata to Firebase

```bash
python AddDataToDatabase.py
```
Ensure it matches the names/IDs used in image files.

### 7. Run the Face Recognition System
```bash
python main.py
```
This will start the webcam, recognize faces, and mark attendance in Firebase.


## ✅ Example Firebase Structure

```
Database
├── Users
│   ├── 101
│   │   ├── name: "Aman"
│   │   ├── department: "CSE"
│   │   └── ...
├── Attendance
│   ├── 101
│   │   ├── 2025-07-06: true

```

📌 Notes
All images must be clear frontal faces for accurate recognition.
Encoding must be regenerated if new users are added.


🧑‍💻 Author
Aman Chand
