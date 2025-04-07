# resume_screening_AI
Project: Resume Screening AI

Goal: Automatically analyze resumes and rank/screen them based on a job description using NLP and basic AI logic.


---

Features You Can Include:

Upload multiple resumes (PDF/DOCX)

Extract text using OCR or PDF parsers

Compare with job description (JD)

Use NLP to match keywords and skills

Give score out of 100

Rank top candidates

Optional: Email result to HR (future enhancement)



---

Technologies:

Python

pdfminer or PyMuPDF for reading resumes

spacy / nltk for NLP

Streamlit (optional frontend)

GitHub + PythonAnywhere or Replit (deployment)



---

Step-by-Step Plan:

1. Resume Upload System:
Accept resumes in PDF format from a folder or upload interface.


2. Text Extraction:
Extract all text from PDF using PyMuPDF or pdfminer.


3. Keyword Matching:

Get job description input.

Extract keywords (like skills, role, experience).

Match % of keywords with each resume.



4. Scoring & Ranking Logic:

Assign scores based on keyword matches.

Rank candidates accordingly.



5. Final Output:

Table showing names, scores, and match percentage.
