// 🔵 Update semicircle progress
function updateProgress(percent) {
    const path = document.getElementById("progressPath");
    const text = document.getElementById("percent");

    const total = 282;
    const offset = total - (percent / 100) * total;

    path.style.strokeDashoffset = offset;
    text.innerText = percent + "%";
}

function checkSpam() {
    const email = document.getElementById("email").value;
    const resultBox = document.getElementById("result");

    // 🛑 Empty check
    if (!email.trim()) {
        resultBox.innerText = "⚠️ Please enter email text";
        resultBox.style.color = "yellow";
        return;
    }

    // =========================
    // 🔍 LEFT PANEL ANALYSIS
    // =========================
    const text = email.toLowerCase();

    // Words count
    const words = text.split(/\s+/).length;
    document.getElementById("words").innerText = words;

    // Spam words count
    const spamList = ["win", "free", "offer", "money", "click", "urgent", "prize"];
    let spamCount = 0;
    spamList.forEach(word => {
        if (text.includes(word)) spamCount++;
    });
    document.getElementById("spamWords").innerText = spamCount;

    // Links count
    const linkCount = (text.match(/http|www/g) || []).length;
    document.getElementById("links").innerText = linkCount;

    // Emojis count
    const emojiCount = (text.match(/[\u{1F600}-\u{1F6FF}]/gu) || []).length;
    document.getElementById("emojis").innerText = emojiCount;

    // =========================
    // ⏳ LOADING ANIMATION
    // =========================
    resultBox.innerText = "Checking...";
    resultBox.style.color = "white";

    let fake = 0;
    const interval = setInterval(() => {
        if (fake < 90) {
            fake += 5;
            updateProgress(fake);
        }
    }, 100);

    // =========================
    // 🤖 ML PREDICTION
    // =========================
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(res => res.json())
    .then(data => {
        clearInterval(interval);

        // 🎯 Final ML accuracy
        updateProgress(data.confidence);

        const path = document.getElementById("progressPath");

        // 🎨 COLOR BASED ON RESULT
        if (data.result === "Spam") {
            resultBox.innerText = `🚨 Spam (${data.confidence}%)`;
            resultBox.style.color = "#ff5252";

            path.style.stroke = "#ff5252"; // 🔴 RED
        } else {
            resultBox.innerText = `✅ Safe (${data.confidence}%)`;
            resultBox.style.color = "#00e676";

            path.style.stroke = "#00e676"; // 🟢 GREEN
        }
    })
    .catch(err => {
        clearInterval(interval);
        resultBox.innerText = "Error checking email!";
        resultBox.style.color = "orange";
        console.error(err);
    });
}
