import face_recognition
import os
import cv2
import numpy as np
import math
from Database import Database
from model.UserProperty import UserProperty
import helper
import uuid

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    know_face_names = []
    cropped_faces = []
    
    
    def __init__(self) -> None:
        pass
    
    def __del__(self) -> None:
        self.clear_properties()
    
    
    def encode_faces(self):
        db: Database = Database().connect()
        users = db.get_users()
        for user in users:
            face_image = face_recognition.load_image_file(user[UserProperty.PATH.value] + user[UserProperty.FILENAME.value])
            face_encoding = face_recognition.face_encodings(face_image)[0]
    
            self.known_face_encodings.append(face_encoding)
            self.know_face_names.append(user[UserProperty.NAME.value])
        
    def run_recognition(self, image_path):
        self.encode_faces()
        image = face_recognition.load_image_file(image_path)
        
        self.face_locations = face_recognition.face_locations(image)
        self.face_encodings = face_recognition.face_encodings(image, self.face_locations)
        
        self.face_names = []
        
        for face_encoding in self.face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Bilinmeyen Kişi"
            confidence = "???"
            
            face_distances  = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name = self.know_face_names[best_match_index]
                confidence = helper.face_confidence(face_distances[best_match_index])
                
            self.face_names.append(f"Bulunan Kişi: {name}, Benzerlik Oranı: {confidence}")
                
    
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            img = cv2.imread(image_path)
            cropped_image = img[top:bottom, left:right]
            image_name = os.getcwd() + '/cropped_faces/'  + str(uuid.uuid4()) + '.jpg'
            cv2.imwrite(image_name, cropped_image)
            self.cropped_faces.append(image_name)
        
        
        
    def clear_properties(self):
        self.face_locations.clear()
        self.face_encodings.clear()
        self.face_names.clear()
        self.known_face_encodings.clear()
        self.know_face_names.clear()
        self.cropped_faces.clear()