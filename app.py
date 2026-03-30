from flask import Flask, request, jsonify, render_template, redirect, session
import pickle
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- DATABASE SETUP ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        email TEXT,
        result TEXT,
        user TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pwd))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
        result = cursor.fetchone()
        conn.close()

        if result:
            session["user"] = user
            return redirect("/")

    return render_template("login.html")

# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")

# ---------------- PREDICT (IMPROVED) ----------------
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return jsonify({"error": "Login required"})

    data = request.json
    email = data["email"]

    email_lower = email.lower()

    # 🔥 KEYWORD BOOST (important)
    spam_keywords = [
        "win", "free", "urgent", "prize", "offer",
        "click", "reward", "money", "lottery", "bank"
    ]

    if any(word in email_lower for word in spam_keywords):
        result = "Spam"
        confidence = 90.0
    else:
        transformed = vectorizer.transform([email])
        pred = model.predict(transformed)[0]
        prob = model.predict_proba(transformed)[0][1]

        result = "Spam" if pred == 1 else "Not Spam"
        confidence = round(prob * 100, 2)

    # Save history
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO history (email, result, user) VALUES (?, ?, ?)",
        (email, result, session["user"])
    )
    conn.commit()
    conn.close()

    return jsonify({
        "result": result,
        "confidence": confidence
    })

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Stats
    cursor.execute("""
        SELECT result, COUNT(*) 
        FROM history 
        WHERE user=? 
        GROUP BY result
    """, (session["user"],))
    stats = cursor.fetchall() or []

    # History
    cursor.execute("""
        SELECT email, result 
        FROM history 
        WHERE user=? 
        ORDER BY id DESC
    """, (session["user"],))
    history = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", stats=stats, history=history)

# ---------------- PROFILE ----------------
@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")
    return render_template("profile.html", user=session["user"])

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)