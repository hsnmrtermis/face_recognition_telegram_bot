from fastapi import FastAPI, UploadFile, File, Form
import uvicorn
import uuid
import shutil
import os
from Database import Database

app = FastAPI()

@app.get('/')
def root():
    return {"Mesaj": "asdasd"}


@app.post('/person')
async def person_create(file: UploadFile, name= Form()):
    extension = os.path.splitext(file.filename)[1]
    path = os.getcwd() + '/faces/' 
    filename =  str(uuid.uuid4()) + extension
    
    db = Database().connect()
    db.cursor.execute("INSERT INTO people (name, path, file_name) VALUES (%s, %s, %s)", 
                      (name, path, filename));
    db.connection.commit()
    db.close()
    
    with open(path + filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "Message": "Person Created."
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)