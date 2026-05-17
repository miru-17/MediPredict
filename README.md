MediPredict – Health Risk Prediction Web Application

Overview

MediPredict is an ML-based Health Risk Prediction Web Application developed to help users identify possible health risks based on the symptoms they experience. The application provides a simple and user-friendly platform where users can enter their symptoms and receive preliminary disease predictions along with basic health recommendations.

The main objective of this project is to improve accessibility to healthcare information and encourage users to seek timely medical attention. MediPredict acts as a supportive healthcare assistant by offering quick predictions and spreading awareness about possible medical conditions.

---

Features

* User Registration and Login Authentication
* Secure Password Encryption
* Symptom-Based Disease Prediction
* ML-Based Health Risk Analysis
* Health Recommendations and Guidance
* User-Friendly Dashboard Interface
* PDF Report Generation
* MongoDB Database Integration
* Responsive Frontend Design
* Session Management using Flask

Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask Framework

## Database

* MongoDB

## Machine Learning

* Random Forest Algorithm
* Scikit-learn
* Pandas
* NumPy

## Additional Tools

* PDFKit
* Werkzeug Security
* Git & GitHub

---

# System Architecture

1. User enters symptoms through the web interface.
2. Flask backend processes the input data.
3. Machine Learning model analyzes symptoms.
4. Random Forest algorithm predicts possible diseases.
5. Prediction results and health recommendations are displayed.
6. User can generate and download a PDF report.

---

# Project Modules

## 1. Authentication Module

* User Registration
* Login System
* Password Hashing
* Session Handling

## 2. Symptom Analysis Module

* Collects symptoms entered by the user
* Processes symptom data for prediction

## 3. Prediction Module

* Uses Random Forest Machine Learning Algorithm
* Predicts possible diseases based on symptoms

## 4. Recommendation Module

* Displays basic health guidance
* Encourages users to consult healthcare professionals

## 5. Report Generation Module

* Generates downloadable PDF reports for prediction results

---

# Why Random Forest?

Random Forest is used in this project because:

* It provides high prediction accuracy.
* Works efficiently with large datasets.
* Reduces overfitting compared to Decision Trees.
* Handles multiple symptoms and conditions effectively.
* Produces reliable results for classification tasks.

---

# Why Flask?

Flask is used as the backend framework because:

* It is lightweight and easy to integrate.
* Supports rapid web application development.
* Easily connects Machine Learning models with web applications.
* Provides simple routing and session management.
* Flexible for both small and large projects.

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/medipredict.git
```

## Step 2: Navigate to the Project Directory

```bash
cd medipredict
```

## Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

## Step 4: Start MongoDB Server

Make sure MongoDB is installed and running locally.

```bash
mongod
```

## Step 5: Run the Flask Application

```bash
python app.py
```

## Step 6: Open in Browser

```text
http://127.0.0.1:5000
```

---
# Future Enhancements

* Integration with AI Chatbot for Health Assistance
* Doctor Appointment Booking System
* Real-Time Health Monitoring
* Multi-Language Support
* Cloud Deployment
* Email Notification System
* Advanced Medical Recommendation Engine
* Mobile Application Integration

---

# Advantages of the Project

* Provides quick preliminary health analysis
* Easy-to-use interface for all users
* Helps increase health awareness
* Saves time for initial health assessment
* Accessible from anywhere through a web browser

---

# Limitations

* Predictions are based only on trained datasets.
* Does not replace professional medical diagnosis.
* Accuracy depends on symptom input quality.

---

# Conclusion

MediPredict is a smart healthcare support system that combines Web Development and Machine Learning to provide users with preliminary health risk predictions. The project demonstrates the practical implementation of Artificial Intelligence in the healthcare field while focusing on accessibility, usability, and user awareness.

---

# Contributors

* K. Mirudhula

---

# License

This project is developed for educational and learning purposes.

---

# Contact

For any queries or suggestions:

* LinkedIn: [https://www.linkedin.com/in/mirudhula-kathirvel-64507a296](https://www.linkedin.com/in/mirudhula-kathirvel-64507a296)
* GitHub: [https://github.com/](https://github.com/)
