from fastapi import FastAPI, UploadFile, Form, File
from digit_detecter import Recognizer
import shutil, os

app = FastAPI()

@app.get("/recognize/{path}")
async def read_item(path):
    recognizer = Recognizer(path= path)
    num = recognizer.recognize()
    return {"result ": str(num) }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), uuid : str = Form(...)):
    try:
        with open(f"{uuid}.png", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)  
            path = f"{uuid}.png"
            recognizer = Recognizer(path=path)
            num = recognizer.recognize()

            os.remove(path= path)
            return {"expression" : str(num)}

    except:
        return {"expression" : "unknown"}        
    

