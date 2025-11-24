import streamlit as st
import base64
import random

# إعدادات الصفحة
st.set_page_config(page_title="Happy Birthday ❤️", layout="wide")

# ===== CSS للخلفية الحمرا =====
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ff4d6d 0%, #ff758f 50%, #ffccd5 100%) !important;
    background-attachment: fixed;
}

/* قلوب ناعمة في الخلفية */
.stApp::before {
    content: "❤ ❤ ❤ ❤ ❤";
    position: fixed;
    top: 20%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 120px;
    color: rgba(255, 255, 255, 0.15);
    letter-spacing: 60px;
    z-index: -1;
}

/* قلوب صغيرة موزعة */
.stApp::after {
    content: "❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤";
    position: fixed;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    font-size: 40px;
    color: rgba(255, 255, 255, 0.12);
    letter-spacing: 20px;
    z-index: -1;
}

h1, h2, h3, p {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ===== تشغيل الموسيقى =====
def play_music(file_path):
    try:
        audio_file = open(file_path, "rb").read()
        audio_bytes = base64.b64encode(audio_file).decode()
        st.markdown(
            f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{audio_bytes}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )
    except:
        st.error("⚠️ ملف الموسيقى غير موجود!")

play_music("music.mp3")

# ===== القلوب المتحركة =====
for _ in range(12):
    size = random.randint(20, 40)
    x = random.randint(0, 95)
    st.markdown(
        f"<div style='position:fixed; left:{x}vw; top:0vh; font-size:{size}px; color:pink;'>❤️</div>",
        unsafe_allow_html=True
    )

# ===== عنوان رئيسي =====
st.markdown("<h1>❤️  كل سنه وانتي طيبه وبخير وسلامه ي اجمل واحلي بنوته في حياتي  ❤️</h1>", unsafe_allow_html=True)

# ===== الرسالة =====
st.markdown("""
<div class="msg-box">
كل سنة وأنتي أجمل حاجة في حياتي ❤️  
وجودك هو أجمل نعمة ربنا رزقني بيها…  
 ربنا يخليكي لقلبي وتفضلي منوّراه دايمًا يا روحي ويبعد عننا الشيطان يبت سماح والله بحبك اوي وانتي اجمل واحلي بت شوفتها في حياتي كل حاجه فيكي ربنا يخليكي ليا يم عيالي يارب .  
</div>
""", unsafe_allow_html=True)

# ===== عرض الصور =====
st.write("")
st.header("📸 احلي واجمل دكتور في الدينا  ❤️")

col1, col2 = st.columns(2)

with col1:
    st.image("p1.jpg", caption="❤️بنتي يولاد والله ", use_column_width=True)

with col2:
    st.image("p2.jpg", caption="❤️ بنتي يولاد والله ", use_column_width=True)
