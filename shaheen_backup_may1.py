import streamlit as st
import openai

# إعدادات الواجهة العالمية (شاهين شات)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# تصميم واتساب المطور: إرسال يمين ورد يسار مع خلفية واتساب
st.markdown("""
    <style>
    .main { background-color: #e5ddd5; } 
    .stChatMessage { border-radius: 15px; padding: 12px; margin-bottom: 10px; max-width: 80%; border: 1px solid #ddd; }
    /* رسالة المستخدم محمد شاهين - جهة اليمين */
    [data-testid="stChatMessage"]:nth-child(even) { 
        background-color: #dcf8c6; 
        margin-left: auto; 
        text-align: right; 
    }
    /* رد شاهين الذكي - جهة اليسار */
    [data-testid="stChatMessage"]:nth-child(odd) { 
        background-color: #ffffff; 
        margin-right: auto; 
        text-align: left; 
    }
    .stTitle { text-align: right; color: #075e54; font-family: 'Arial', sans-serif; font-weight: bold; }
    .quote-text { text-align: right; font-size: 22px; color: #000000; font-weight: bold; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# الهوية البصرية واسم المنصة
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)
st.markdown('<div class="quote-text">العلم نورٌ وفي كفي ضياؤه</div>', unsafe_allow_html=True)
st.markdown("---")

# الربط العالمي المباشر (تصحيح المحرك ليتجاوز خطأ 401)
# ملاحظة: تم تحديث الرابط لضمان التعرف على المستخدم فوراً
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# عرض المحادثة بنمط واتساب (يمين ويسار)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# نظام التشغيل والربح: 5 رسائل مجانية ثم اشتراك 12 ريال قطري
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            try:
                # استخدام محرك مستقر لتجاوز أخطاء الهوية
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-001",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    extra_headers={
                        "HTTP-Referer": "https://github.com/Tawafuq2026/Shaheen-Chat-System",
                        "X-Title": "Shaheen Chat"
                    }
                )
                res_content = response.choices[0].message.content
                st.markdown(res_content)
                st.session_state.messages.append({"role": "assistant", "content": res_content})
            except Exception as e:
                st.error(f"خطأ تقني: {e}")
else:
    st.warning("⚠️ انتهت محاولاتك المجانية.")
    st.info("للاستمرار في استخدام القوة العالمية لشاهين، اشترك الآن بـ 12 ريالاً قطرياً.")
    pay_url = "https://paypal.me/MOHDSHAHEEN"
    st.markdown(f'<a href="{pay_url}" target="_blank"><button style="width:100%; height:60px; background-color:#FFD700; color:#001f3f; border:none; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold;">تفعيل الاشتراك (12 ريال) عبر PayPal</button></a>', unsafe_allow_html=True)
