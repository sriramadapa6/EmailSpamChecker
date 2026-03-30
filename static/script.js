function checkSpam() {
    const email = document.getElementById("email").value;
    const resultBox = document.getElementById("result");

    // 🛑 Empty check
    if (!email.trim()) {
        resultBox.innerText = "⚠️ Please enter email text";
        resultBox.style.color = "yellow";
        return;
    }

    // ⏳ Loading state
    resultBox.innerText = "Checking...";
    resultBox.style.color = "white";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(res => res.json())
    .then(data => {
        // 🎯 Show result
        if (data.result === "Spam") {
            resultBox.innerText = `🚨 Spam (${data.confidence}%)`;
        } else {
            resultBox.innerText = `✅ Safe (${data.confidence}%)`;
        }
        // 🎨 Color based on result
        if (data.result === "Spam") {
            resultBox.style.color = "#ff5252"; // red
        } else {
            resultBox.style.color = "#00e676"; // green
        }
    })
    .catch(err => {
        // ❌ Error handling
        resultBox.innerText = "Error checking email!";
        resultBox.style.color = "orange";
        console.error(err);
    });
}