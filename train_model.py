import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Better dataset
data = {
    "text": [
        "Win money now",
        "Free iPhone offer",
        "Claim your prize urgently",
        "Send bank details to receive money",
        "Limited time discount offer",
        "Account will be suspended",
        "Click here to claim reward",

        "Hello friend how are you",
        "Meeting at 5pm",
        "Let's study together",
        "Project discussion tomorrow",
        "Please review the document"
    ],
    "label": [1,1,1,1,1,1,1, 0,0,0,0,0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model retrained ✅")