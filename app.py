from flask import Flask, request, jsonify, render_template, redirect, session
import pickle
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        email TEXT
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
        cursor.execute("SELECT * FROM users WHERE username=?", (user,))
        result = cursor.fetchone()
        conn.close()

        # ❌ USER NOT FOUND
        if not result:
            return render_template("login.html", error="❌ User not found")

        # ❌ PASSWORD WRONG
        if pwd != result[2]:
            return render_template("login.html", error="❌ Password incorrect")

        # ✅ SUCCESS
        session["user"] = user
        return redirect("/")

    return render_template("login.html")

# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return jsonify({"error": "Login required"})

    data = request.json
    email = data["email"]

    transformed = vectorizer.transform([email])
    prediction = model.predict(transformed)[0]
    probability = model.predict_proba(transformed)[0][1]

    result = "Spam" if prediction == 1 else "Not Spam"
    confidence = round(probability * 100, 2)

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

    cursor.execute("""
        SELECT result, COUNT(*) 
        FROM history 
        WHERE user=? 
        GROUP BY result
    """, (session["user"],))
    stats = cursor.fetchall() or []

    cursor.execute("""
        SELECT email, result 
        FROM history 
        WHERE user=? 
        ORDER BY id DESC
    """, (session["user"],))
    history = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", stats=stats, history=history)

@app.route("/clear_history", methods=["POST"])
def clear_history():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history WHERE user=?", (session["user"],))
    
    conn.commit()
    conn.close()

    return redirect("/dashboard")

# ---------------- PROFILE ----------------
@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM users WHERE username=?", (session["user"],))
    result = cursor.fetchone()

    email = result[0] if result and result[0] else ""

    conn.close()

    return render_template("profile.html", user=session["user"], email=email)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

@app.route("/save_email", methods=["POST"])
def save_email():
    if "user" not in session:
        return redirect("/login")

    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET email=? WHERE username=?",
        (email, session["user"])
    )

    conn.commit()
    conn.close()

    return redirect("/profile")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
