from cv2 import imshow, imwrite
import face_recognition as fr
import cv2 as cv


path = "C:/Users/The path where you place it/FaceRecognitionWindows/faces/"
path1 = "C:/Users/The path where you place it/"

face = fr.load_image_file(path + "image.jpg")
encoding = fr.face_encodings(face) [0]


while True:
    camPort = 0
    cam = cv.VideoCapture(camPort)
    result, image = cam.read()
    if result:
        cv.imwrite("faceDetected.jpg", image)
        cv.imshow("Face Detected", image)

        findFace = fr.load_image_file(path1 + "faceDetected.jpg")
        encodingFace = fr.face_encodings(image) [0]

        match = fr.compare_faces([face], findFace[0])
        if match:
            imshow("Face", image)
            print("Match")
            break
        else :
            print("No Match")