import yaml
from utils.paths import CONFIG_DIR, STYLES_DIR, ASSETS_DIR, PROFILE_PIC, CSS_FILE
import base64
from streamlit.components.v1 import html
from utils.templates import JOB_DESCRIPTION_TEMPLATE, PROJECT_DESCRIPTION_TEMPLATE
import streamlit as st

def load_main_css():
    with open(CSS_FILE) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

def load_config(filename: str) -> dict:
    path = CONFIG_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_image_data(image_path):
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

def get_resume_data(resume_path):
    PDF_byte = resume_path.read()
    return PDF_byte

def load_profile_description():
    DESCRIPTION = load_config("profile.yaml")['description']
    st.markdown(f'<div class="profile-card">{DESCRIPTION}</div>', unsafe_allow_html=True)

def load_greeting_component():
    with open(STYLES_DIR / "greeting.js") as f:
        greeting_js = f.read()

    with open(STYLES_DIR / "greeting.css") as f:
        greeting_css = f.read()

    html(f"""
    <style>
    {greeting_css}
    </style>

    <div class="hero">
    <div class="typing-container">
        <span class="typing" id="typing"></span>
    </div>
    </div>

    <script>
    {greeting_js}
    </script>
    """, height=150
    )

def load_profile_pic():
    prof_pic_data = get_image_data(PROFILE_PIC)
    prof_pic_html = f"""
    <div class="profile-img-container">
        <img src="data:image/png;base64,{prof_pic_data}" />
    </div>
    """
    st.markdown(prof_pic_html, unsafe_allow_html=True)

def load_job(experience: dict) -> str:
    description = experience["description"]
    role = experience["role"]
    company = experience["company"]
    period = experience["period"]
    color = experience["color"]

    final_description = JOB_DESCRIPTION_TEMPLATE.format(
        role=role, company=company, period=period
    )

    for desc in description.split("\n")[:-1]:
        final_description += f"\n- ➤ {desc.lstrip('-')}"

    return f"""<div class="job-card" style="border-left: 5px solid {color}">{final_description}</div>"""

def load_project(project: dict) -> str:
    desc = project["description"]
    link = project["link"]
    project_name = project["name"]
    final_description = PROJECT_DESCRIPTION_TEMPLATE.format(
        project_name=project_name,  link=link, desc=desc
    )
    return final_description

def load_social(social: dict) -> str:
    link = social["link"]
    platform = social["name"]
    icon_path = ASSETS_DIR / social["icon"]
    data = get_image_data(icon_path)

    final_description = f"""
    <div style="display:flex; justify-content:center;">
        <a href="{link}">
            <div class="social-img-container">
                <img src="data:image/png;base64,{data}" width="50"/>
                {platform}
            </div>
        </a>
    </div>
    """

    return final_description

def load_skill(skill: dict) -> str:
    name = skill["name"]
    icon_path = ASSETS_DIR / skill["icon"]
    data = get_image_data(icon_path)

    final_description = f"""
    <div class="skill-card">
        <img src="data:image/png;base64,{data}" width="50" />
        <p>{name}</p>
    </div>
    """

    return final_description