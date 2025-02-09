from io import BytesIO
import tensorflow 
import numpy as np
from PIL import Image
import os
import logging
from fastapi.encoders import jsonable_encoder


def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'model.h5')
    logging.debug(f"Loading model from path: {model_path}")
    
    model = tensorflow.keras.models.load_model(model_path)
    return model

def read_image(image_encoded: bytes):
    image = Image.open(BytesIO(image_encoded))
    return image

def pre_process_image(img: Image.Image):
    
    print(f"Image size: {img.size}") 
    img = img.convert('RGB')
    img = img.resize((30,30))
    print(f"Image size after resize: {img.size}") 
    img_array = np.array(img)/255
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def load_labels():
    classes = {
    0: 'Speed limit (20km/h)',
    1: 'Speed limit (30km/h)',
    2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)',
    4: 'Speed limit (70km/h)',
    5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)',
    7: 'Speed limit (100km/h)',
    8: 'Speed limit (120km/h)',
    9: 'No passing',
    10: 'No passing veh over 3.5 tons',
    11: 'Right-of-way at intersection',
    12: 'Priority road',
    13: 'Yield',
    14: 'Stop',
    15: 'No vehicles',
    16: 'Veh > 3.5 tons prohibited',
    17: 'No entry',
    18: 'General caution',
    19: 'Dangerous curve left',
    20: 'Dangerous curve right',
    21: 'Double curve',
    22: 'Bumpy road',
    23: 'Slippery road',
    24: 'Road narrows on the right',
    25: 'Road work',
    26: 'Traffic signals',
    27: 'Pedestrians',
    28: 'Children crossing',
    29: 'Bicycles crossing',
    30: 'Beware of ice/snow',
    31: 'Wild animals crossing',
    32: 'End speed + passing limits',
    33: 'Turn right ahead',
    34: 'Turn left ahead',
    35: 'Ahead only',
    36: 'Go straight or right',
    37: 'Go straight or left',
    38: 'Keep right',
    39: 'Keep left',
    40: 'Roundabout mandatory',
    41: 'End of no passing',
    42: 'End no passing veh > 3.5 tons'
    }
    return classes

def predict_img(img_array: np.ndarray, model: load_model):

    prediction = model.predict(img_array)
    confidence = round(float(np.max(prediction)*100),2)
    labels= load_labels()
    predicted_class = np.argmax(prediction)
    return jsonable_encoder({
            "predicted_class": labels[predicted_class],
            "confidence": confidence
        })