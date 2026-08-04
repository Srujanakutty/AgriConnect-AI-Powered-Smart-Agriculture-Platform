# 🌾 AgriConnect – AI Powered Smart Agriculture Platform

> An AI-powered web application that helps farmers detect crop diseases using Deep Learning and provides crop advisory, real-time weather updates, and a farmer marketplace.

---

## 📖 Overview

AgriConnect is an AI-powered smart agriculture platform developed to help farmers identify crop diseases at an early stage using the MobileNetV2 deep learning model. The platform combines crop disease detection, crop advisory, weather information, and a farmer marketplace into a single web application.

---

## ✨ Features

- 🌿 AI-Based Crop Disease Detection
- 🧠 MobileNetV2 Deep Learning Model
- 📷 Leaf Image Upload & Disease Prediction
- 🌱 Crop Advisory
- 🌦️ Real-Time Weather Information
- 🛒 Farmer Marketplace
- 💾 SQLite Database
- 💻 Responsive Web Application

---

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Artificial Intelligence
- TensorFlow
- Keras
- MobileNetV2
- OpenCV
- NumPy

### Database
- SQLite

### API
- OpenWeather API

## Model

The trained MobileNetV2 model (`disease_model.h5`) is not included in this repository because it exceeds GitHub's file size limit. You can train the model using `train_model.py` or place the trained model inside the `model/` directory.

The trained model (`disease_model.h5`) is not included in this repository because it exceeds GitHub's maximum file size limit.

To use this project:

1. Place the trained model file inside this folder as:

```
model/disease_model.h5
```

2. Or train a new model using:

```
python train_model.py
```

---
## Dataset

The complete training dataset is not included in this repository.

A small sample of leaf images is provided for demonstration purposes. To train the model from scratch, replace the sample dataset with the complete dataset while maintaining the same folder structure.

## 📂 Project Structure

```text
AgriConnect-AI-Powered-Smart-Agriculture-Platform
│
├── app.py
├── predict.py
├── train_model.py
├── create_db.py
├── clear_db.py
├── check_db.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
├── model/
├── static/
├── templates/
├── utils/
└── screenshots/
```

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/AgriConnect-AI-Powered-Smart-Agriculture-Platform.git

cd AgriConnect-AI-Powered-Smart-Agriculture-Platform

pip install -r requirements.txt

python app.py
```

---

## 📸 Screenshots

- Home Page
- Crop Disease Detection
- Prediction Result
- Weather Information
- Farmer Marketplace

---

## 🔮 Future Enhancements

- Mobile Application
- Multi-language Support
- Live Market Price Integration
- AI Chatbot for Farmers
- Cloud Deployment

---

## 👩‍💻 Author

**K. Srujana**

B.Tech – Computer Science and Engineering

---

## 📄 License

This project is licensed under the MIT License.
