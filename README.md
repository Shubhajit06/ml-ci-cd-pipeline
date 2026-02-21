# 🚀 ML CI/CD Pipeline (MLOps Project)

## 📌 Project Overview
This project implements an end-to-end CI/CD pipeline for Machine Learning model training using GitHub Actions.  
Whenever new code is pushed to the repository, the pipeline automatically checks code quality, runs unit tests, trains the ML model, and uploads the trained model as an artifact.

The objective of this project is to demonstrate real-world MLOps practices such as automation, testing, and reproducibility in ML systems.

---

## 🎯 Objectives
- Automate ML workflow using CI/CD
- Maintain code quality
- Automatically test ML code
- Train model on every update
- Store trained model for download

---

## ⚙️ CI/CD Workflow
The pipeline triggers automatically on every push to the main branch.

### Steps performed:
1. Checkout repository code
2. Setup Python environment
3. Install dependencies
4. Run linting (flake8)
5. Run unit tests (pytest)
6. Train ML model
7. Save trained model
8. Upload model as artifact

---

## 🧠 Machine Learning Model
The project trains a Linear Regression model using the Scikit-Learn Diabetes dataset.

### Training Process
- Load dataset
- Split data into training & testing
- Train Linear Regression model
- Save trained model as `model.pkl`

---

## 🏗️ Project Structure

ml-ci-cd-pipeline/
│
├── .github/workflows/ci.yml
├── src/
│ ├── init.py
│ ├── model.py
│ └── train.py
│
├── tests/
│ └── test_model.py
│
├── Dockerfile
├── requirements.txt
├── .flake8
├── model.pkl
└── README.md

---

## 👤 Author
**Shubhajit Sarkar**

GitHub: https://github.com/Shubhajit06
