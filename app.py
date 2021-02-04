import base64
from io import BytesIO
import numpy as np
import uvicorn
from PIL import Image
from fastapi import FastAPI
from arcp import ARCP

from typing import List
import onnxruntime


async def get_data(image_path: str) -> List[int]:
    """
    Args:
        image_path (str): path of image to predict age

    Returns:
        data (list): list of image pixel of size (1, 224, 224, 3)
    """
    img = Image.open(BytesIO(base64.b64decode(image_path))).convert('RGB')
    # img = Image.frombytes("RGB", (224, 224))
    # img = Image.open(image_path)
    img = img.resize((224, 224))
    img1 = np.array(img)
    data = np.expand_dims(img1, axis=0)
    return list(data)


async def get_prediction(data: List[int]) -> int:
    """
    Args:
        data (list): list of image pixel of size (1, 224, 224, 3)

    Returns:
        age (int): returns predicted age
    """

    session = onnxruntime.InferenceSession('onnx_arcp_v1.onnx')
    input_name = session.get_inputs()[0].name
    result = session.run(None, {input_name: data})
    age = round(result[0][0][0])
    # print(f'{age=}')
    return age


app = FastAPI()


@app.get('/')
def welcome():
    return 'Welcome to My API'


@app.post('/predict')
async def predict(data: ARCP):
    data = data.dict()
    # print(data)
    image_name = data['data']
    dataset = await get_data(image_name)
    prediction = await get_prediction(dataset)
    return {'predicted_age': prediction}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
