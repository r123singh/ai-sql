# SQL Query Assistant

SQL Query Assistant is a Streamlit-based web application that leverages OpenAI's GPT models to convert natural language queries into SQL statements. This tool simplifies database interactions by allowing users to input questions in plain English and receive corresponding SQL queries.

## Features

- **Natural Language to SQL Conversion**: Transforms user input into SQL queries using OpenAI's language models.
- **Customizable Table Schemas**: Accepts table schemas in JSON format to tailor the SQL generation to specific database structures.
- **Interactive Web Interface**: Provides a user-friendly interface for inputting queries and viewing generated SQL statements.

## Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system.
- **OpenAI API Key**: Obtain an API key from OpenAI to access their GPT models.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/r123singh/ai-sql.git
   cd ai-sql
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

2. **Access the Interface**:

   Open your web browser and navigate to `http://localhost:8501` to interact with the application.

3. **Input Details**:

   - Enter your OpenAI API key in the sidebar.
   - Provide your natural language query in the "Input your query" field.
   - Input the table schema in JSON format in the designated area.

4. **Generate SQL**:

   Click the "Submit" button to generate the SQL query based on your input.

## Example

**User Query**: "Find the names of all employees in the sales department."

**Table Schema**:

```json
{
  "table_name": "employees",
  "columns": [
    {"name": "id", "type": "INTEGER"},
    {"name": "name", "type": "VARCHAR"},
    {"name": "department", "type": "VARCHAR"},
    {"name": "salary", "type": "FLOAT"}
  ]
}
```

**Generated SQL**:

```sql
SELECT name
FROM employees
WHERE department = 'sales';
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## Acknowledgements

- **OpenAI**: For providing the GPT models that power the natural language processing capabilities.
- **Streamlit**: For offering an easy-to-use framework for building interactive web applications.

---

*Simplify your database queries with the power of AI!* 
