import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="English to SQL Translator",
    page_icon="📝",
    layout="centered"
)

# Header
st.title("📝 English → SQL Translator")
st.markdown("Convert natural language queries into **SQL statements** using an AI model.")

# Input box
query = st.text_area("💬 Enter your query in plain English:", height=150, placeholder="e.g. Show me all customers who spent more than $500 last month")

# Generate button
if st.button("✨ Generate SQL"):
    if not query.strip():
        st.warning("Please enter a query before clicking Generate.")
    else:
        with st.spinner("Translating to SQL..."):
            try:
                response = requests.post("http://127.0.0.1:8000/generate", json={"prompt": query})
                data = response.json()

                # Output
                st.success("✅ SQL Generated Successfully!")
                st.code(data["sql"], language="sql")

                # Copy button
                st.download_button(
                    label="📋 Copy SQL",
                    data=data["sql"],
                    file_name="query.sql",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("🔗 Built with **FastAPI** + **Streamlit** + **MLX-LM** | Demo Project for Portfolio")
