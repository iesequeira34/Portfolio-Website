from pathlib import Path
import streamlit as st
from PIL import Image
import base64

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic-small.PNG"
linkedin_logo = current_dir / "assets" / "linkedin-logo.png"

PAGE_TITLE = "Digital CV | Ian Sequeira"

PAGE_ICON = ":computer:"

NAME = "Ian Sequeira"

DESCRIPTION = """Machine Learning Engineer building scalable, agentic AI systems using LLMs,
reinforcement learning, and multimodal models. Experienced in deploying
Generative AI solutions for NLP, vision, and structured data tasks. Skilled in cloudnative development, model optimization, and ethical AI deployment. Focused on
aligning ML with business goals to drive intelligent automation and real-world
impact."""

EMAIL = "iesequeira34@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ian-sequeira-94b924204/",
    "GitHub": "https://github.com/iesequeira34",
    "Email": "mailto:iesequeira34@gmail.com",
    "Phone": "tel:+919769007256"
}

PROJECTS = {
    "Crop Yield Prediction": "https://github.com/iesequeira34/Crop-Yield-Prediction",
    "Paddy Disease Classification": "https://github.com/iesequeira34/Agricare",
}

PROJECT_DESC = {
    "Crop Yield Prediction": """The XGBoost Regressor Model was used to estimate crop yield losses and based on this, the production of Rice
and Wheat in certain states of India was estimated. This was implemented in a web application using HTML5,
CSS 3, Flask, and JavaScript.
""",
    "Paddy Disease Classification": """Designed a high-accuracy (97%) disease classification system using a cascading U-Net and CNN
architecture. Improved agricultural decision-making by enabling early detection of crop diseases, optimizing
yield protection strategies for farmers.""",
}

ICON_PATHS = {
    "LinkedIn": "assets/linkedin-logo.png",
    "GitHub": "assets/github-icon.png",
    "Email": "assets/email-icon.png",
    "Phone": "assets/phone-icon.png"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)

# with open(resume_file, "rb") as pdf_file:
#     PDF_byte = pdf_file.read()

profile_pic = Image.open(profile_pic_path)

st.markdown('<div class="greeting">👋 Hello, I\'m Ian Sequeira!</div>', unsafe_allow_html=True)
st.write("#")




with open("assets/profile-pic-small.png", "rb") as f:
    data = base64.b64encode(f.read()).decode()



st.markdown(f"""
<div class="profile-img-container">
    <img src="data:image/png;base64,{data}" />
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="profile-card">{DESCRIPTION}</div>', unsafe_allow_html=True)


st.write("#")
st.subheader("Experience", divider=True, text_alignment="center")

j1 = st.container()
PWC_DESC = """
<h3>Machine Learning Engineer | PwC India</h3>
<p><strong><i>July 2023 - June 2025</i></strong></p>
<hr />


- ➤ Engineered end-to-end ML pipeline for complaint management at
India's largest private bank, orchestrating Azure cloud services (VMs,
SQL Database, Blob Storage, Key Vault) in a microservices architecture
for scalable ML inference.

- ➤ Trained and deployed fine-tuned LLMs for NLP tasks including
sentiment analysis, topic modelling, fraud detection, achieving 40%
reduction in triage time through automated classification and root
cause analysis.

- ➤ Built real-time analytics infrastructure with Power BI dashboards
consuming ML outputs, enabling data-driven operations decisions
through automated reporting pipelines.

- ➤ Built feedback loops for LLM fine-tuning via user corrections, improving
model accuracy by 25%.
- Automated production monitoring for model health checks, data
quality validation, and system diagnostics, ensuring reliable ML
operations.

- ➤ Secured AI infrastructure investment by presenting a data-driven
cost-benefit case to senior leadership.

- ➤ Led AI enablement sessions to upskill developers on ML tools, Linux
systems, and Azure-based deployment workflows.
"""
j1.markdown("""
<div class="job-card" style="border-left: 5px solid orange">
{PWC_DESC}
</div>""".format(PWC_DESC=PWC_DESC), unsafe_allow_html=True)
# j1.write()


j2 = st.container()
JK_DESC = """
<h3>Data Science Intern | JK Cement Ltd.</h3>
<p><strong><i>October 2022 - June 2023</i></strong></p>
<hr />

- ➤ Developed a predictive model for ascertaining appropriate fan speeds
to be applied by Operators using random forest models for a Waste
Heat Recovery System which reduced heat energy requirements by
16%.

- ➤ Optimized cement manufacturing by training XGBoost models,
reducing specific heat of the clinker mix and thus reducing the heat
energy required in the manufacturing process by 20%.
"""
j2.markdown(f"""<div class="job-card" style="border-left: 5px solid green">{JK_DESC}</div>""", unsafe_allow_html=True)

j3 = st.container()
NEC_DESC = """
<h3>Web Development Intern | NEC Corporation</h3>
<p><strong><i>June 2021 - September 2021</i></strong></p>
<hr />


- ➤ Created REST APIs for internal transportation management, enabling
seamless employee and client access.

- ➤ Designed and integrated a COVID-19 portal with Microsoft SharePoint
for efficient data management and visualization.

- ➤ Programmed an automated email notification system for talent show
results, enhancing event management efficiency.
"""
j3.markdown(f"""<div class="job-card" style="border-left: 5px solid blue">{NEC_DESC}</div>""", unsafe_allow_html=True)

st.write("#")
st.subheader("Projects", divider=True, text_alignment="center")

for project, link in PROJECTS.items():
    desc = PROJECT_DESC[project]
    st.markdown(f"""<div class="job-card" style="border-left: 5px solid">
<h5><u><a href="{link}">{project}</a></u></h5>
{desc}
</div>""", unsafe_allow_html=True)

st.write("#")
st.subheader("Socials", divider=True, text_alignment="center")
cols = st.columns(len(SOCIAL_MEDIA), vertical_alignment="center", gap="medium")

for col, (platform, link) in zip(cols, SOCIAL_MEDIA.items()):
    icon_path = ICON_PATHS[platform]

    with open(icon_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    col.markdown(
        f"""
        <div style="text-align: center;">
            <a href="{link}">
                <img src="data:image/png;base64,{data}" width="36"/>
            </a>
            <p>
            {platform}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


