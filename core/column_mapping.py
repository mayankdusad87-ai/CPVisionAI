"""
=========================================================
ChannelIQ AI

Column Mapping

Single source of truth for the ChannelIQ Excel Template.
If the Excel template changes, only this file should
require modification.
=========================================================
"""

# ==========================================================
# EXCEL COLUMN -> INTERNAL COLUMN
# ==========================================================

COLUMN_MAPPING = {

    "Form No": "form_no",

    "Date of Visit* (DD-MM-YYYY)": "visit_date",

    "First Name*": "first_name",

    "Last Name*": "last_name",

    "Mobile Number*": "mobile",

    "Visit Type": "visit_type",

    "Customer Fresh/Revisit": "customer_fresh_revisit",

    "Channel Partner Company*": "channel_partner",

    "Closing Manager*": "closing_manager",

    "Booking Date (DD-MM-YYYY)": "booking_date",

    "Booking Done (Y/N)": "booking_done"

    "Project Name": "project_name",

    "Source*": "source",

    "Budget*": "budget",

    "Preferred Configuration*": "configuration",
    
    "Month name": "reporting_period",

}

# ==========================================================
# REQUIRED COLUMNS
# ==========================================================

REQUIRED_COLUMNS = list(COLUMN_MAPPING.keys())

# ==========================================================
# BUSINESS VALUES
# ==========================================================

BUSINESS_VALUES = {

    "fresh": "Fresh",

    "unique_revisit": "Unique Revisit",

    "second_revisit": "Second Revisit",

    "third_revisit": "Third Revisit",

    "fourth_revisit": "Fourth Revisit",

    "revisit": "Revisit",

}

# ==========================================================
# INTERNAL COLUMN NAMES
# (Convenience Constants)
# ==========================================================

FORM_NO = "form_no"

VISIT_DATE = "visit_date"

CUSTOMER_NAME = "customer_name"

MOBILE = "mobile"

VISIT_TYPE = "visit_type"

CUSTOMER_FRESH_REVISIT = "customer_fresh_revisit"

CHANNEL_PARTNER = "channel_partner"

CLOSING_MANAGER = "closing_manager"

BOOKING_DATE = "booking_date"

BOOKING_DONE = "booking_done"

PROJECT_NAME = "project_name"

SOURCE = "source"

BUDGET = "budget"

CONFIGURATION = "configuration"

REPORTING_PERIOD = "reporting_period"
