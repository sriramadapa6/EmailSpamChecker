# 📧 Email Spam Detection System

A full-stack web application that detects whether an email is **Spam or Not Spam** using **Machine Learning** along with rule-based filtering techniques.

---

## 🚀 Features

* 🔐 User Authentication (Login & Register)
* 🤖 Spam Detection using **Machine Learning Model**
* 📧 Keyword-Based Filtering (Fallback system)
* 📊 Dashboard with Pie Chart Analytics
* 📜 Email History Tracking
* 🎨 Modern UI (Glassmorphism Design)
* ⚡ Real-time Prediction with Confidence Score

---

## 🤖 Machine Learning Details

* **Algorithm Used:** Naive Bayes (MultinomialNB)
* **Text Processing:** TF-IDF Vectorization
* **Library:** Scikit-learn

### 🔍 ML Workflow

1. Collect dataset (spam / not spam emails)
2. Preprocess text (lowercase, remove noise)
3. Convert text → numerical using **TF-IDF**
4. Train model using **Naive Bayes**
5. Save model using `pickle`
6. Load model in Flask app
7. Predict user input in real-time

---

## 🛠️ Tech Stack

**Frontend:** HTML, CSS, JavaScript
**Backend:** Python (Flask)
**Machine Learning:** Scikit-learn
**Database:** SQLite

---

## 📂 Project Structure

```id="n1e93r"
EmailSpamChecker/
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── database.db
│
├── templates/
├── static/
```

---

## ▶️ Run Locally

```bash id="2m2f0n"
pip install flask scikit-learn
python app.py
```

👉 Open: http://127.0.0.1:5000

---

## 📊 Example

**Input:**

```id="njzn0u"
Win a FREE gift card now! Click here!
```

**Output:**

```id="9xib0u"
🚨 Spam (92%)
```

---

## 📌 Note

* `model.pkl` → trained ML model
* `vectorizer.pkl` → TF-IDF transformer
* `database.db` auto-created

---

## 📈 Future Improvements

* Deep Learning (LSTM / BERT)
* Gmail API integration
* Real-time email scanning
* Better dataset training

---

## 👨‍💻 Author

**Sriram Adapa**
