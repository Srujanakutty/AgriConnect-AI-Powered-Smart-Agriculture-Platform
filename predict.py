import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("model/disease_model.h5")

classes = [
"Apple Black Rot",
"Apple Healthy",
"Grape Black Rot",
"Corn Common Rust",
"Potato Early Blight",
"Potato Late Blight",
"Tomato Early Blight",
"Tomato Late Blight"
]

def predict_disease(img_path):

    img = image.load_img(img_path,target_size=(224,224))

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array,axis=0)

    img_array = img_array/255.0

    prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction)

    disease_name = classes[predicted_index]

    confidence = float(np.max(prediction))

    return disease_name,confidence