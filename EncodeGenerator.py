import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, db, storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://trashbotfacerec-default-rtdb.firebaseio.com/",
    'storageBucket': "trashbotfacerec.appspot.com"
})

# importing the student image into a list
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in PathList:
    # Only consider .png files
    if not path.lower().endswith('.png'):
        print(f"Skipping non-png file: {path}")
        continue

    img = cv2.imread(os.path.join(folderPath, path))
    if img is None:
        print(f"Error loading image: {path}")
        continue  # Skip this image if it's not loaded correctly
    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])  # Store student ID without extension

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


# print(studentIds)


def findEncodings(imagesList):
    encodList = []
    for image in imagesList:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        encode = face_recognition.face_encodings(image)[0]  # Encode the image
        encodList.append(encode)

    return encodList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)
print("Encoding Complete")

# Saving the encodings into a file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved.")