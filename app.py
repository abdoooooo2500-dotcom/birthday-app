# الملف: app.py
import streamlit as st

# ======================================
# --- الأسطر الوحيدة التي يجب عليك تعديلها! ---
# ======================================
GIRLFRIEND_NAME = "يا حبيبتي الغالية" 
MESSAGE = (
    "كل سنة وأنتي ي أجمل إنسانة في حياتي.\n"
    "انتي كل حاجه ليها كل حاجه اتمنتها كانت فيكي ي اجمل زكري حصلتلي في حياتي .\n"
    "بحبك اوي يروح قلبي، وذكرياتنا هي كنزي."
)
# ضع أسماء صورك هنا. تأكد أن الأسماء مطابقة تماماً لما في المجلد (مثلاً: ["صورة_الرحلة.png", "صورة_1.jpeg"])
PHOTO_FILES = ["p1.jpg", "p2.jpg"] 
# ======================================

# إعدادات التصميم (لا تعدل هذا القسم)
st.set_page_config(layout="wide")

st.markdown(f"""
<style>
.stApp {{ background-color: #f7e8ec; text-align: right; direction: rtl; }}
h1, h2, h3 {{ color: #a73a64; text-align: center; font-family: 'Arial', sans-serif; }}
.message-box {{ background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
</style>
""", unsafe_allow_html=True)

# 1. شاشة الترحيب والرسالة
st.markdown("<h1>🎉 عيد ميلاد سعيد يا ي اجمل انسانه في حياتي ي كل حياتي " + GIRLFRIEND_NAME + "</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='message-box'><p>{MESSAGE}</p></div>", unsafe_allow_html=True)

st.divider()

# 2. معرض الصور
st.header("🖼️ معرض الصور")
cols = st.columns(len(PHOTO_FILES))

for i, photo_name in enumerate(PHOTO_FILES):
    try:
        with cols[i]:
            # عرض الصورة مع وصف بسيط
            st.image(photo_name, use_column_width=True, caption=f"ذكرى رقم {i+1}")
    except FileNotFoundError:
        # رسالة خطأ إذا لم يتم العثور على الصورة
        st.error(f"خطأ: لم يتم العثور على الصورة باسم {photo_name}. تأكد من وجودها في نفس المجلد!")