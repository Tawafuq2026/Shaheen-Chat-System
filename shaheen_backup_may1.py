import streamlit as st
import requests
import json

# 1. الهوية البصرية (شاهين شات - العلم نور)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. تصميم واتساب (يمين ويسار) بخط واضح وغير مائل
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

# 3. مفتاح التشغيل الجديد المرتبط برصيدك (20.98 دولار)
API_KEY = "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"

if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. نظام الربح (5 رسائل مجانية ثم 12 ريالاً)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
        st.session_state.append_messages = st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            headers = {
                "Authorization": f"Bearer {API_KEY.strip()}",
                "Content-Type": "application/json",
                "X-Title": "Shaheen Chat"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=15)
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    st.error(f"عذراً يا سيد محمد، المزود العالمي (OpenRouter) لا يزال يرفض هذا المفتاح. الخطأ: {response.status_code}. يرجى محاولة شحن رصيد إضافي أو مراجعة إعدادات الحساب.")
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
else:
    st.warning("⚠️ انتهت محاولاتك المجانية.")
    st.info("للاستمرار، اشترك بـ 12 ريالاً.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:50px; background-color:#FFD700; border-radius:10px;">ادفع 12 ريال لتفعيل الخدمة</button></a>', unsafe_allow_html=True)
