"""
ChannelIQ AI
Global configuration for the application.
"""

from pathlib import Path

# ----------------------------------------------------
# APPLICATION
# ----------------------------------------------------

APP_NAME = "ChannelIQ AI"
APP_TAGLINE = "AI-Powered Channel Partner Intelligence"

VERSION = "2.0.0"

PAGE_TITLE = APP_NAME
PAGE_ICON = "📊"

# ----------------------------------------------------
# PROJECT PATHS
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
UPLOAD_DIR = BASE_DIR / "uploads"
EXPORT_DIR = BASE_DIR / "exports"
REPORT_DIR = BASE_DIR / "reports"
DATABASE_DIR = BASE_DIR / "database"

DB_FILE = DATABASE_DIR / "channeliq.db"

# Automatically create folders

for folder in [
    ASSETS_DIR,
    UPLOAD_DIR,
    EXPORT_DIR,
    REPORT_DIR,
    DATABASE_DIR,
]:
    folder.mkdir(exist_ok=True)

# ----------------------------------------------------
# THEME
# ----------------------------------------------------

PRIMARY_COLOR = "#1E3A8A"
SECONDARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#10B981"
WARNING_COLOR = "#F59E0B"
DANGER_COLOR = "#EF4444"

BACKGROUND_COLOR = "#F8FAFC"

CARD_RADIUS = 18

# ----------------------------------------------------
# DASHBOARD
# ----------------------------------------------------

DEFAULT_PAGE_SIZE = 20

MAX_UPLOAD_SIZE_MB = 50

SUPPORTED_FILES = [
    "xlsx",
    "xls",
    "csv",
]

# ----------------------------------------------------
# BUSINESS SETTINGS
# ----------------------------------------------------

DEFAULT_BOOKING_VALUE = 8000000

CURRENCY = "₹"

# Partner Score Weights

WEIGHTS = {
    "bookings": 0.40,
    "conversion": 0.35,
    "fresh": 0.25,
}

# Score Thresholds

CHAMPION_SCORE = 80
GROWTH_SCORE = 65
STABLE_SCORE = 50
WATCHLIST_SCORE = 35

# ----------------------------------------------------
# RISK SETTINGS
# ----------------------------------------------------

HIGH_RISK = 80
MEDIUM_RISK = 60
LOW_RISK = 40

# ----------------------------------------------------
# AI SETTINGS
# ----------------------------------------------------

AI_MODEL = "llama-3.3-70b-versatile"

AI_TEMPERATURE = 0.2

MAX_AI_TOKENS = 3000

# ----------------------------------------------------
# REPORT SETTINGS
# ----------------------------------------------------

PPT_THEME = "Executive"

PDF_FONT = "Helvetica"

# ----------------------------------------------------
# CHART SETTINGS
# ----------------------------------------------------

CHART_HEIGHT = 420

ENABLE_ANIMATIONS = True
