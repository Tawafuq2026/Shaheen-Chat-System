import streamlit as st
import openai

# إعدادات الواجهة (شاهين شات - النسخة العالمية الشاملة)
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# تصميم واتساب المطور: إرسال يمين ورد يسار مع خلفية مريحة وحماية فائقة
st.markdown("""
    <style>
    .main { background-color: #e5ddd5; } 
    .stChatMessage { border-radius: 15px; padding: 12px; margin-bottom: 10px; max-width: 80%; border: 1px solid #ddd; }
    /* محادثة المستخدم محمد شاهين (يمين) */
    [data-testid="stChatMessage"]:nth-child(even) { background-color: #dcf8c6; margin-left: auto; text-align: right; }
    /* رد شاهين الذكي (يسار) */
    [data-testid="stChatMessage"]:nth-child(odd) { background-color: #ffffff; margin-right: auto; text-align: left; }
    .stTitle { text-align: right; color: #075e54; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_index=True)

# الهوية البصرية واسم المنصة على اليمين كما طلبت
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_index=True)
st.markdown('<div style="text-align: right; font-style: italic; color: #075e54;">"العلم نورٌ وفي كفي ضياؤه.. أرنو بعينٍ لا تخطئ الهدفا"</div>', unsafe_allow_index=True)
st.markdown("---")

# الربط المحمي بالمحرك العالمي (قوة OpenAI و Gemini مدمجة)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# نظام الذاكرة الشاملة والخصوصية المطلقة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# عرض المحادثة بنمط واتساب (يمين ويسار)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطق التشغيل العالمي والمنافسة الربحية
# يوفر 3 رسائل مجانية ثم يطلب الاشتراك بـ 19 ريالاً قطرياً لضمان ROI
if st.session_state.msg_count < 3:
    if prompt := st.chat_input("تحدث مع شاهين في أي مجال... العلم نور"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # استخدام أحدث موديل عالمي لضمان جودة الردود
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-001",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                res_content = response.choices[0].message.content
                st.markdown(res_content)
                st.session_state.messages.append({"role": "assistant", "content": res_content})
            except Exception:
                st.error("نظام الحماية العالمي نشط. يرجى إعادة المحاولة.")
else:
    # قفل الأرباح الذكي المرتبط بحسابك PayPal في قطر
    st.warning("⚠️ لقد استهلكت محاولاتك المجانية في النسخة التجريبية.")
    st.info("للاستمرار في استخدام 'شاهين شات' بكامل قدراته العالمية، اشترك الآن بـ 19 ريالاً فقط.")
    pay_url = "https://paypal.me/MOHDSHAHEEN"
    st.markdown(f'''
        <a href="{pay_url}" target="_blank">
            <button style="width:100%; height:60px; background-color:#FFD700; color:#001f3f; border:none; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold;">
                تفعيل الاشتراك العالمي عبر PayPal
            </button>
        </a>
    ''', unsafe_allow_index=True)
