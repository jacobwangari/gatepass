# Import necessary libraries
import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# Initialize Firebase app using service account key file
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://gate-pass-system-c8536-default-rtdb.firebaseio.com/",
    'storageBucket': "gate-pass-system-c8536.appspot.com"
})

# Define folder path for images
folderPath = 'Images'

# Get list of image paths in folder
pathList = os.listdir(folderPath)
print(pathList)

# Initialize empty lists for images and student IDs
imgList = []
studentIds = []

# Loop through image paths
for path in pathList:
    # Read image using OpenCV's imread function and append to image list
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    
    # Extract student ID from image filename and append to student ID list
    studentIds.append(os.path.splitext(path)[0])

    # Upload image to Firebase Storage
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Print image path and student ID for verification
    # print(path)
    # print(os.path.splitext(path)[0])

# Print list of student IDs for verification
print(studentIds)

# Define function to encode faces in a list of images
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # Convert image to RGB format using OpenCV's cvtColor function
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Encode face in image using face_recognition's face_encodings function
        encode = face_recognition.face_encodings(img)[0]
        
        # Append encoded face to list of encoded faces
        encodeList.append(encode)

    # Return list of encoded faces
    return encodeList



# Encode faces in image list using findEncodings function
encodeListKnown = findEncodings(imgList)

# Create list of encoded faces with their corresponding student IDs
encodeListKnownWithIds = [encodeListKnown, studentIds]

# Print message indicating encoding is complete
print("Encoding Complete")

# Save encoded faces with student IDs to file using pickle
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
