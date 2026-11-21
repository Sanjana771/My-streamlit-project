"""
NLP Skill Extractor Module
Handles text cleaning, tokenization, phrase matching, and standardized skill extraction.
"""

import re
from typing import List, Set, Dict, Any
from .skill_taxonomy import SKILL_SYNONYMS, standardize_skill, get_skill_category

# Common English stop words
STOP_WORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", 
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", 
    "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", 
    "from", "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself", 
    "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", 
    "just", "me", "more", "most", "my", "myself", "no", "nor", "not", "of", "off", "on", 
    "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", 
    "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", 
    "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", 
    "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", 
    "when", "where", "which", "while", "who", "whom", "why", "with", "would", "you", 
    "your", "yours", "yourself", "yourselves"
}

def clean_text(raw_text: str) -> str:
    """Preprocess text by removing URLs, unusual characters, and normalizing whitespace."""
    if not raw_text:
        return ""
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', raw_text)
    # Remove email addresses
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', ' ', text)
    # Normalize common technical notations
    text = text.replace('/', ' / ')
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_skills_from_text(text: str) -> List[str]:
    """
    Extract technical skills from text using multi-word n-gram matching,
    regex boundary checks, and skill taxonomy normalization.
    """
    if not text:
        return []
    
    cleaned = clean_text(text).lower()
    detected_canonical = set()

    # Sort skill synonyms by length descending so multi-word skills like 'machine learning'
    # take precedence before matching single words
    sorted_patterns = sorted(SKILL_SYNONYMS.keys(), key=lambda x: len(x), reverse=True)

    for pattern in sorted_patterns:
        # Construct boundary-safe regex pattern
        escaped_pattern = re.escape(pattern)
        # Handle word boundaries (special handling for C++, C#, .js, etc.)
        regex = r'(?<![a-zA-Z0-9])' + escaped_pattern + r'(?![a-zA-Z0-9])'
        
        if re.search(regex, cleaned, re.IGNORECASE):
            canonical = standardize_skill(pattern)
            detected_canonical.add(canonical)
            # Mask the matched phrase to prevent redundant sub-matches
            cleaned = re.sub(regex, ' ', cleaned, flags=re.IGNORECASE)

    return sorted(list(detected_canonical))

def group_skills_by_category(skills: List[str]) -> Dict[str, List[str]]:
    """Group a list of extracted canonical skills by their technology category."""
    categorized = {}
    for skill in skills:
        cat = get_skill_category(skill)
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(skill)
    return categorized
