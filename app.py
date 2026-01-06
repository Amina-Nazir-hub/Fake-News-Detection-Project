from flask import Flask, render_template, request
import pickle
import re
import string

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("final_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\n", " ", text)
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        news = request.form["news"]
        news = clean_text(news)

        vector = vectorizer.transform([news])
        result = model.predict(vector)[0]

        if result == 1:
            prediction = "Real News"
        else:
            prediction = "Fake News"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
