import openai
import json
import streamlit as st

st.subheader("🔍💻 SQL Query Assistant: Transform Natural Language into SQL Instantly!🧠✨", divider=True)
apiKey = st.sidebar.text_input("Enter OpenAI API Key", type="password")
    
input_user_query = st.text_input("🚀 Input your query", placeholder="for e.g. Find the names of all employees in the sales department")

input_schema = st.text_area("📊Input table schema in JSON format",height=200, placeholder= """for e.g.{
        "table_name": "employees",
        "columns": [
            {"name": "id", "type": "INTEGER"},
            {"name": "name", "type": "VARCHAR"},
            {"name": "department", "type": "VARCHAR"},
            {"name": "salary", "type": "FLOAT"}
        ]
    }""")

submitted = st.button("Submit", type="primary")

if apiKey:
    openai.api_key = apiKey
else:
    st.info("Please input OpenAI API Key")

prompt = f"""
Generate an SQL query based on the following table schema and user request:

Table Schema:
{json.dumps(input_schema, indent=2)}

User Query:
{input_user_query}

SQL Query:
"""
if openai.api_key is None:
    st.info("Please enter OpenAI Key")
elif submitted:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role":"system",
                "content": prompt
            },
            {
                "role": "user",
                "content": ""
            }
        ]
    )
    st.code(response.choices[0].message.content)
    