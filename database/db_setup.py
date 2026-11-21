"""
Job Database Setup & Seeding Module
Initializes an SQLite database and CSV file populated with cleaned job listings
modeled after Naukri and LinkedIn job posting datasets.
"""

import os
import sqlite3
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(__file__), "jobs.db")
CSV_PATH = os.path.join(os.path.dirname(__file__), "jobs_dataset.csv")

JOBS_DATA = [
    {
        "job_title": "Machine Learning Engineer",
        "company": "Fractal Analytics",
        "experience": "0-2 Years",
        "location": "Bengaluru / Remote",
        "skills": "Python, Machine Learning, Scikit-learn, Pandas, NumPy, Deep Learning, SQL, Git",
        "description": "Looking for an ML Engineer with strong grasp of predictive modeling, supervised and unsupervised learning algorithms, feature engineering, and deploying models using Flask or FastAPI.",
        "role_category": "Machine Learning",
        "source": "Naukri"
    },
    {
        "job_title": "Junior Data Scientist",
        "company": "Tiger Analytics",
        "experience": "0-1 Years",
        "location": "Chennai / Bengaluru",
        "skills": "Python, Statistics, Machine Learning, Scikit-learn, Pandas, NumPy, SQL, Data Visualization, Power BI",
        "description": "Join our AI innovation lab. Must possess strong foundations in statistics, regression, classification, clustering, exploratory data analysis, and dashboard generation.",
        "role_category": "Data Science",
        "source": "LinkedIn"
    },
    {
        "job_title": "Data Analyst Intern / Associate",
        "company": "Mu Sigma",
        "experience": "0-1 Years",
        "location": "Bengaluru",
        "skills": "SQL, Microsoft Excel, Power BI, Python, Data Analysis, Tableau, Statistics",
        "description": "Seeking analytical minds for data extraction, SQL queries, dashboard creation in Power BI, data cleaning, and business insights generation.",
        "role_category": "Data Analytics",
        "source": "Naukri"
    },
    {
        "job_title": "Python Developer",
        "company": "ThoughtWorks",
        "experience": "0-2 Years",
        "location": "Bengaluru / Mysuru",
        "skills": "Python, Django, Flask, RESTful APIs, SQL, PostgreSQL, Git, Object-Oriented Programming, Linux",
        "description": "Backend Python developer role writing clean, scalable microservices, REST APIs, database schemas, and unit tests using pytest.",
        "role_category": "Software Engineering",
        "source": "Naukri"
    },
    {
        "job_title": "Software Development Engineer (SDE-1)",
        "company": "Amazon",
        "experience": "0-1 Years",
        "location": "Bengaluru / Hyderabad",
        "skills": "Java, Data Structures & Algorithms, Object-Oriented Programming, DBMS, Operating Systems, System Design, Git",
        "description": "Strong problem solving skills in Data Structures and Algorithms, object oriented design patterns, multi-threading, and distributed system concepts.",
        "role_category": "Software Engineering",
        "source": "LinkedIn"
    },
    {
        "job_title": "Full Stack Developer (MERN)",
        "company": "Zoho Corporation",
        "experience": "0-2 Years",
        "location": "Chennai / Remote",
        "skills": "JavaScript, React.js, Node.js, Express.js, MongoDB, HTML, CSS, RESTful APIs, Git",
        "description": "Design and develop scalable modern web applications with responsive React frontends and robust Node.js backend services.",
        "role_category": "Web Development",
        "source": "Naukri"
    },
    {
        "job_title": "AI & NLP Engineer",
        "company": "InMobi",
        "experience": "0-2 Years",
        "location": "Bengaluru",
        "skills": "Python, Natural Language Processing, Transformers, Large Language Models, PyTorch, NLTK, spaCy, Hugging Face",
        "description": "Work on state-of-the-art NLP pipelines, sentiment analysis, document parsing, embeddings, and fine-tuning transformer models.",
        "role_category": "Machine Learning",
        "source": "LinkedIn"
    },
    {
        "job_title": "Computer Vision Engineer",
        "company": "Bosch Global Software Technologies",
        "experience": "0-2 Years",
        "location": "Bengaluru / Coimbatore",
        "skills": "Python, Computer Vision, OpenCV, PyTorch, TensorFlow, Deep Learning, C++",
        "description": "Develop edge AI and computer vision algorithms for autonomous driving, object detection (YOLO), image segmentation, and camera calibration.",
        "role_category": "Machine Learning",
        "source": "Naukri"
    },
    {
        "job_title": "DevOps & Cloud Engineer Associate",
        "company": "Infosys",
        "experience": "0-2 Years",
        "location": "Mysuru / Bengaluru",
        "skills": "AWS, Docker, Kubernetes, CI/CD, Jenkins, Linux, Bash/Shell Scripting, Git, Terraform",
        "description": "Automate build and deployment pipelines, manage containerized infrastructure on AWS, configure Kubernetes clusters, and monitor systems.",
        "role_category": "Cloud & DevOps",
        "source": "Naukri"
    },
    {
        "job_title": "Data Engineer",
        "company": "Flipkart",
        "experience": "0-2 Years",
        "location": "Bengaluru",
        "skills": "Python, SQL, Apache Spark, PySpark, Apache Kafka, Apache Hadoop, ETL, Big Data",
        "description": "Build high-throughput real-time and batch data pipelines, manage data lakes, optimize complex SQL queries, and handle petabyte-scale data.",
        "role_category": "Data Science",
        "source": "LinkedIn"
    },
    {
        "job_title": "Systems Engineer (Campus Recruit)",
        "company": "TCS (Tata Consultancy Services)",
        "experience": "Fresher",
        "location": "Pan India / Mysuru",
        "skills": "Java, Python, C++, SQL, DBMS, Data Structures & Algorithms, Object-Oriented Programming, Computer Networks",
        "description": "Entry-level software engineering role for graduating engineering students with strong computer science fundamentals and analytical aptitude.",
        "role_category": "Software Engineering",
        "source": "Naukri"
    },
    {
        "job_title": "Frontend Engineer",
        "company": "Swiggy",
        "experience": "0-2 Years",
        "location": "Bengaluru",
        "skills": "JavaScript, TypeScript, React.js, HTML, CSS, Tailwind CSS, Redux, RESTful APIs",
        "description": "Create pixel-perfect, highly responsive consumer facing interfaces with fast render times and clean state management.",
        "role_category": "Web Development",
        "source": "LinkedIn"
    },
    {
        "job_title": "Generative AI Application Developer",
        "company": "Persistent Systems",
        "experience": "0-2 Years",
        "location": "Pune / Bengaluru",
        "skills": "Python, Generative AI, Large Language Models, LangChain, Hugging Face, FastAPI, Vector Databases",
        "description": "Build enterprise GenAI agents, RAG (Retrieval-Augmented Generation) architectures, and integrate LLM APIs into business workflows.",
        "role_category": "Machine Learning",
        "source": "LinkedIn"
    },
    {
        "job_title": "Business Intelligence Engineer",
        "company": "Target",
        "experience": "0-2 Years",
        "location": "Bengaluru",
        "skills": "SQL, Tableau, Power BI, Data Visualization, Data Analysis, Microsoft Excel, Statistics",
        "description": "Create executive dashboards, uncover retail sales trends, execute high volume SQL queries, and deliver actionable metric reports.",
        "role_category": "Data Analytics",
        "source": "Naukri"
    },
    {
        "job_title": "Backend Java Engineer",
        "company": "Oracle",
        "experience": "0-2 Years",
        "location": "Bengaluru",
        "skills": "Java, Spring Boot, MySQL, RESTful APIs, Microservices, Docker, Git, Data Structures & Algorithms",
        "description": "Develop scalable enterprise cloud microservices in Spring Boot, manage database transactions, and secure RESTful endpoints.",
        "role_category": "Software Engineering",
        "source": "Naukri"
    }
]

def init_job_database():
    """Create SQLite database, table and seed the initial clean dataset."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT NOT NULL,
        company TEXT NOT NULL,
        experience TEXT,
        location TEXT,
        skills TEXT NOT NULL,
        description TEXT,
        role_category TEXT,
        source TEXT
    )
    """)

    # Check if table already populated
    cursor.execute("SELECT COUNT(*) FROM jobs")
    count = cursor.fetchone()[0]

    if count == 0:
        for job in JOBS_DATA:
            cursor.execute("""
            INSERT INTO jobs (job_title, company, experience, location, skills, description, role_category, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                job["job_title"], job["company"], job["experience"], job["location"],
                job["skills"], job["description"], job["role_category"], job["source"]
            ))
        conn.commit()

    conn.close()

    # Also save to CSV
    df = pd.DataFrame(JOBS_DATA)
    df.to_csv(CSV_PATH, index=False)
    print(f"Database initialized at {DB_PATH} with {len(JOBS_DATA)} records.")
    print(f"CSV backup saved at {CSV_PATH}.")

def get_all_jobs() -> pd.DataFrame:
    """Load all jobs from SQLite into a pandas DataFrame."""
    if not os.path.exists(DB_PATH):
        init_job_database()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df

def get_job_roles_list():
    """Retrieve distinct job titles available for selection."""
    df = get_all_jobs()
    return sorted(df["job_title"].unique().tolist())

if __name__ == "__main__":
    init_job_database()
