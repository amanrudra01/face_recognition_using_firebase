import os
import pickle
import cvzone
import cv2
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials, db, storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "DATABASE_URL",
    'storageBucket': "STORAGE_BUCKET"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackGround = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
print("Loading Encoded File...") 
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

modeType = 1
counter = 0
id = -1
imgStudent = []

# Define the threshold for an unknown face
faceDisThreshold = 0.6

while True:
    success, img = cap.read()

    faceCurFrame = face_recognition.face_locations(img)
    encodeCurFrame = face_recognition.face_encodings(img, faceCurFrame)

    imgBackGround[162:162 + 480, 55:55 + 640] = img
    imgBackGround[44:44 + 633, 808:808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < faceDisThreshold:
            # Known face
            y1, x2, y2, x1 = faceLoc
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackGround = cvzone.cornerRect(imgBackGround, bbox, rt=0)
            id = studentIds[matchIndex]

            if counter == 0:
                counter = 1

        else:
            # Unknown face
            print("Unknown Person Detected")
            y1, x2, y2, x1 = faceLoc
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackGround = cvzone.cornerRect(imgBackGround, bbox, rt=0, colorR=(0, 0, 255))  # Red for unknown
            id = "Unknown"
            counter = 1

    if counter != 0:
        if counter == 1:
            if id != "Unknown":
                # Fetch student data
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                # Fetch student image
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)


            else:
                # Fetch unknown image
                blob = bucket.get_blob(f'Unknown/unknown.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                studentInfo = {'name': 'Unknown', 'id': 'N/A'}

        cv2.putText(imgBackGround, str(studentInfo['name']), (1006, 550), cv2.FONT_HERSHEY_COMPLEX, .4, (255, 255, 255), 1)
        cv2.putText(imgBackGround, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255), 1)
        imgBackGround[175:175 + 216, 909:909 + 216] = imgStudent

    cv2.imshow("Camera", img)
    cv2.imshow("Face Recognition", imgBackGround)

    cv2.waitKey(1)


