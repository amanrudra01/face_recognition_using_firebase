# 🔐 Face Recognition using Firebase

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-RealTime-blue?style=flat-square&logo=opencv)
![Firebase](https://img.shields.io/badge/Firebase-Backend-yellow?style=flat-square&logo=firebase)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=flat-square)

A Python-based real-time **face recognition system** integrated with **Firebase Realtime Database**.  
It encodes faces, detects individuals through a webcam, and stores/retrieves user data from Firebase.

---

## ✨ Features

- 🎥 Real-time face detection via webcam
- 🧠 Face encoding using `face_recognition`
- 💾 Pickle-based face encoding storage (`EncodeFile.p`)
- ☁️ Firebase Realtime Database integration
- 🧑‍💼 User data management (name, ID, department, etc.)
- 📸 Visual face annotations on webcam feed

> 🔮 **Future Enhancement**  
> ➤ Automatic attendance logging in Firebase with timestamps

---

## 🧰 Tech Stack

| Technology      | Purpose                     |
|----------------|-----------------------------|
| `Python 3`      | Core Programming Language   |
| `face_recognition` | Face encoding & recognition |
| `OpenCV`        | Webcam stream & annotations |
| `Firebase Admin SDK` | Cloud integration       |
| `Pickle`         | Serialization of encodings |

---

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

- Save the JSON file as `serviceAccountKey.json` in the project root

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
├── Students
│   ├── 101
│   │   ├── name: "Aman"
│   │   ├── department: "CSE"
│   │   └── ...

```
Extended Structure with Attendance Logging
> For Future Enhancement
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
