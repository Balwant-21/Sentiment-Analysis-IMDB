# 🎬 IMDB Movie Review Sentiment Analysis using NLP

## 📌 Project Overview

This project is a Machine Learning-based Sentiment Analysis system that classifies IMDB movie reviews as **Positive** or **Negative** using Natural Language Processing (NLP).

The project demonstrates the complete machine learning workflow, including text preprocessing, TF-IDF vectorization, model training using Logistic Regression, and prediction on custom movie reviews.

---

## 🎯 Objective

The objective of this project is to build a sentiment classification model that can automatically determine whether a movie review expresses a positive or negative sentiment.

---

## 📂 Dataset

- Dataset: IMDB Movie Reviews Dataset
- Total Reviews: 50,000
- Classes:
  - Positive
  - Negative

---

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- Machine Learning

---

## 📚 Libraries Used

- pandas
- numpy
- re (Regular Expressions)
- nltk
- scikit-learn
- matplotlib
- seaborn
- pickle

---

## ⚙️ Project Workflow

1. Load the IMDB dataset
2. Perform basic data exploration
3. Clean the text data
   - Convert text to lowercase
   - Remove HTML tags
   - Remove URLs
   - Remove numbers
   - Remove punctuation
   - Remove stopwords
4. Convert text into numerical features using TF-IDF Vectorization
5. Split the dataset into training and testing sets
6. Train a Logistic Regression model
7. Evaluate the model
8. Save the trained model and TF-IDF vectorizer
9. Predict sentiment for custom movie reviews

---

## 🤖 Machine Learning Model

- Feature Extraction: TF-IDF Vectorizer
- Classification Algorithm: Logistic Regression

---

## 📊 Model Performance

- Accuracy: **88.57%**

Evaluation Metrics:

- Accuracy Score
- Classification Report
- Confusion Matrix

---

## 📁 Project Structure

```
Sentiment-Analysis-PROJECT/
│
├── dataset/
│   └── IMDB Dataset.csv
│
├── models/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook/
│   └── Sentiment_Analysis.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-link>
```

### 2. Navigate to the project folder

```bash
cd Sentiment-Analysis-IMDB
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

---

## 💻 Example Prediction

Input:

```
This movie was absolutely amazing. I loved every moment of it.
```

Output:

```
Prediction: Positive 😊
```

Input:

```
Worst movie ever. Complete waste of time.
```

Output:

```
Prediction: Negative 😞
```

---

## 📈 Future Improvements

- Deploy the model using Streamlit or Flask
- Experiment with advanced NLP models
- Improve prediction accuracy using deep learning techniques

---

## 👨‍💻 Author

**Balwant Singh**

If you found this project helpful, feel free to ⭐ this repository.