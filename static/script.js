/* ===== BODY ===== */
body.bg {
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background: url("https://images.unsplash.com/photo-1586769852836-bc069f19e1b6") no-repeat center center/cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* DARK OVERLAY */
body.bg::before {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    top: 0;
    left: 0;
    z-index: -1;
}

/* ===== NAVBAR ===== */
.navbar {
    position: absolute;
    top: 0;
    width: 100%;
    padding: 15px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
}

.logo {
    color: white;
    font-weight: bold;
    font-size: 18px;
}

.nav-right a {
    color: white;
    margin-left: 20px;
    text-decoration: none;
    font-weight: 500;
}

.nav-right a:hover {
    color: #00e676;
}

.logout {
    color: #ff5252;
}

/* ===== MAIN LAYOUT ===== */
.main-container {
    display: flex;
    gap: 30px;
    align-items: center;
}

/* ===== GLASS CARD ===== */
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    text-align: center;
    color: white;
    width: 320px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* ===== LEFT ANALYSIS PANEL ===== */
.analysis-box {
    width: 260px;
    text-align: left;
}

.analysis-box h1 {
    text-align: center;
    font-size: 40px;
    margin: 10px 0;
}

.metric {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    font-size: 14px;
}

.note {
    font-size: 12px;
    margin-top: 10px;
    color: #ccc;
}

/* ===== INPUTS ===== */
input, textarea {
    width: 90%;
    padding: 10px;
    margin: 10px;
    border: none;
    border-radius: 10px;
    outline: none;
}

/* ===== BUTTON ===== */
.btn {
    padding: 10px 20px;
    margin: 10px;
    border: none;
    border-radius: 20px;
    background: #00c853;
    color: white;
    cursor: pointer;
    transition: 0.3s;
}

.btn:hover {
    transform: scale(1.05);
}

.btn.outline {
    background: transparent;
    border: 2px solid white;
}

/* ===== RESULT TEXT ===== */
#result {
    margin-top: 15px;
    font-size: 20px;
    transition: all 0.3s ease;
}

/* ===== DASHBOARD ===== */
.dashboard-container {
    display: flex;
    gap: 20px;
    margin-top: 80px;
    padding: 20px;
}

.history-box {
    max-height: 300px;
    overflow-y: auto;
}

.history-item {
    background: rgba(255,255,255,0.1);
    padding: 10px;
    margin: 10px 0;
    border-radius: 10px;
    text-align: left;
}

.spam {
    color: #ff5252;
    font-weight: bold;
}

.safe {
    color: #00e676;
    font-weight: bold;
}
.btn.outline {
    border: 2px solid #ff5252;
    color: #ff5252;
}

.btn.outline:hover {
    background: #ff5252;
    color: white;
}
.main-container {
    display: flex;
    gap: 40px;
    align-items: center;
}

/* LEFT PANEL */
.analysis-box {
    width: 260px;
}

/* SEMI CIRCLE */
.progress-container {
    position: relative;
    width: 220px;
    margin: 20px auto;
}

svg {
    width: 100%;
}

.bg-path {
    fill: none;
    stroke: #444;
    stroke-width: 10;
}

.progress-path {
    fill: none;
    stroke: #00e676;
    stroke-width: 10;
    stroke-dasharray: 282;
    stroke-dashoffset: 282;
    transition: stroke-dashoffset 0.5s ease, stroke 0.5s;
}

.percent-text {
    position: absolute;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    font-weight: bold;
}

/* METRICS */
.metric {
    display: flex;
    justify-content: space-between;
    padding: 5px 0;
    font-size: 14px;
}

.note {
    font-size: 12px;
    margin-top: 10px;
    color: #ccc;
}
.percent-text {
    top: 70%;   /* adjust center */
}
/* PROFILE DASHBOARD STYLE */
.dashboard-container {
    display: flex;
    gap: 20px;
    margin-top: 80px;
    padding: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

.glass-card h1 {
    font-size: 40px;
    margin: 10px 0;
}
.glass-card hr {
    border: 1px solid rgba(255,255,255,0.2);
    margin: 15px 0;
}
