import streamlit as st
import google.generativeai as genai

# ============ Gemini API setup ============
# Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyAc6ctooYBucHy1dvONh6IPPRqBX4U4H68")

model = genai.GenerativeModel("gemini-2.5-flash")

# ============ Streamlit UI ============
st.title("🧾 TaxGenie AI — Smart Tax Optimizer")
st.write("Upload your financial data and get AI-powered tax-saving suggestions.")

# File uploader or text input
uploaded_file = st.file_uploader("Upload your financial summary (.txt)", type=["txt"])
user_text = st.text_area("Or paste your financial data here", "")

analyze_button = st.button("Analyze & Suggest Tax Savings")

if analyze_button:
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")
        input_text = file_content
    elif user_text.strip():
        input_text = user_text
    else:
        st.warning("Please upload a file or paste your data.")
        st.stop()

    # Prompt for Gemini
    prompt = f"""
You are an expert tax advisor. Analyze the following financial data and suggest possible tax deductions
and legal ways to reduce taxable income in India for FY 2025-26. Provide clear actionable steps.

Financial data:
{input_text}
    """

    with st.spinner("Analyzing with Gemini..."):
        response = model.generate_content(prompt)
        ai_output = response.text

    st.subheader("💡 Tax-Saving Suggestions")
    st.markdown(ai_output)

