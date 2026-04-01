import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "text": [
        "Win money now", "Free iPhone offer", "Claim your prize urgently",
        "Click here to win cash", "Limited offer hurry up",
        "You have won lottery", "Earn money fast", "Bank alert update details",

        "Hi how are you", "Meeting at 5pm", "Let's work on project",
        "Call me later", "Send me notes", "Lunch tomorrow?",
        "Project submission deadline", "Team meeting today"
    ],
    "label": [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0,0]
}

df = pd.DataFrame(data)

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# ---------------- Logistic Regression ----------------
lr = LogisticRegression()
lr.fit(X, y)
lr_pred = lr.predict(X)
lr_acc = accuracy_score(y, lr_pred)

# ---------------- Naive Bayes ----------------
nb = MultinomialNB()
nb.fit(X, y)
nb_pred = nb.predict(X)
nb_acc = accuracy_score(y, nb_pred)

# ---------------- Choose Best Model ----------------
if lr_acc >= nb_acc:
    best_model = lr
    best_name = "Logistic Regression"
    best_acc = lr_acc
else:
    best_model = nb
    best_name = "Naive Bayes"
    best_acc = nb_acc

# Save everything
pickle.dump(best_model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump({"model": best_name, "accuracy": best_acc}, open("info.pkl", "wb"))

print(f"Best Model: {best_name}")
print(f"Accuracy: {best_acc * 100:.2f}%")
