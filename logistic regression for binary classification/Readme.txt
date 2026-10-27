# Student Placement Prediction

A machine learning web application that predicts whether a student is likely to be placed based on their **CGPA** and **IQ score**.

The project uses **Logistic Regression** for binary classification and **Flask** to provide a simple web interface for making predictions.

## Project Overview

The application takes two inputs from the user:

* Student CGPA
* Student IQ

The trained machine learning model then predicts one of two outcomes:

* **Student is Likely to be PLACED**
* **Student is NOT Likely to be PLACED**

## Technologies Used

* Python
* Flask
* NumPy
* Scikit-learn
* Logistic Regression
* HTML
* CSS
* Pickle

## Machine Learning Model

The project uses **Logistic Regression**, a classification algorithm used to predict categorical outcomes.

### Input Features

1. CGPA
2. IQ

### Target

The model predicts the student's placement status:

* `1` → Student is Likely to be PLACED
* `0` → Student is NOT Likely to be PLACED

## How the Application Works

```text
Student enters CGPA
        +
Student enters IQ
        ↓
       Flask
        ↓
Trained Logistic Regression Model
        ↓
    Prediction
        ↓
Placement Result
```

## Project Structure

```text
Student-Placement-Predictor/
│
├── app.py
├── BCModel.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Open the Project Folder

```bash
cd Student-Placement-Predictor
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## Example

If a student enters:

```text
CGPA: 8.5
IQ: 120
```

The model will process these values and return a placement prediction.

## Important Note

This application is an educational machine learning project. The prediction is based only on the features used to train the model and should not be considered a guarantee of actual placement.

## Author

**Atharv Dhobale**

B.Tech — Computer Science and Engineering (AI & ML)
