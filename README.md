# 📧 Email Spam Detection System

A full-stack web application that detects whether an email is **Spam or Not Spam** using rule-based filtering techniques.

---

## 🚀 Features

* 🔐 User Authentication (Login & Register)
* 📧 Spam Detection using keyword-based filtering
* 📊 Dashboard with Pie Chart Analytics
* 📜 Email History Tracking
* 🎨 Modern UI (Glassmorphism Design)

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask)
* **Spam Detection**: Rule-Based Filtering (Keyword Matching)
* **Database**: SQLite

---

## 🧠 How It Works

The system analyzes email content and checks for spam-related keywords such as:

* "free"
* "win"
* "urgent"
* "offer"
* "click"
* "bank"

If these keywords are found, the email is classified as **Spam**, otherwise **Not Spam**.

---

## 📂 Project Structure

```
EmailSpamChecker/
│
├── app.py
├── templates/
├── static/
├── model.pkl (optional)
├── vectorizer.pkl (optional)
```

---

## ▶️ Run Locally

```bash
pip install flask
python app.py
```

Open:
http://127.0.0.1:5000

---

## 📌 Note

**database.db will be automatically created when you run the application for the first time.**

---

## 📊 Example

Input:
"Get FREE iPhone now!!!"

Output:
🚨 Spam

---

## 📈 Future Improvements

* Add Machine Learning model for better accuracy
* Gmail API integration
* Advanced spam pattern detection

---

## 👨‍💻 Author

Sriram Adapa
