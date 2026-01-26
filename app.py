import streamlit as st
from utils.config_loader import *


app_cfg = load_config("app.yaml")
experiences = load_config("experience.yaml")['experience']
projects = load_config("projects.yaml")['projects']
socials = load_config("profile.yaml")['socials']
skills = load_config("profile.yaml")['skills']

DESCRIPTION = load_config("profile.yaml")['description']


st.set_page_config(
    page_title=app_cfg["page"]["title"],
    page_icon=app_cfg["page"]["icon"]
)


load_main_css()

load_greeting_component()

load_profile_pic()

load_profile_description()

st.write("#")
st.subheader("Skills", divider=True, text_alignment="center")

for i in range(0, len(skills), 3):
    cols = st.columns(3, gap="small")
    for col, skill in zip(cols, skills[i:i + 3]):
        desc = load_skill(skill)
        col.markdown(
            desc,
            unsafe_allow_html=True
        )


st.write("#")
st.subheader("Experience", divider=True, text_alignment="center")

for experience in experiences:
    job_desc = load_job(experience)
    j = st.container()
    j.markdown(job_desc, unsafe_allow_html=True)



st.write("#")
st.subheader("Projects", divider=True, text_alignment="center")

for project in projects:
    desc = load_project(project)
    st.markdown(desc, unsafe_allow_html=True)



st.write("#")
st.subheader("Social Media", divider=True, text_alignment="center")

for i in range(0, len(socials), 2):
    cols = st.columns(2, gap="xxsmall", width="stretch")

    for col, social in zip(cols, socials[i:i+2]):
        desc = load_social(social)

        col.markdown(
            desc,
            unsafe_allow_html=True
        )


