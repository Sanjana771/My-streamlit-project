"""
Matcher Module
Implements TF-IDF vectorization and Cosine Similarity calculation,
skill overlap comparison, and job ranking.
"""

from typing import List, Dict, Any, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .skill_taxonomy import standardize_skill

def compute_tfidf_similarity(text1: str, text2: str) -> float:
    """
    Computes cosine similarity between two texts using TF-IDF term weighting.
    Returns float in range [0.0, 1.0].
    """
    if not text1 or not text2:
        return 0.0
    
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    try:
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(np.clip(sim, 0.0, 1.0))
    except Exception:
        return 0.0

def compare_skills(student_skills: List[str], job_skills_str: str) -> Dict[str, Any]:
    """
    Compares candidate skills with required job skills.
    Returns matched skills, missing skills, and match percentage.
    """
    student_set = {standardize_skill(s) for s in student_skills}
    
    # Split comma-separated job skills
    raw_job_skills = [s.strip() for s in job_skills_str.split(',') if s.strip()]
    job_set = {standardize_skill(s) for s in raw_job_skills}
    
    matched = sorted(list(student_set.intersection(job_set)))
    missing = sorted(list(job_set.difference(student_set)))
    
    total_required = len(job_set) if len(job_set) > 0 else 1
    skill_match_pct = round((len(matched) / total_required) * 100, 1)
    
    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "matched_count": len(matched),
        "total_required": len(job_set),
        "skill_match_percentage": skill_match_pct
    }

def calculate_overall_match(resume_text: str, student_skills: List[str], job_row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Combines skill-taxonomy exact match with TF-IDF context similarity
    to produce a robust placement match percentage.
    """
    skill_comp = compare_skills(student_skills, job_row["skills"])
    
    # Contextual TF-IDF between full resume and full job description + skills
    job_full_text = f"{job_row['job_title']} {job_row['skills']} {job_row.get('description', '')}"
    tfidf_sim = compute_tfidf_similarity(resume_text, job_full_text)
    tfidf_pct = round(tfidf_sim * 100, 1)
    
    # Weighted composite score: 65% skills overlap + 35% semantic TF-IDF
    composite_pct = round((skill_comp["skill_match_percentage"] * 0.65) + (tfidf_pct * 0.35), 1)
    composite_pct = min(100.0, max(0.0, composite_pct))
    
    return {
        "job_id": job_row.get("id", 0),
        "job_title": job_row["job_title"],
        "company": job_row["company"],
        "location": job_row.get("location", "India"),
        "experience": job_row.get("experience", "Fresher"),
        "role_category": job_row.get("role_category", "Tech"),
        "description": job_row.get("description", ""),
        "required_skills": job_row["skills"],
        "matched_skills": skill_comp["matched_skills"],
        "missing_skills": skill_comp["missing_skills"],
        "skill_match_percentage": skill_comp["skill_match_percentage"],
        "tfidf_similarity_percentage": tfidf_pct,
        "overall_match_percentage": composite_pct
    }

def rank_jobs(resume_text: str, student_skills: List[str], jobs_df) -> List[Dict[str, Any]]:
    """
    Evaluates and ranks all jobs in the database against the student's profile.
    """
    results = []
    for _, row in jobs_df.iterrows():
        match_info = calculate_overall_match(resume_text, student_skills, row.to_dict())
        results.append(match_info)
        
    # Sort descending by overall match percentage
    results.sort(key=lambda x: x["overall_match_percentage"], reverse=True)
    return results
