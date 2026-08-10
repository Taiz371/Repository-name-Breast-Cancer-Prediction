# Breast Cancer Prediction

A machine learning project that predicts whether a breast tumor is **benign** or **malignant** using Python and scikit-learn. The project includes a Jupyter Notebook for model development and a Flask web application for making predictions through a browser interface.

> **Disclaimer:** This project is for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used to make healthcare decisions.

## Project Overview

The project follows a typical machine-learning workflow:

1. Load and inspect the breast cancer dataset.
2. Clean and prepare the data.
3. Select features for model training.
4. Split the data into training and testing sets.
5. Train a Logistic Regression classifier.
6. Evaluate the model on the test data.
7. Save the trained model.
8. Use Flask to provide a simple web interface for predictions.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- Bootstrap
- Git & GitHub

## Project Structure

```text
Breast-Cancer-Prediction/
├── Breast Cancer.ipynb
├── app.py
├── data.csv
├── model.pkl
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Model

The notebook uses **Logistic Regression** as the classification algorithm.

The test split in the notebook reports an accuracy of approximately **97.37%**. This value depends on the data split and preprocessing used in the notebook.

For a complete evaluation, accuracy should be considered together with metrics such as precision, recall, F1-score, and the confusion matrix.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Breast-Cancer-Prediction.git
cd Breast-Cancer-Prediction
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Jupyter Notebook

Start Jupyter:

```bash
jupyter notebook
```

Then open:

```text
Breast Cancer.ipynb
```

You can also open the notebook directly in VS Code if the Python and Jupyter extensions are installed.

## Run the Flask Application

After installing the dependencies:

```bash
python app.py
```

Open the local address shown by Flask in your browser.

## GitHub Workflow

After making changes:

```bash
git add .
git commit -m "Update breast cancer prediction project"
git push
```

## Future Improvements

- Add cross-validation.
- Include precision, recall, F1-score, and ROC-AUC.
- Improve input validation in the web application.
- Add automated tests.
- Improve the user interface.
- Add model explainability.
- Add a reproducible training pipeline.

## Author

**Your Name**

Replace `Your Name` with your name before publishing the repository.
