"""
Batch Placement Analyzer Module
Enables VVCE Placement Cell, HOD, and Mentors to analyze batch-wide readiness,
identify systemic skill deficits, and organize targeted technical bootcamps.
"""

from typing import List, Dict, Any
import numpy as np
import pandas as pd

def generate_sample_batch_data(n_students: int = 60) -> pd.DataFrame:
    """
    Generates a realistic batch dataset of 5th semester AIML students at VVCE.
    """
    np.random.seed(42)
    names = [
        "Sanjana B R", "Namith N", "Rohith S", "Aditya Sharma", "Ananya Hegde", 
        "Bhavana Gowda", "Chetan Kumar", "Darshan M", "Divya K", "Gagan Prasad",
        "Harshitha Rao", "Karthik V", "Kavya N", "Manoj K", "Meghana S",
        "Naveen Raj", "Nidhi Shetty", "Pooja Patil", "Prathiksha B", "Rahul Nayak",
        "Rakshith Gowda", "Sahana R", "Sanjay S", "Shashank M", "Sneha Joshi",
        "Suhas Bhat", "Tanvi Desai", "Varun Teja", "Vidya Sagar", "Yashaswini K"
    ]
    # Expand to n_students
    while len(names) < n_students:
        names.extend([f"Student_{i+1}" for i in range(len(names), n_students)])
    names = names[:n_students]
    
    usns = [f"4VV25CI{400 + i:03d}" for i in range(1, n_students + 1)]
    
    roles = [
        "Machine Learning Engineer", "Junior Data Scientist", "Data Analyst Intern / Associate", 
        "Python Developer", "Software Development Engineer (SDE-1)", "Full Stack Developer (MERN)",
        "DevOps & Cloud Engineer Associate"
    ]
    
    common_skills_pool = [
        "Python", "C++", "Java", "SQL", "HTML", "CSS", "Data Structures & Algorithms", 
        "DBMS", "Machine Learning", "Pandas", "NumPy", "Scikit-learn", "Git", "Power BI"
    ]
    
    data = []
    for i in range(n_students):
        name = names[i]
        usn = usns[i]
        cgpa = round(float(np.clip(np.random.normal(7.8, 0.9), 6.0, 9.8)), 2)
        target_role = np.random.choice(roles)
        # Sample number of skills student has
        k = np.random.randint(4, 11)
        skills_held = np.random.choice(common_skills_pool, size=k, replace=False).tolist()
        
        # Readines score roughly tied to CGPA and skills
        readiness = int(np.clip(35 + (cgpa - 6.0) * 10 + k * 4 + np.random.randint(-5, 6), 30, 96))
        
        status = "Ready for Placement" if readiness >= 75 else ("Moderately Ready" if readiness >= 55 else "Needs Preparation")
        
        data.append({
            "USN": usn,
            "Name": name,
            "CGPA": cgpa,
            "Target Role": target_role,
            "Skills": ", ".join(skills_held),
            "Readiness Score (%)": readiness,
            "Placement Status": status
        })
        
    return pd.DataFrame(data)

def compute_batch_statistics(batch_df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes summary metrics, readiness distribution, and most common skill gaps across the batch.
    """
    avg_readiness = round(batch_df["Readiness Score (%)"].mean(), 1)
    status_counts = batch_df["Placement Status"].value_counts().to_dict()
    role_counts = batch_df["Target Role"].value_counts().to_dict()
    
    # Calculate skill frequency across all students
    skill_frequency = {}
    for skills_str in batch_df["Skills"]:
        for s in str(skills_str).split(','):
            s_clean = s.strip()
            if s_clean:
                skill_frequency[s_clean] = skill_frequency.get(s_clean, 0) + 1
                
    total_students = len(batch_df)
    
    # Identify high-demand industry skills that are least held in batch (Skill Gaps)
    crucial_industry_skills = [
        "Docker", "AWS", "PyTorch", "Deep Learning", "Natural Language Processing", 
        "Scikit-learn", "Power BI", "RESTful APIs", "React.js", "CI/CD"
    ]
    
    batch_skill_gaps = []
    for skill in crucial_industry_skills:
        students_with_skill = skill_frequency.get(skill, 0)
        gap_percentage = round(((total_students - students_with_skill) / total_students) * 100, 1)
        batch_skill_gaps.append({
            "Skill": skill,
            "Students Possessing": students_with_skill,
            "Deficit Rate (%)": gap_percentage
        })
        
    batch_skill_gaps.sort(key=lambda x: x["Deficit Rate (%)"], reverse=True)
    
    return {
        "total_students": total_students,
        "average_readiness": avg_readiness,
        "status_counts": status_counts,
        "role_counts": role_counts,
        "batch_skill_gaps": batch_skill_gaps
    }
