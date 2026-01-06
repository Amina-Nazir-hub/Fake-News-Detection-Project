# Fake News Detection Using Machine Learning

## Project Overview

Fake news has become a major challenge in the digital age, especially on social media platforms where misleading information spreads rapidly. This project focuses on detecting fake news articles using machine learning techniques by analyzing the textual content of news data.

The system classifies news as **Fake** or **Real** based on patterns learned from previously labeled articles.

---

## Objectives

- Understand the problem of fake news and its impact  
- Preprocess and analyze textual news data  
- Build and evaluate machine learning models  
- Compare model performance using standard metrics  

---

## Dataset

The dataset consists of news articles with the following attributes:

- Title of the news article  
- Text content  
- Label indicating Fake or Real news  

Text preprocessing is applied before training the models.

---

## Methodology

### 1. Data Preprocessing
- Lowercasing text  
- Removing punctuation and special characters  
- Stopword removal  
- Tokenization  

### 2. Feature Extraction
- TF-IDF Vectorization

### 3. Model Training
- Logistic Regression  
- Naive Bayes  
- Passive Aggressive Classifier  

### 4. Model Evaluation
- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  

---

## Tools and Technologies

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## Results and Findings

- The models successfully classify news into Fake and Real categories  
- Logistic Regression and Passive Aggressive Classifier performed well  
- TF-IDF proved effective for text feature extraction  

Detailed results are available in the notebooks.


---

## How to Run

1. Clone the repository  
2. Install the required dependencies  
3. Run the Jupyter Notebook or Python script  
4. Execute cells step by step to train and test the model  

---

## Future Improvements

- Apply deep learning models such as LSTM or BERT  
- Use real-time news data  
- Deploy the model as a web application  
- Improve accuracy with larger datasets  

---

## Author

**Amina Nazir**  
BS Software Engineering  
Fake News Detection Project


