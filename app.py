import streamlit as st
import base64

# ============ إعدادات الصفحة ============
st.set_page_config(page_title="Happy Birthday", layout="wide")

# ===== خلفية حمرا + أنيميشن القلوب =====
st.markdown("""
    <style>
    body {
        background-color: #8b0000 !important;
    }
    .heart {
        position: fixed;
        top: -10px;
        color: pink;
        font-size: 30px;
        animation: fall 5s linear infinite;
    }
    @keyframes fall {
        0% {transform: translateY(0) translateX(0);}
        100% {transform: translateY(100vh) translateX(20px);}
    }
    </style>

    <script>
    const createHeart = () => {
        const heart = document.createElement("div");
        heart.classList.add("heart");
        heart.innerHTML = "❤";
        heart.style.left = Math.random() * 100 + "vw";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 4000);
    };
    setInterval(createHeart, 300);
    </script>
""", unsafe_allow_html=True)

# ===== تشغيل موسيقى =====
def play_music(file_path):
    audio_file = open(file_path, "rb").read()
    audio_bytes = base64.b64encode(audio_file).decode()
    st.markdown(f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{audio_bytes}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

play_music("music.mp3")  # ← حط اسم ملف الموسيقى هنا

# ===== الرسالة =====
st.markdown("<h1 style='text-align:center; color:white;'>❤️ عيد ميلاد سعيد ❤️</h1>", unsafe_allow_html=True)

st.write("")

st.markdown("""
<div style='background:white; padding:20px; border-radius:10px; text-align:right;'>
كل سنة وأنتي أجمل إنسانة في حياتي ❤️  
وجودك هو أحلى حاجة حصلتلي…  
ربنا يخليكي لقلبي ويبارك فيكي يا عمري.
</div>
""", unsafe_allow_html=True)
