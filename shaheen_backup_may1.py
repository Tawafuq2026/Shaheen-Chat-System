import streamlit as st
import openai

# إعدادات الواجهة العالمية لشاهين شات
st.set_page_config(page_title="شاهين شات - المنصة العالمية", page_icon="🌐")
st.title("🌐 شاهين شات: منصة الذكاء الاصطناعي الشاملة")
st.markdown("---")

# ربط المحرك مباشرة بالمفتاح الجديد المشحون بـ 10 دولارات
# يا سيد محمد: ضع المفتاح الجديد بين علامات التنصيص في السطر أدناه
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ضع_مفتاح_OpenRouter_الجديد_هنا"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسأل شاهين عن أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-001",
                messages=[
                    {"role": "system", "content": "أنت مساعد ذكاء اصطناعي شامل وقوي تدعى 'شاهين'. تقدم إجابات ذكية في كافة المجالات بأسلوب احترافي وعالمي."},
                    {"role": "user", "content": prompt}
                ]
            )
            response = completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
