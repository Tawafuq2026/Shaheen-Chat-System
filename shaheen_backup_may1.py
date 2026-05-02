import streamlit as st
import requests
import json

# 1. الهوية البصرية (شاهين شات - العلم نور)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. تصميم واتساب المطور بنظام الإرسال والرد المتقابل
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

# 3. عرض اسم المنصة والشعار المعتمد بخط واضح
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)
st.markdown('<div class="quote-text">العلم نورٌ وفي كفي ضياؤه</div>', unsafe_allow_html=True)
st.markdown("---")

# 4. الربط بالخزنة السرية (نظام التحقق المزدوج)
# قمنا بتطوير طريقة سحب المفتاح لتكون أكثر مرونة لتجنب خطأ 401
try:
    if "OPENROUTER_API_KEY" in st.secrets:
        API_KEY = st.secrets["OPENROUTER_API_KEY"].strip()
    else:
        # محاولة أخرى للوصول للمفتاح في حال وجوده بتنسيق مختلف
        API_KEY = st.secrets.get("OPENROUTER_API_KEY", "").strip()
except Exception:
    st.error("تنبيه تقني: لا يوجد مفتاح نشط في الخزنة السرية.")
    st.stop()

if not API_KEY or API_KEY == "":
    st.error("تنبيه: المفتاح الموجود في الخزنة فارغ.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# 5. عرض المحادثة بنمط واتساب
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. نظام التشغيل والربح (5 رسائل مجانية ثم اشتراك 12 ريال قطري)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي... العلم نور"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # بروتوكول اتصال مباشر مع تجاوز أخطاء التعريف
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/Tawafuq2026/Shaheen-Chat-System"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                # محاولة الاتصال المباشر بالمزود
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=30)
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    # تشخيص دقيق لسبب استمرار الخطأ
                    st.error(f"تنبيه تقني ({response.status_code}): المزود العالمي لا يزال يرفض الهوية.")
                    st.info("يا سيد محمد، يرجى التأكد أن المفتاح في الخزنة موضوع بين علامتي تنصيص هكذا: \"key\"")
            except Exception as e:
                st.error(f"عطل في الاتصال بالخادم: {e}")
else:
    # واجهة الدفع (ROI)
    st.warning("⚠️ انتهت محاولاتك المجانية.")
    st.info("للاستمرار في الخدمة، اشترك بـ 12 ريالاً قطرياً فقط.")
    pay_url = "https://paypal.me/MOHDSHAHEEN"
    st.markdown(f'<a href="{pay_url}" target="_blank"><button style="width:100%; height:60px; background-color:#FFD700; border-radius:12px; cursor:pointer; font-weight:bold;">تفعيل الاشتراك بـ 12 ريال</button></a>', unsafe_allow_html=True)
