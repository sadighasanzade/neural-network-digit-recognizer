from fastapi import FastAPI
from digit_detecter import Recognizer

app = FastAPI()

@app.get("/recognize/{path}")
async def read_item(path):
    recognizer = Recognizer(path= path)
    num = recognizer.recognize()
    return {"result ": str(num) }

