# crop_recommendation
✅ README.md
markdown
Copy
Edit
# 🌾 Automatic Crop Recommendation System

This project is a **machine learning-powered web application** that recommends the most suitable crop to cultivate based on user-inputted soil and environmental parameters.

![App Screenshot](static/bg.jpg)

## 🚀 Features

- Predicts the best crop using soil nutrients and weather parameters
- User-friendly interface with a modern, farm-themed UI
- Built with Flask and a Random Forest classifier
- Real-time crop suggestion based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - Soil pH
  - Rainfall (mm)

## 🧠 Machine Learning

- Model: Random Forest Classifier
- Dataset: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) from Kaggle
- Trained with 80:20 train-test split
- Accuracy: ~98%

## 🖥️ Tech Stack

- Python
- Flask (Web Framework)
- HTML, CSS (Frontend)
- scikit-learn (Machine Learning)
- joblib (Model Persistence)

## 📁 Folder Structure

├── app.py # Flask application ├── train_model.py # ML model training script ├── crop_model.pkl # Trained ML model ├── dataset.csv # Kaggle dataset ├── templates/ │ ├── index.html │ └── result.html ├── static/ │ ├── style.css │ ├── bg.jpg # Background image │ └── crops/ # Crop images (e.g., rice.png)

bash
Copy
Edit

## 📸 UI Screenshots

### Home Page
![Home Page](screenshots/homepage.png)

### Result Page
![Result Page](screenshots/result.png)

> *(Add screenshots to `/screenshots/` folder and update these paths)*

## ✅ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
   cd crop-recommendation-system
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Train the model:

bash
Copy
Edit
python train_model.py
Run the app:

bash
Copy
Edit
python app.py
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:5000
🏁 Future Enhancements
Add fertilizer suggestions

Weather API integration for live data

Multi-language support for farmers

🧑‍💻 Developed By
Berlin
B.Tech Artificial Intelligence & Machine Learning

📬 Feel free to fork, contribute or give this project a ⭐ if you found it useful!

yaml
Copy
Edit

---

Let me know if you want me to generate a ZIP with:
- All code
- Background image placeholders
- Crop icons
- `README.md`

Would you like that?
