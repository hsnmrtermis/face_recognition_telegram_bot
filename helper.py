from io import BytesIO 
import numpy as np
import cv2
import uuid
import os
import math
import requests
import shutil

def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance)  / (range * 2.0)
    
    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'
        
async def savePhoto(file):
    path = os.getcwd() + '/permanents/'
    randomName = str(uuid.uuid4())
    fileName = randomName + '.jpg'
    fullpath = path + fileName
    image = await loadMemoryPhoto(file)
    cv2.imwrite(fullpath , image)
    return fullpath

async def loadMemoryPhoto(file):
    byteArrays = await file.download_as_bytearray()
    f = BytesIO(byteArrays)
    file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
    return cv2.imdecode(file_bytes,  cv2.IMREAD_COLOR)

def sendPhoto(path):
    token = "TOKEN GELECEK"
    chatId = "CHAT ID GELECEK"
    url = f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={chatId}"
    file = open(path, 'rb')
    files = {"photo": file}
    requests.post(url, files=files)
    
    
def removeImageFolders():
    directories = ['cropped_faces', 'permanents']
    for directory in directories:
        path = os.getcwd() + '/' +directory + '/'
        shutil.rmtree(path, ignore_errors=False, onerror= None)
        try:
            os.mkdir(directory)
        except OSError as error:
            pass
        
        
def getCountOfDirectoryFiles(path):
    full_path = os.getcwd() + '/' + path 
    _, _, files = next(os.walk(full_path))
    return len(files)