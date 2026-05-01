import streamlit as st
import openai

# إعدادات واجهة الموقع الاحترافية
st.set_page_config(page_title="شاهين شات - النسخة العالمية", page_icon="🏢")
st.title("🏢 شاهين شات: منصة الإدارة والعمليات العالمية")
st.markdown("---")

# إعداد الاتصال (باستخدام مفتاحك الحالي)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# نظام الذاكرة للموقع
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض تاريخ المحادثة بشكل منسق
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# مدخل البيانات (أنت:)
if prompt := st.chat_input("سيد محمد، اسأل شاهين عن أي استشارة إدارية أو فنية..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-001",
                messages=[
                    {"role": "system", "content": "أنت مساعد خبير في الإدارة، الموارد البشرية، وتصنيع الألمنيوم والأخشاب. اسمك شاهين."},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
            