# SHL GenAI Assessment Recommendation Engine

## Problem Statement
Recommend suitable SHL assessments based on job requirements using GenAI techniques.

## Data
- SHL Product Catalogue (public, manually structured)
- Gen_AI Dataset.xlsx (provided by SHL for evaluation)

## Approach
1. Baseline TF-IDF recommender
2. GenAI embedding-based retrieval using Sentence Transformers


## How to Run
pip install -r requirements.txt  
streamlit run app.py



## Evaluation
Evaluation was performed using Recall@10 on the Train-Set, as it contains
ground-truth assessment URLs. The Test-Set contains query-only inputs and
was used solely for inference, reflecting a real-world retrieval scenario
where relevance labels are unavailable.
