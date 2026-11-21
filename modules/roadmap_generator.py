"""
Personalized Roadmap Generator Module
Synthesizes a structured step-by-step learning path tailored to the student's missing skills
and chosen target role, including practical portfolio projects and interview preparation tips.
"""

from typing import List, Dict, Any

# Curated repository of skill roadmaps, resources, and project recommendations
SKILL_ROADMAP_DATA = {
    "Pandas": {
        "stage": "Data Wrangling & Manipulation",
        "priority": 1,
        "topics": ["Series & DataFrames", "Data Cleaning & Imputation", "GroupBy & Aggregations", "Merging & Joins"],
        "recommended_resource": "Kaggle Pandas Micro-Course / Official Docs",
        "project": "Build an Automated Exploratory Data Analysis (EDA) tool for campus placement data",
        "estimated_hours": 10
    },
    "NumPy": {
        "stage": "Numerical Computing Foundations",
        "priority": 1,
        "topics": ["N-d Arrays", "Vectorization & Broadcasting", "Linear Algebra operations", "Random sampling"],
        "recommended_resource": "NumPy Quickstart Tutorial",
        "project": "Implement Matrix Factorization and basic neural network layers from scratch using pure NumPy",
        "estimated_hours": 8
    },
    "Scikit-learn": {
        "stage": "Applied Machine Learning",
        "priority": 2,
        "topics": ["Pipelines & Transformers", "Classification & Regression", "Cross-Validation & Hyperparameter Tuning", "Model Evaluation Metrics"],
        "recommended_resource": "Scikit-Learn Official User Guide / Hands-On ML (Geron)",
        "project": "Student Placement Prediction model with Streamlit UI and Confusion Matrix visualization",
        "estimated_hours": 15
    },
    "Machine Learning": {
        "stage": "Core ML Algorithms",
        "priority": 2,
        "topics": ["Supervised Learning (Regression, Trees, Ensemble)", "Unsupervised Learning (K-Means, PCA)", "Bias-Variance Tradeoff", "Feature Engineering"],
        "recommended_resource": "Andrew Ng Machine Learning Specialization (Coursera / Stanford)",
        "project": "End-to-End Customer Churn or Real Estate Price Predictor with deployment",
        "estimated_hours": 25
    },
    "Deep Learning": {
        "stage": "Neural Networks & Representation Learning",
        "priority": 3,
        "topics": ["Multi-Layer Perceptrons", "Backpropagation & Optimizers", "CNNs for Image Classification", "RNNs/LSTMs for Sequences"],
        "recommended_resource": "DeepLearning.AI Specialization / Fast.ai Practical Deep Learning",
        "project": "Medical Disease / Chest X-ray classification using Transfer Learning (ResNet / MobileNet)",
        "estimated_hours": 30
    },
    "PyTorch": {
        "stage": "Deep Learning Frameworks",
        "priority": 3,
        "topics": ["Tensors & Autograd", "Custom nn.Module & Datasets", "Training loops & GPU acceleration", "Torchvision models"],
        "recommended_resource": "PyTorch 60-Minute Blitz & Official Tutorials",
        "project": "Custom Vision Classifier with PyTorch Lightning and model export to ONNX",
        "estimated_hours": 20
    },
    "TensorFlow": {
        "stage": "Deep Learning Frameworks",
        "priority": 3,
        "topics": ["Keras Sequential & Functional APIs", "TensorFlow Data Pipelines (tf.data)", "Callbacks & TensorBoard", "TF Serving"],
        "recommended_resource": "TensorFlow in Practice Specialization",
        "project": "Image classification and real-time webcam inference using TF.js / TFLite",
        "estimated_hours": 20
    },
    "Natural Language Processing": {
        "stage": "Language Intelligence",
        "priority": 3,
        "topics": ["Text Preprocessing & Regex", "TF-IDF & Word Embeddings (Word2Vec)", "Sequence tagging & NER", "Transformer Attention"],
        "recommended_resource": "Hugging Face NLP Course / Stanford CS224N",
        "project": "Automated Resume Screening and Skill Matching Engine with Semantic Search",
        "estimated_hours": 25
    },
    "Large Language Models": {
        "stage": "Generative AI & LLMs",
        "priority": 4,
        "topics": ["Prompt Engineering", "RAG (Retrieval Augmented Generation)", "Vector Databases (Chroma/FAISS)", "LangChain / LlamaIndex"],
        "recommended_resource": "DeepLearning.AI Short Courses on LLMs & LangChain",
        "project": "Build an intelligent Q&A Chatbot over College Syllabus PDFs using RAG & Ollama/Gemini",
        "estimated_hours": 20
    },
    "Computer Vision": {
        "stage": "Visual Perception Systems",
        "priority": 3,
        "topics": ["Image Processing with OpenCV", "Object Detection (YOLO)", "Face Recognition", "Image Segmentation"],
        "recommended_resource": "PyImageSearch / OpenCV Tutorials",
        "project": "Automated Classroom Attendance System using Real-Time Face Recognition",
        "estimated_hours": 22
    },
    "SQL": {
        "stage": "Database Querying & Management",
        "priority": 1,
        "topics": ["Complex Joins & Subqueries", "Window Functions (RANK, DENSE_RANK, LEAD, LAG)", "Indexing & Query Optimization", "Stored Procedures"],
        "recommended_resource": "Mode Analytics SQL Tutorial / LeetCode SQL 50",
        "project": "Design and optimize a College Placement Portal relational schema in PostgreSQL/MySQL",
        "estimated_hours": 15
    },
    "Power BI": {
        "stage": "Business Intelligence & Reporting",
        "priority": 2,
        "topics": ["Power Query & Data Cleaning", "DAX Formulas & Measures", "Interactive Dashboards", "Data Modeling (Star Schema)"],
        "recommended_resource": "Microsoft Learn Power BI Data Analyst Path",
        "project": "Interactive Executive Dashboard tracking VVCE Placement Statistics by Company and Branch",
        "estimated_hours": 12
    },
    "Tableau": {
        "stage": "Visual Analytics",
        "priority": 2,
        "topics": ["Calculated Fields & LOD Expressions", "Dual Axis Charts & Heatmaps", "Dashboard Actions & Stories", "Publishing to Tableau Public"],
        "recommended_resource": "Tableau Free Training Videos",
        "project": "Global Tech Hiring Trends and Salary Benchmarking Visual Dashboard",
        "estimated_hours": 12
    },
    "React.js": {
        "stage": "Modern Frontend Engineering",
        "priority": 2,
        "topics": ["Components & Props", "Hooks (useState, useEffect, useMemo)", "State Management (Redux/Context)", "API Integration"],
        "recommended_resource": "React.dev Official Interactive Docs",
        "project": "Full-Featured Student Job Board with filtering, bookmarks, and application tracking",
        "estimated_hours": 20
    },
    "Node.js": {
        "stage": "Backend Engineering",
        "priority": 2,
        "topics": ["Event Loop & Async I/O", "Express.js REST APIs", "Middleware & JWT Authentication", "Database Integration (Mongoose/Prisma)"],
        "recommended_resource": "Node.js & Express by FreeCodeCamp",
        "project": "Secure Student Authentication & Placement Application Management API",
        "estimated_hours": 18
    },
    "Docker": {
        "stage": "DevOps & Containerization",
        "priority": 3,
        "topics": ["Dockerfile syntax & Multi-Stage Builds", "Docker Compose for Multi-Container Apps", "Networking & Volumes", "Pushing to Docker Hub"],
        "recommended_resource": "Docker for Beginners (TechWorld with Nana)",
        "project": "Containerize full-stack ML application (Streamlit + FastAPI + SQLite) with Docker Compose",
        "estimated_hours": 10
    },
    "AWS": {
        "stage": "Cloud Infrastructure",
        "priority": 3,
        "topics": ["EC2 & S3 Basics", "AWS Lambda & API Gateway", "IAM Roles & Security Groups", "Deploying ML Models on Cloud"],
        "recommended_resource": "AWS Cloud Practitioner Essentials",
        "project": "Deploy an automated resume scoring serverless API with AWS Lambda & S3",
        "estimated_hours": 15
    },
    "Data Structures & Algorithms": {
        "stage": "Core CS & Placement Problem Solving",
        "priority": 1,
        "topics": ["Arrays, Strings & Two Pointers", "Hashing, Linked Lists, Stacks & Queues", "Trees & Graphs (BFS/DFS)", "Dynamic Programming"],
        "recommended_resource": "Striver's SDE Sheet / NeetCode 150 / LeetCode",
        "project": "Solve and document top 100 campus placement interview coding questions on GitHub",
        "estimated_hours": 40
    }
}

def generate_learning_roadmap(missing_skills: List[str], target_role: str) -> List[Dict[str, Any]]:
    """
    Generates an ordered step-by-step learning roadmap for missing skills.
    """
    roadmap = []
    
    # Process each missing skill
    for skill in missing_skills:
        info = SKILL_ROADMAP_DATA.get(skill)
        if info:
            roadmap.append({
                "skill": skill,
                "stage": info["stage"],
                "priority": info["priority"],
                "topics": info["topics"],
                "resource": info["recommended_resource"],
                "project": info["project"],
                "estimated_hours": info["estimated_hours"]
            })
        else:
            # Fallback for other skills
            roadmap.append({
                "skill": skill,
                "stage": "Specialized Competency",
                "priority": 3,
                "topics": [f"{skill} Core Syntax & Patterns", f"{skill} Best Practices", f"Real-world application of {skill}"],
                "resource": f"Official documentation and tutorials for {skill}",
                "project": f"Build a practical mini-project integrating {skill} into your tech portfolio",
                "estimated_hours": 12
            })
            
    # Sort roadmap by priority order (Foundations -> Intermediate -> Advanced)
    roadmap.sort(key=lambda x: x["priority"])
    return roadmap
