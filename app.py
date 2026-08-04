from flask import Flask, render_template, request
import os
import sqlite3
import requests

from predict import predict_disease
from utils.crop_advisory import recommend_crop

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
DATABASE = "database/products.db"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

API_KEY = "8b8fff71dc1e73a2b4521f8719032372"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==============================
# HOME
# ==============================

@app.route('/')
def home():
    return render_template("home.html")


# ==============================
# DISEASE REMEDIES DATA
# ==============================

remedies = {

"Tomato Early Blight":
"Spray Mancozeb fungicide every 7 days and remove infected leaves.",

"Tomato Late Blight":
"Apply Copper based fungicide and improve air circulation.",

"Tomato Leaf Mold":
"Use Chlorothalonil fungicide and avoid overhead watering.",

"Tomato Bacterial Spot":
"Use copper spray and remove infected plants.",

"Tomato Septoria Leaf Spot":
"Apply fungicide and remove infected leaves.",

"Tomato Yellow Leaf Curl Virus":
"Control whiteflies using neem oil spray and remove infected plants.",

"Healthy":
"No disease detected. Maintain proper irrigation and balanced nutrients."

}


# ==============================
# DISEASE DETECTION
# ==============================

@app.route('/disease', methods=['GET','POST'])
def disease():

    if request.method == "POST":

        file = request.files['image']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        disease, confidence = predict_disease(filepath)

        # get remedy for predicted disease
        remedy = remedies.get(
            disease,
            "Consult an agricultural expert for proper treatment."
        )

        return render_template(
            "result.html",
            disease=disease,
            confidence=confidence,
            remedy=remedy
        )

    return render_template("disease.html")


# ==============================
# CROP ADVISORY
# ==============================

@app.route('/advisory', methods=['GET','POST'])
def advisory():

    crops=None

    if request.method=='POST':

        soil=request.form['soil']
        season=request.form['season']

        recommendations={

        ('alluvial','kharif'):['Rice','Maize','Sugarcane'],
        ('alluvial','rabi'):['Wheat','Mustard','Barley'],
        ('alluvial','zaid'):['Watermelon','Cucumber','Vegetables'],

        ('black','kharif'):['Cotton','Soybean','Sorghum'],
        ('black','rabi'):['Wheat','Chickpea','Sunflower'],
        ('black','zaid'):['Vegetables','Groundnut','Maize'],

        ('red','kharif'):['Millets','Groundnut','Cotton'],
        ('red','rabi'):['Wheat','Pulses','Mustard'],
        ('red','zaid'):['Vegetables','Watermelon','Cucumber'],

        ('laterite','kharif'):['Tea','Coffee','Rubber'],
        ('laterite','rabi'):['Cashew','Pulses','Vegetables'],
        ('laterite','zaid'):['Banana','Pineapple','Coconut'],

        ('loamy','kharif'):['Rice','Maize','Cotton'],
        ('loamy','rabi'):['Wheat','Barley','Mustard'],
        ('loamy','zaid'):['Vegetables','Watermelon','Cucumber'],

        ('sandy','kharif'):['Groundnut','Millet','Maize'],
        ('sandy','rabi'):['Mustard','Barley','Gram'],
        ('sandy','zaid'):['Watermelon','Cucumber','Vegetables']

        }

        crops=recommendations.get((soil,season),['Rice','Maize','Vegetables'])

    return render_template("advisory.html",crops=crops)


# ==============================
# WEATHER API FUNCTION
# ==============================

def get_weather(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        r = requests.get(url)

        data = r.json()

        if data.get("cod") != 200:
            return None

        weather = data["weather"][0]["description"]

        temp = data["main"]["temp"]

        humidity = data["main"]["humidity"]

        return {
            "temperature": temp,
            "humidity": humidity,
            "weather": weather
        }

    except:
        return None

# ==============================
# WEATHER PAGE
# ==============================

@app.route('/weather', methods=['GET','POST'])
def weather():


    weather_data = None

    if request.method == "POST":

        city = request.form["city"]

        weather_data = get_weather(city)

    return render_template("weather.html", weather=weather_data)


# ==============================
# MARKETPLACE ROLE
# ==============================

@app.route('/marketplace')
def marketplace():
    return render_template("marketplace_choice.html")


# ==============================
# FARMER PAGE
# ==============================

@app.route('/farmer', methods=['GET','POST'])
def farmer():

    success=False

    if request.method == "POST":

        crop = request.form["crop"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        farmer_name = request.form["farmer_name"]
        contact = request.form["contact"]
        location = request.form["location"]

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO products
        (crop_name, price, quantity, farmer_name, contact, location)
        VALUES (?,?,?,?,?,?)
        """,(crop, price, quantity, farmer_name, contact, location))

        conn.commit()
        conn.close()

        success=True

    return render_template("farmer.html",success=success)

# ==============================
# CONSUMER PAGE
# ==============================

@app.route('/consumer')
def consumer():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return render_template("consumer.html", products=products)


# ==============================
# RUN APP
# ==============================

if __name__ == "__main__":
    app.run(port=8000, debug=True)