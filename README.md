# 🏏 IPL Player Next Innings Run Predictor (Flask Web App)

This project is a machine learning web application built using **Flask** that predicts how many runs an IPL batsman is likely to score in their next innings. The model is trained using IPL ball-by-ball data and historical player performance features.

---

## 🚀 Features

- Select any batsman from IPL history
- View their recent match stats
- Predict next innings run score using a trained **XGBoost model**
- Clean and responsive web interface (HTML + CSS)

---

## 🧠 Technologies Used

- Python 3
- Flask (Web Framework)
- XGBoost (Machine Learning Model)
- Pandas, NumPy (Data Handling)
- Jinja2 Templates (HTML rendering)

---

## 📁 Project Structure

ipl_predictor_flask/
├── app.py # Main Flask application
├── ipl_predictor.pkl # Trained XGBoost model
├── X_data.pkl # Historical player match data with features
├── feature_columns.pkl # Feature columns used during model training
├── templates/
│ └── index.html # Web interface template


---

## 🧪 How to Run Locally

### 1. Clone or download this repository

```bash
git clone https://github.com/your-username/ipl-run-predictor-flask.git
cd ipl-run-predictor-flask
