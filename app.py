# app.py
import streamlit as st
from vertex_llm import chain
from bq_query import run_query

st.set_page_config(page_title="Ask BigQuery", page_icon="💬", layout="centered")

st.title("💬 Ask BigQuery using Vertex AI + LangChain")

st.write("""
Type a natural language question about your dataset and get the answer directly from BigQuery.
""")

question = st.text_input("Enter your question:")

if st.button("Submit") and question.strip():
    with st.spinner("Generating SQL using Vertex AI..."):
        sql = chain.run(question)
        st.subheader("🧠 Generated SQL:")
        st.code(sql, language="sql")

    with st.spinner("Running on BigQuery..."):
        try:
            rows = run_query(sql)
            st.success(f"✅ Query returned {len(rows)} rows")
            st.dataframe(rows)
        except Exception as e:
            st.error(f"Error executing query: {e}")
