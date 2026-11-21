"""
Skill Taxonomy Module
Standardizes and normalizes technical skills based on ESCO and O*NET taxonomies.
Maps variants, misspellings, and synonymous skill names to unified canonical skills.
"""

# Canonical skill mapping: mapping variant tokens/synonyms to standard canonical name
SKILL_SYNONYMS = {
    # Programming Languages
    "python": "Python",
    "python3": "Python",
    "py": "Python",
    "python programming": "Python",
    "java": "Java",
    "core java": "Java",
    "java 8": "Java",
    "advanced java": "Java",
    "c++": "C++",
    "cpp": "C++",
    "c": "C",
    "c programming": "C",
    "c#": "C#",
    "c sharp": "C#",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "es6": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "r": "R",
    "r programming": "R",
    "go": "Go",
    "golang": "Go",
    "rust": "Rust",
    "kotlin": "Kotlin",
    "scala": "Scala",
    "php": "PHP",
    "ruby": "Ruby",
    "dart": "Dart",
    "swift": "Swift",

    # AI, ML & Data Science
    "machine learning": "Machine Learning",
    "ml": "Machine Learning",
    "deep learning": "Deep Learning",
    "dl": "Deep Learning",
    "nlp": "Natural Language Processing",
    "natural language processing": "Natural Language Processing",
    "computer vision": "Computer Vision",
    "cv": "Computer Vision",
    "artificial intelligence": "Artificial Intelligence",
    "ai": "Artificial Intelligence",
    "scikit-learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "tensorflow": "TensorFlow",
    "tf": "TensorFlow",
    "pytorch": "PyTorch",
    "torch": "PyTorch",
    "keras": "Keras",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scipy": "SciPy",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "plotly": "Plotly",
    "opencv": "OpenCV",
    "cv2": "OpenCV",
    "xgboost": "XGBoost",
    "lightgbm": "LightGBM",
    "catboost": "CatBoost",
    "huggingface": "Hugging Face",
    "hugging face": "Hugging Face",
    "transformers": "Transformers",
    "llm": "Large Language Models",
    "llms": "Large Language Models",
    "large language models": "Large Language Models",
    "generative ai": "Generative AI",
    "genai": "Generative AI",
    "langchain": "LangChain",
    "spacy": "spaCy",
    "nltk": "NLTK",

    # Data Engineering & Analytics
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL",
    "plsql": "PL/SQL",
    "pl/sql": "PL/SQL",
    "sqlite": "SQLite",
    "mongodb": "MongoDB",
    "mongo": "MongoDB",
    "redis": "Redis",
    "cassandra": "Cassandra",
    "data analysis": "Data Analysis",
    "data analytics": "Data Analysis",
    "data visualization": "Data Visualization",
    "power bi": "Power BI",
    "powerbi": "Power BI",
    "tableau": "Tableau",
    "excel": "Microsoft Excel",
    "advanced excel": "Microsoft Excel",
    "ms excel": "Microsoft Excel",
    "spark": "Apache Spark",
    "apache spark": "Apache Spark",
    "pyspark": "PySpark",
    "hadoop": "Apache Hadoop",
    "kafka": "Apache Kafka",
    "etl": "ETL",
    "statistics": "Statistics",
    "statistical modeling": "Statistics",

    # Web & Full Stack Development
    "html": "HTML",
    "html5": "HTML",
    "css": "CSS",
    "css3": "CSS",
    "bootstrap": "Bootstrap",
    "tailwind": "Tailwind CSS",
    "tailwind css": "Tailwind CSS",
    "react": "React.js",
    "react.js": "React.js",
    "reactjs": "React.js",
    "angular": "Angular",
    "angularjs": "Angular",
    "vue": "Vue.js",
    "vue.js": "Vue.js",
    "vuejs": "Vue.js",
    "node": "Node.js",
    "node.js": "Node.js",
    "nodejs": "Node.js",
    "express": "Express.js",
    "express.js": "Express.js",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "spring": "Spring Boot",
    "spring boot": "Spring Boot",
    "rest api": "RESTful APIs",
    "rest apis": "RESTful APIs",
    "restful api": "RESTful APIs",
    "graphql": "GraphQL",

    # Cloud & DevOps
    "aws": "AWS",
    "amazon web services": "AWS",
    "azure": "Microsoft Azure",
    "microsoft azure": "Microsoft Azure",
    "gcp": "Google Cloud Platform",
    "google cloud": "Google Cloud Platform",
    "google cloud platform": "Google Cloud Platform",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "k8s": "Kubernetes",
    "ci/cd": "CI/CD",
    "cicd": "CI/CD",
    "jenkins": "Jenkins",
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "linux": "Linux",
    "unix": "Linux",
    "bash": "Bash/Shell Scripting",
    "shell": "Bash/Shell Scripting",
    "terraform": "Terraform",
    "ansible": "Ansible",

    # Core Computer Science
    "data structures": "Data Structures & Algorithms",
    "algorithms": "Data Structures & Algorithms",
    "dsa": "Data Structures & Algorithms",
    "data structures and algorithms": "Data Structures & Algorithms",
    "oop": "Object-Oriented Programming",
    "oops": "Object-Oriented Programming",
    "object oriented programming": "Object-Oriented Programming",
    "dbms": "DBMS",
    "database management": "DBMS",
    "os": "Operating Systems",
    "operating systems": "Operating Systems",
    "computer networks": "Computer Networks",
    "networking": "Computer Networks",
    "system design": "System Design",
    "software engineering": "Software Engineering"
}

# Categorization of skills for visual radar charts and gap breakdown
SKILL_CATEGORIES = {
    "Programming Languages": [
        "Python", "Java", "C++", "C", "C#", "JavaScript", "TypeScript", 
        "R", "Go", "Rust", "Kotlin", "Scala", "PHP", "Ruby", "Dart", "Swift"
    ],
    "AI & Machine Learning": [
        "Machine Learning", "Deep Learning", "Natural Language Processing", 
        "Computer Vision", "Artificial Intelligence", "Scikit-learn", 
        "TensorFlow", "PyTorch", "Keras", "Pandas", "NumPy", "SciPy", 
        "OpenCV", "XGBoost", "LightGBM", "CatBoost", "Hugging Face", 
        "Transformers", "Large Language Models", "Generative AI", 
        "LangChain", "spaCy", "NLTK"
    ],
    "Data & Analytics": [
        "SQL", "MySQL", "PostgreSQL", "PL/SQL", "SQLite", "MongoDB", "Redis", 
        "Cassandra", "Data Analysis", "Data Visualization", "Power BI", 
        "Tableau", "Microsoft Excel", "Apache Spark", "PySpark", 
        "Apache Hadoop", "Apache Kafka", "ETL", "Statistics", "Matplotlib", 
        "Seaborn", "Plotly"
    ],
    "Web & Full Stack": [
        "HTML", "CSS", "Bootstrap", "Tailwind CSS", "React.js", "Angular", 
        "Vue.js", "Node.js", "Express.js", "Django", "Flask", "FastAPI", 
        "Spring Boot", "RESTful APIs", "GraphQL"
    ],
    "Cloud & DevOps": [
        "AWS", "Microsoft Azure", "Google Cloud Platform", "Docker", 
        "Kubernetes", "CI/CD", "Jenkins", "Git", "GitHub", "GitLab", 
        "Linux", "Bash/Shell Scripting", "Terraform", "Ansible"
    ],
    "Core CS & Foundations": [
        "Data Structures & Algorithms", "Object-Oriented Programming", 
        "DBMS", "Operating Systems", "Computer Networks", "System Design", 
        "Software Engineering"
    ]
}

def standardize_skill(skill_raw: str) -> str:
    """Normalize a raw skill string to its canonical taxonomy name."""
    cleaned = skill_raw.strip().lower()
    return SKILL_SYNONYMS.get(cleaned, skill_raw.strip().title())

def get_skill_category(skill_canonical: str) -> str:
    """Return the primary category for a canonical skill."""
    for category, skills in SKILL_CATEGORIES.items():
        if skill_canonical in skills:
            return category
    return "Other Technical Skills"
