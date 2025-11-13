import streamlit as st
import pandas as pd
from pathlib import Path
import base64

st.set_page_config(page_title="Cybersecurity Jobs: Salary Explorer", page_icon="🕵️‍♂️")

# --- Banner Section ---
banner_path = Path("digital_rain_banner.jpg")
if banner_path.exists():
    with open(banner_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .banner {{
            width: 100%;
            height: 280px;
            background: url("data:image/jpeg;base64,{b64}") no-repeat center center;
            background-size: cover;
            border-radius: 12px;
            margin-bottom: 25px;
            position: relative;
        }}
        .banner-overlay {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.45); /* optional dark overlay for contrast */
            border-radius: 12px;
        }}
        .banner-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            font-size: 2.2rem;
            font-weight: 700;
            text-shadow: 0 2px 8px rgba(0,0,0,0.6);
        }}
        </style>
        <div class="banner">
            <div class="banner-overlay"></div>
            <div class="banner-text">🕵️‍♂️ Cybersecurity Jobs: Salary Explorer</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning("Banner image `digital_rain_banner.jpeg` not found. Please place it beside this file.")

# --- Page Intro ---
st.write("""
Welcome to the **Cybersecurity Jobs: Salary Explorer!**  
Analyze trends in salary, job roles, remote work, and more.
""")

# --- Load Dataset ---
df = pd.read_csv('salaries_cyber_clean.csv')

# --- Dataset Info ---
st.subheader("Dataset at a Glance")
st.markdown(f"- **Total Records:** {df.shape[0]}")
st.markdown(f"- **Unique Job Titles:** {df['job_title'].nunique()}")
st.markdown(f"- **Years Covered:** {df['work_year'].min()}–{df['work_year'].max()}")
st.markdown(f"- **Countries Covered:** {df['company_location'].nunique()}")

st.subheader("Sample Data")
st.dataframe(df.head(10))

st.subheader("Column Descriptions")
column_info = {
    "work_year": "Year of the salary record",
    "experience_level": "Experience level of employee",
    "employment_type": "Full-time, part-time, etc.",
    "job_title": "Role or job title",
    "salary": "Salary in original currency",
    "salary_currency": "Currency of salary",
    "salary_in_usd": "Salary standardized to USD",
    "employee_residence": "Country of employee",
    "remote_ratio": "Remote work percentage (0–100)",
    "company_location": "Location of company HQ",
    "company_size": "Company size (S/M/L)"
}
st.table(pd.DataFrame(list(column_info.items()), columns=["Column", "Description"]))
