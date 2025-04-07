import streamlit as st
import re

st.set_page_config(page_title="Resume Screening AI", layout="centered")

st.title("Resume Screening AI")
st.subheader("Evaluate your resume based on job keywords")

# Input Section
resume_text = st.text_area("Paste your Resume Text here")

job_keywords = st.text_input("Enter job-specific keywords (comma-separated)", "Python, Machine Learning, Data Analysis")

if st.button("Evaluate"):
    if not resume_text.strip():
        st.warning("Please paste your resume text.")
    else:
        keywords = [kw.strip().lower() for kw in job_keywords.split(",")]
        matched = [kw for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', resume_text.lower())]
        score = round((len(matched) / len(keywords)) * 100)

        st.success(f"Job-Fit Score: {score}%")
        st.write("Matched Keywords:", ", ".join(matched))

        if score > 70:
            st.balloons()
            st.info("Great! Your resume is quite relevant.")
        elif score > 40:
            st.info("Decent. You can still improve it by adding more job-relevant keywords.")
        else:
            st.error("Resume needs improvement for the desired job profile.")