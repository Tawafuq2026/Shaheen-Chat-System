import streamlit as st
import requests
import json

# 1. الهوية البصرية (شاهين شات - العلم نور)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #e5ddd5; } 
    .stChatMessage { border-radius: 15px; padding: 12px; margin-bottom: 10px; max-width: 80%; border: 1px solid #ddd; }
    [data-testid="stChatMessage"]:nth-child(even) { background-color: #dcf8c6; margin-left: auto; text-align: right; }
    [data-testid="stChatMessage"]:nth-child(odd) { background-color: #ffffff; margin-right: auto; text-align: left; }
    .stTitle { text-align: right; color: #075e54; font-family: 'Arial', sans-serif; font-weight: bold; }
    .quote-text { text-align: right; font-size: 24px; color: #000000; font-weight: bold; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)
st.markdown('<div class="quote-text">العلم نورٌ وفي كفي ضياؤه</div>', unsafe_allow_html=True)
st.markdown("---")

# 2. جلب المفتاح بأمان تام (الإصلاح الجذري)
try:
    # جلب المفتاح وتنظيفه من أي مسافات زائدة
    raw_key = st.secrets["OPENROUTER_API_KEY"]
    API_KEY = raw_key.strip().replace('"', '').replace("'", "")
except Exception:
    st.error("تنبيه: المفتاح غير موجود في الخزنة السرية (Secrets).")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. نظام التشغيل والربح (5 رسائل مجانية ثم اشتراك 12 ريال قطري)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي... العلم نور"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # الرابط النظيف تماماً بدون أي مسافات
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                # استخدام الرابط النظيف المباشر
                response = requests.post(url.strip(), headers=headers, data=json.dumps(payload), timeout=30)
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    st.error(f"تنبيه تقني ({response.status_code}): المزود يرفض المفتاح. تأكد من رصيدك.")
            except Exception as e:
                st.error(f"عطل في الاتصال: {e}")
else:
    st.warning("⚠️ انتهت محاولاتك المجانية.")
    st.info("للاستمرار، اشترك بـ 12 ريالاً قطرياً.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:50px; background-color:#FFD700; border-radius:10px; cursor:pointer;">تفعيل الاشتراك (12 ريال)</button></a>', unsafe_allow_html=True)
