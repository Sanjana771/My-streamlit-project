# Mini-Project Review-2 Presentation & Viva Guide
**Department of CSE (Artificial Intelligence & Machine Learning)**  
**Vidyavardhaka College of Engineering (VVCE), Mysuru**  
**Date of Review:** 20th November 2026  

---

## 📌 Project Title
**AI-Powered Placement Readiness & Skill Gap Analyzer**

### 👥 Project Team Members
- **Sanjana B R** — USN: `4VV25CI414` (5th Sem AIML)
- **Namith N** — USN: `4VV25CI409` (5th Sem AIML)
- **Rohith S** — USN: `4VV25CI412` (5th Sem AIML)

---

## 🏆 Review-2 Compliance Checklist (Circular Requirements)

| Requirement from Circular | Status | Implementation Details in This Project |
|---|:---:|---|
| **Project Implementation (At least 50% required)** | **100% COMPLETE** | Full end-to-end working system: resume parsing, NLP extraction, TF-IDF cosine matching, trained ML classifier, roadmap generator, and batch dashboard. |
| **Effective Use & Deployment of Tools** | **COMPLETED** | Python 3.12, Streamlit web app, SQLite3 database, Scikit-learn ML models, Plotly interactive charts, pdfplumber & python-docx. |
| **Individual & Team Contributions** | **DOCUMENTED** | Distinct, balanced roles clearly divided across NLP, Data/Matching, and ML/UI. |
| **Live Working Demonstration Ready** | **READY** | 1-Click launcher (`run.bat`) + preloaded student resumes + live PDF/DOCX file upload. |

---

## 👤 Individual and Team Contributions Breakdown

### 1. Sanjana B R (USN: `4VV25CI414`) — NLP & Text Processing Lead
- **Modules Owned:** `modules/resume_parser.py`, `modules/nlp_extractor.py`, and `modules/skill_taxonomy.py`.
- **Key Contributions:**
  1. Developed automated multi-format text extraction supporting PDF (`pdfplumber`) and Word documents (`python-docx`).
  2. Implemented text preprocessing pipeline: noise filtering, tokenization, regular expression masking, and stop-word elimination.
  3. Integrated **ESCO / O\*NET** hierarchical skill taxonomy covering over 200+ canonical technical skills and aliases (e.g., standardizing `Python3`, `Py`, `Python Programming` to canonical `Python`).
  4. Built candidate metadata extractor for auto-detecting candidate names, emails, and phone numbers.

### 2. Namith N (USN: `4VV25CI409`) — Job Data & Matching Engine Lead
- **Modules Owned:** `database/db_setup.py`, `modules/matcher.py`, and `database/jobs.db`.
- **Key Contributions:**
  1. Curated and structured cleaned job posting datasets inspired by Naukri and LinkedIn across 15+ high-demand tech roles.
  2. Designed SQLite persistent database schema and CSV data backup.
  3. Implemented mathematical **TF-IDF vector space model** and **Cosine Similarity** calculation between candidate resumes and job descriptions.
  4. Built dual-layer matching algorithm: combines exact taxonomy intersection (65% weight) with semantic TF-IDF context similarity (35% weight).
  5. Developed job recommendation engine ranking all available opportunities by composite match score.

### 3. Rohith S (USN: `4VV25CI412`) — Machine Learning & UI/Dashboard Lead
- **Modules Owned:** `models/train_readiness_model.py`, `modules/batch_analyzer.py`, `modules/roadmap_generator.py`, and `app.py`.
- **Key Contributions:**
  1. Designed and trained multi-model Placement Readiness classifiers: **Logistic Regression**, **Decision Tree**, and **Random Forest**.
  2. Evaluated models using 80-20 stratified train-test splits on **Accuracy, Precision, Recall, F1-Score**, and generated Confusion Matrices.
  3. Developed interactive **Streamlit** web application styled with official VVCE branding, color themes, and responsive metric cards.
  4. Designed interactive **Plotly** data visualizations (Placement Readiness Gauge, Competency Domain Radar Chart, and Batch Skill Deficit Bar Charts).
  5. Implemented the **Placement Cell Batch Analytics** module to give the HOD and placement coordinators high-level visibility over batch-wide skill deficits.

---

## 🚀 Live Demonstration Flow for Review-2 (Step-by-Step)

1. **Step 1: Launch Application**
   - Double-click `run.bat` or run:
     ```bash
     streamlit run app.py
     ```
   - Show the evaluator the clean VVCE AIML branded dashboard.

2. **Step 2: 1-Click Student Self-Assessment Demo**
   - Select **Sanjana B R (Machine Learning Profile)** or **Namith N** or **Rohith S** from the preloaded demo selector (or upload any PDF resume).
   - Select Target Role: `Machine Learning Engineer`.
   - Set CGPA (e.g., 8.4) and Projects (e.g., 3).
   - Click **"🚀 Analyze Placement Readiness"**.

3. **Step 3: Highlight Key Output Modules**
   - **Overall Match Score:** Show composite match (e.g., 78%).
   - **Matched Skills:** Green badges indicating student competencies.
   - **Skill Gaps:** Red badges displaying exact missing industry requirements.
   - **Radar Chart:** Visual competency breakdown across AI/ML, Data, Web, and Core CS.
   - **Personalized Roadmap:** Show step-by-step topic order, learning resources, and portfolio project ideas.
   - **Job Recommendations:** Ranked top 5 jobs from Naukri & LinkedIn database.
   - **Download Report:** Click the download button to generate a clean placement report.

4. **Step 4: Demonstrate Batch Analytics for VVCE Placement Cell**
   - Switch to **"📊 Placement Cell Batch Analytics"** tab in the sidebar.
   - Explain how this solves the administrative bottleneck for VVCE by revealing that 70%+ of students lack Docker/Cloud skills, justifying department workshops.

5. **Step 5: Demonstrate ML Models & Evaluation**
   - Switch to **"🧠 ML Models & Evaluation"** tab.
   - Show the comparative table of Logistic Regression vs Decision Tree vs Random Forest.
   - Point out the Confusion Matrix and explain precision/recall metrics.

---

## 🎯 Evaluator Viva Questions & Ready Answers

### Q1: Why did you use TF-IDF and Cosine Similarity instead of simple keyword count?
> **Answer:** Simple keyword counting is biased by document length (a long resume with repetitive words gets an inflated score) and cannot distinguish between rare technical words and generic English words. TF-IDF penalizes common words and awards higher weights to rare domain terms (like `PyTorch` or `Scikit-learn`). Cosine similarity calculates the cosine of the angle between two vectors in n-dimensional space, measuring orientation/direction rather than length, making it ideal for resume-to-job matching.

### Q2: What is the purpose of the ESCO / O*NET Skill Taxonomy?
> **Answer:** It solves the vocabulary mismatch problem. Candidates write "Python 3", "Python Programming", or "Py", while job descriptions may write "Python". Without taxonomy canonicalization, exact string matching fails. Our taxonomy maps synonyms and variations to one canonical standard node.

### Q3: Why train a separate ML model when you already have similarity scores?
> **Answer:** Campus placements are multi-factorial. Similarity score only checks if the resume text mentions keywords. Recruiters also evaluate academic consistency (CGPA), number of completed projects, internships, and certifications. Our ML model learns from historical patterns to predict actual placement probability based on the holistic candidate profile.

### Q4: Which project category does this fall under and what is the justification?
> **Answer:** **Automation of Administrative and Academic Tasks at VVCE**. Currently, mentors and placement officers review hundreds of student resumes manually, giving delayed and subjective feedback. Our system automates screening, gap identification, and personalized roadmap creation in seconds.
