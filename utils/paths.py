from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

ASSETS_DIR = BASE_DIR / "assets"
STYLES_DIR = BASE_DIR / "styles"
CONFIG_DIR = BASE_DIR / "config"

CSS_FILE = STYLES_DIR / "main.css"
RESUME_FILE = ASSETS_DIR / "CV.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic-small.PNG"


