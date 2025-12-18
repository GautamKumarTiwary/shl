import streamlit as st
from src.embedding_recommender import recommend_embeddings

st.set_page_config(page_title="SHL GenAI Recommender", layout="centered")

st.title("SHL Assessment Recommendation Engine")

job_role = st.text_input("Job Role", placeholder="Automation Test Engineer")
skills = st.text_area("Required Skills", placeholder="Selenium, Automation Testing")
job_level = st.selectbox("Job Level", ["entry", "mid", "senior"])

if st.button("Recommend"):
    if not job_role.strip() and not skills.strip():
        st.warning(" Please enter Job Role or Skills")
    else:
        query = f"{job_role} {skills} {job_level}"
        st.write(" Searching relevant assessments...")

        results = recommend_embeddings(query, top_n=5)

        if results.empty:
            st.error("No recommendations found.")
        else:
            st.subheader("Recommended Assessments")
            for _, row in results.iterrows():
                st.markdown(
                    f"""
                    **{row['assessment_name']}**  
                    Category: {row['category']}  
                    Job Level: {row['job_level']}  
                    Score: `{row['score']:.2f}`  
                    Link: [View Assessment]({row['assessment_url']})
                    ---
                    """
                )
