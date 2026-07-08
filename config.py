"""
=========================================================
ChannelIQ AI
Global Configuration
Version : 2.0
=========================================================
"""

from pathlib import Path

# =========================================================
# APPLICATION
# =========================================================

APP_NAME = "ChannelIQ AI"

APP_TAGLINE = "AI-Powered Channel Partner Intelligence"

VERSION = "2.0.0"

PAGE_TITLE = APP_NAME

PAGE_ICON = "📊"

LAYOUT = "wide"

INITIAL_SIDEBAR_STATE = "expanded"

# =========================================================
# DIRECTORY STRUCTURE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

DATABASE_DIR = BASE_DIR / "database"

UPLOADS_DIR = BASE_DIR / "uploads"

EXPORTS_DIR = BASE_DIR / "exports"

REPORTS_DIR = BASE_DIR / "reports"

LOGS_DIR = BASE_DIR / "logs"

STYLE_FILE = ASSETS_DIR / "styles.css"

DB_PATH = DATABASE_DIR / "channeliq.db"

LOGO_PATH = ASSETS_DIR / "logo.png"

# Create folders automatically

# Create folders automatically

# Create writable directories

DIRECTORIES = [

    DATABASE_DIR,

    UPLOADS_DIR,

    EXPORTS_DIR,

    REPORTS_DIR,

    LOGS_DIR,

]

for folder in DIRECTORIES:

    try:

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        print(f"✓ Created/Verified: {folder}")

    except Exception as e:

        print(f"❌ Failed: {folder}")

        print(type(e).__name__)

        print(e)

        raise

# =========================================================
# FILES
# =========================================================

SUPPORTED_FILE_TYPES = [

    "xlsx",

    "xls",

    "csv"

]

MAX_UPLOAD_SIZE_MB = 50

# =========================================================
# BUSINESS SETTINGS
# =========================================================

DEFAULT_COMPANY = "Demo Builder"

DEFAULT_PROJECT = "Demo Project"

DEFAULT_CURRENCY = "₹"

AVERAGE_BOOKING_VALUE = 8000000

# =========================================================
# KPI SCORING WEIGHTS
# =========================================================

WEIGHTS = {

    "bookings": 0.40,

    "conversion": 0.35,

    "fresh": 0.25

}

# =========================================================
# SCORE THRESHOLDS
# =========================================================

CHAMPION_SCORE = 80

GROWTH_SCORE = 65

STABLE_SCORE = 50

WATCHLIST_SCORE = 35

# =========================================================
# RISK SCORE
# =========================================================

LOW_RISK = 30

MEDIUM_RISK = 60

HIGH_RISK = 80

CRITICAL_RISK = 90

# =========================================================
# COLORS
# =========================================================

PRIMARY = "#1E3A8A"

SECONDARY = "#2563EB"

SUCCESS = "#10B981"

WARNING = "#F59E0B"

DANGER = "#EF4444"

BACKGROUND = "#F5F7FB"

CARD = "#FFFFFF"

TEXT = "#111827"

SUBTEXT = "#64748B"

BORDER = "#E5E7EB"

# =========================================================
# CHARTS
# =========================================================

CHART_HEIGHT = 420

PLOT_TEMPLATE = "plotly_white"

# =========================================================
# AI SETTINGS
# =========================================================

AI_MODEL = "llama-3.3-70b-versatile"

AI_TEMPERATURE = 0.2

MAX_AI_TOKENS = 3000

SYSTEM_PROMPT = """
You are a senior management consultant specialising in
real estate channel partner performance.

Your role is to:

1. Analyse business performance

2. Identify trends

3. Explain WHY performance changed

4. Identify business risks

5. Identify revenue opportunities

6. Recommend actions ranked by impact

Always write in executive language.
"""

# =========================================================
# DATABASE
# =========================================================

DB_TIMEOUT = 30

# =========================================================
# DASHBOARD
# =========================================================

KPI_CARDS = [

    "Network Health",

    "Bookings",

    "Conversion",

    "Revenue Opportunity",

    "High Risk Partners",

    "Growth Rate"

]

# =========================================================
# HISTORY
# =========================================================

MAX_HISTORY = 100

# =========================================================
# EXPORT
# =========================================================

PPT_THEME = "Executive"

PDF_FONT = "Helvetica"

# =========================================================
# ANALYSIS
# =========================================================

AUTO_ANALYSE_AFTER_UPLOAD = True

SAVE_HISTORY = True

SAVE_AI_REPORT = True

# =========================================================
# DEBUG
# =========================================================

DEBUG = True

# =========================================================
# EXCEL TEMPLATE SETTINGS
# =========================================================

# Header is on Excel Row 4
EXCEL_HEADER_ROW = 4

# Actual data starts on Excel Row 5
EXCEL_DATA_START_ROW = 5
