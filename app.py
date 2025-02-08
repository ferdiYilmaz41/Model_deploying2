from fastapi import FastAPI
from predict import predict_img,load_model,read_image,pre_process_image
from fastapi import UploadFile, File
import uvicorn

app = FastAPI()

@app.get("/docs")
async def geetNamedeneme():
    return {"message": "Hello Ferdi!"}

@app.post("/APi/predict")
async def predict_uploaded_image(file: bytes = File(...)):
    model= load_model()
    print("Model loaded")
    image = read_image(file)
    print("Image read")
    img_array = pre_process_image(image)
    print("Image processed")
    result = predict_img(img_array, model)
    print("Prediction done")
    print(result)
    return result

# if __name__ == "__main__":
    
#     uvicorn.run(app, host="127.0.0.1", port=7001)