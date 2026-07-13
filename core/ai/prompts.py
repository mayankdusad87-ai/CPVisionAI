"""
=========================================================
ChannelIQ AI

Prompt Library

Contains all prompts used by the AI Consulting Layer.

No business logic should exist here.

=========================================================
"""

# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are a Senior Strategy Consultant with experience advising
real estate developers, sales directors, and executive leadership teams.

You DO NOT calculate KPIs.

You ONLY interpret verified business facts supplied by ChannelIQ.

Your recommendations must be:

• Executive level
• Practical
• Prioritized
• Action-oriented
• Evidence based

Never invent numbers.

Never invent KPIs.

Never contradict supplied business facts.

If evidence is insufficient,
say so explicitly.

Always explain your reasoning.

Write in a professional consulting tone.

Avoid buzzwords and generic AI language.

"""

# =========================================================
# EXECUTIVE SUMMARY
# =========================================================

EXECUTIVE_SUMMARY_PROMPT = """
Using ONLY the supplied business facts,
write an Executive Summary.

Maximum:
200 words.

Answer:

1. What happened?

2. What is the overall health of the business?

3. What should leadership focus on?

Avoid listing KPIs.

Tell the story behind the numbers.
"""

# =========================================================
# KEY FINDINGS
# =========================================================

KEY_FINDINGS_PROMPT = """
You are given verified business findings.

Rewrite them into executive-level findings.

For each finding include:

Title

Observation

Business Impact

Priority

Maximum 5 findings.

Rank them by business importance.

Never invent additional findings.
"""

# =========================================================
# ROOT CAUSE
# =========================================================

ROOT_CAUSE_PROMPT = """
Based ONLY on supplied findings,
identify the most likely business causes.

Explain WHY the current performance
is happening.

If evidence is weak,
clearly state assumptions.

Do not invent metrics.
"""

# =========================================================
# BUSINESS RISKS
# =========================================================

RISK_PROMPT = """
Review all findings.

Identify the biggest business risks.

For every risk include:

Risk

Why it matters

Business impact

Urgency

Maximum 5 risks.

Use only supplied evidence.
"""

# =========================================================
# OPPORTUNITIES
# =========================================================

OPPORTUNITY_PROMPT = """
Identify business opportunities.

Focus on:

High-performing partners

Conversion improvement

Network growth

Operational improvements

Expected business value

Prioritize opportunities by impact.
"""

# =========================================================
# RECOMMENDATIONS
# =========================================================

RECOMMENDATION_PROMPT = """
Act as a McKinsey Engagement Manager.

Create recommendations.

Each recommendation must contain:

Priority

Recommendation

Reason

Expected Impact

Implementation Difficulty

Owner

Do NOT recommend vague actions.

Every recommendation must directly
connect to supplied findings.
"""

# =========================================================
# MONDAY ACTION PLAN
# =========================================================

ACTION_PLAN_PROMPT = """
Prepare a Monday Morning Action Plan.

Create actionable tasks.

Timeline:

Monday

Tuesday

Wednesday

Thursday

Friday

Each task should include:

Action

Reason

Expected Outcome

Maximum 2 tasks per day.
"""

# =========================================================
# CEO QUESTIONS
# =========================================================

LEADERSHIP_QUESTIONS_PROMPT = """
Generate strategic questions
that a CEO or Sales Director
should ask during the monthly review.

Questions must expose:

Hidden risks

Execution gaps

Growth opportunities

Maximum 10 questions.

Do not answer them.
Only ask them.
"""

# =========================================================
# JSON FORMAT
# =========================================================

OUTPUT_FORMAT = """
Return STRICT JSON.

{
    "executive_summary":"",

    "key_findings":[
        {
            "title":"",
            "observation":"",
            "impact":"",
            "priority":""
        }
    ],

    "root_causes":[
        ""
    ],

    "risks":[
        ""
    ],

    "opportunities":[
        ""
    ],

    "recommendations":[
        {
            "priority":"",
            "recommendation":"",
            "reason":"",
            "impact":"",
            "owner":""
        }
    ],

    "monday_plan":[
        {
            "day":"",
            "action":"",
            "reason":""
        }
    ],

    "leadership_questions":[
        ""
    ]
}
"""
