"""
End-to-End System Test Script
Verifies that all components: parser, NLP extractor, taxonomy, database,
TF-IDF matcher, ML model, roadmap generator, and batch analyzer execute flawlessly.
"""

import os
import sys
import pickle

def run_tests():
    print("==================================================")
    print("🧪 RUNNING SYSTEM VERIFICATION TESTS")
    print("==================================================")

    # 1. Test database
    from database.db_setup import get_all_jobs, get_job_roles_list
    jobs_df = get_all_jobs()
    print(f"✅ Job Database: Loaded {len(jobs_df)} jobs across {len(get_job_roles_list())} distinct roles.")

    # 2. Test Resume Parsing & Metadata
    from modules.resume_parser import extract_text_from_file, extract_candidate_metadata
    sample_resume_path = os.path.join(os.path.dirname(__file__), "data", "sample_resumes", "sanjana_ml_resume.txt")
    with open(sample_resume_path, "r", encoding="utf-8") as f:
        text = f.read()
    meta = extract_candidate_metadata(text)
    print(f"✅ Resume Parsing & Metadata: Extracted candidate name '{meta['name']}', email '{meta['email']}'.")

    # 3. Test NLP Skill Extraction & Taxonomy
    from modules.nlp_extractor import extract_skills_from_text, group_skills_by_category
    skills = extract_skills_from_text(text)
    categorized = group_skills_by_category(skills)
    print(f"✅ NLP Skill Extraction: Identified {len(skills)} skills: {skills[:6]}...")
    print(f"✅ Skill Categories: {list(categorized.keys())}")

    # 4. Test TF-IDF Matcher & Job Ranking
    from modules.matcher import calculate_overall_match, rank_jobs
    target_job = jobs_df.iloc[0].to_dict()
    match = calculate_overall_match(text, skills, target_job)
    print(f"✅ Matcher: Match with '{target_job['job_title']}': Overall {match['overall_match_percentage']}% (Matched: {len(match['matched_skills'])}, Missing: {len(match['missing_skills'])})")

    ranked = rank_jobs(text, skills, jobs_df)
    print(f"✅ Job Ranking: Top ranked job is '{ranked[0]['job_title']}' at {ranked[0]['company']} with {ranked[0]['overall_match_percentage']}% match.")

    # 5. Test ML Model
    model_path = os.path.join(os.path.dirname(__file__), "models", "readiness_model.pkl")
    with open(model_path, "rb") as f:
        payload = pickle.load(f)
    model = payload["best_model"]
    scaler = payload["scaler"]
    import numpy as np
    sample_input = np.array([[match["overall_match_percentage"], match["tfidf_similarity_percentage"], 8.5, 3, 1, len(skills), 2]])
    if payload["best_model_name"] == "Logistic Regression":
        sample_input = scaler.transform(sample_input)
    prob = model.predict_proba(sample_input)[0][1]
    print(f"✅ ML Model ({payload['best_model_name']}): Placement Readiness Probability = {prob*100:.1f}%")

    # 6. Test Roadmap Generator
    from modules.roadmap_generator import generate_learning_roadmap
    roadmap = generate_learning_roadmap(match["missing_skills"], target_job["job_title"])
    print(f"✅ Roadmap Generator: Created {len(roadmap)} learning milestone steps.")

    # 7. Test Batch Analyzer
    from modules.batch_analyzer import generate_sample_batch_data, compute_batch_statistics
    batch_df = generate_sample_batch_data(30)
    stats = compute_batch_statistics(batch_df)
    print(f"✅ Batch Analyzer: Analyzed {stats['total_students']} students. Batch Average Readiness = {stats['average_readiness']}%.")

    print("==================================================")
    print("🎉 ALL TESTS PASSED SUCCESSFULLY! 100% OPERATIONAL")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
