import streamlit as st
import openai

# إعدادات واجهة الموقع الاحترافية لتعكس رؤيتك العالمية
st.set_page_config(page_title="شاهين شات - المنصة العالمية", page_icon="🌐")
st.title("🌐 شاهين شات: منصة الذكاء الاصطناعي الشاملة")
st.markdown("---")

# إعداد الاتصال باستخدام المفتاح الجديد الذي استخرجته (النهاية 68b6)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# نظام الذاكرة للموقع لضمان استمرارية الحوار
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض تاريخ المحادثة بشكل منسق
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# مدخل البيانات لخدمة عملائك من قطر وعمان والصين
if prompt := st.chat_input("سيد محمد، اسأل شاهين عن أي موضوع إداري، تقني، أو عام..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # استخدام أقوى نماذج الذكاء الاصطناعي لتقديم إجابات شاملة
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-001",
                messages=[
                    {"role": "system", "content": "أنت مساعد ذكاء اصطناعي عالمي وشامل تدعى 'شاهين'. تقدم استشارات احترافية في كافة المجالات بأسلوب السيد محمد شاهين الخبير الإداري."},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
