from src.model import model_pipeline

from typing import Union

from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
import io
from PIL import Image
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text:str
    image: UploadFile


@app.get("/",response_class=HTMLResponse)
def read_root():
    # Read the HTML content from your file (e.g., index.html)
    with open("/Users/anmolarora/Desktop/Galaxy/projects/crud-fastapi/src/templates/home.html", "r") as html_file:
        html_content = html_file.read()

    return html_content


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    # image = Image.open(image.file)
    
    result = model_pipeline(text, image)
    return {"answer":result}



@app.get("/result/")
def result(message: str):
    return message










# @app.post("/ask")

# def process_data(input_data: InputData):
#     try:
#         # Process the text
#         text = input_data.text

#         # Process the image
#         image_contents = input_data.image.file.read()
#         # Save the image or perform any other necessary actions

#         return {"message": "Data processed successfully!"}
#     except Exception as e:
#         return {"error": str(e)}
#     finally:
#         input_data.image.file.close()