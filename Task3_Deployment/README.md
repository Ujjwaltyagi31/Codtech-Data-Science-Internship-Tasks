# 🏠 Task 3 – House Price Prediction with Flask Deployment | CodTech Data Science Internship

This project demonstrates an end-to-end machine learning pipeline for **house price prediction** using a **Linear Regression model**, deployed with a **Flask web application**.

---

## 📌 Objective

To build a complete data science solution involving:
- Data collection and preprocessing
- Model training and serialization
- Flask-based web deployment
- Real-time prediction via a user interface

---

## 🗃️ Dataset

As a substitute for the California Housing dataset, a similar synthetic regression dataset with 8 numerical features and 20,640 records was generated to simulate real-world housing features like:
- Median Income
- House Age
- Rooms per household
- Bedrooms per household
- Population
- Average Occupancy
- Latitude
- Longitude

---

## 🧪 Workflow

1. **Data Preparation**
   - Normalized using `StandardScaler`
   - Train-test split (80/20)

2. **Model Training**
   - Linear Regression from `scikit-learn`
   - Evaluation and export to `model.pkl`

3. **Flask Web Application**
   - Accepts 8 input features via HTML form
   - Sends data to model
   - Returns predicted house price

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** scikit-learn, Flask, joblib
- **Frontend:** HTML, CSS
- **Deployment:** Render.com (or local server)

---

## 📁 Project Structure
```bash
Task3_Deployment/
│
├── app.py                     # Flask app
├── model.pkl                  # Trained model (saved with joblib)
├── scaler.pkl
├── index.html                 # Input form UI
├── style.css                  # Webpage styling
├── prediction_script.py       # Model training
├── README.md                  # Project Documentation


---

## ▶️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/codtech-internship-tasks.git
   cd Task3_Deployment
