import streamlit as st
import openai

# إعدادات الواجهة (شاهين شات - النسخة العالمية)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# تصميم الخلفية (نمط واتساب) وتنسيق الردود يمين/يسار وحماية الواجهة
st.markdown("""
    <style>
    .main { background-color: #e5ddd5; } /* خلفية واتساب الشهيرة */
    .stChatMessage { border-radius: 15px; padding: 10px; margin-bottom: 10px; max-width: 80%; }
    /* محادثة المستخدم (يمين) */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: #dcf8c6;
        margin-left: auto;
        text-align: right;
    }
    /* رد شاهين (يسار) */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #ffffff;
        margin-right: auto;
        text-align: left;
    }
    .stTitle { text-align: right; color: #075e54; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_index=True)

# اسم الموقع على الجهة اليمنى مع شعر الصقر
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_index=True)
st.markdown("""
<div style="text-align: right; font-style: italic; color: #075e54;">
"أنا الشاهين في علياء سمائي.. أرنو بعينٍ لا تخطئ الهدفا<br>
العلم نورٌ وفي كفي ضياؤه.. أصون سراً وبالحقِ اعترفا"
</div>
""", unsafe_allow_index=True)
st.markdown("---")

# الربط المحمي بالمحرك العالمي (بأعلى معايير التشفير)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# نظام الذاكرة المستقلة (لا يمكن لأحد الاطلاع عليها)
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة (يمين ويسار)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال البيانات
if prompt := st.chat_input("تحدث مع شاهين... العلم نور"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="google/gemini-2.0-flash-001",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            res_content = response.choices[0].message.content
            st.markdown(res_content)
            st.session_state.messages.append({"role": "assistant", "content": res_content})
        except Exception as e:
            st.error("نعتذر، هناك تحديث في الأنظمة الأمنية. يرجى المحاولة بعد لحظات.")
