"""
Prompt Template Library
Stores reusable prompt formats for slogan generation.
"""

PROMPT_TEMPLATES = {
    "professional_branding": """
Role: You are a branding consultant.
Task: Generate 3 concise marketing slogans for the product below.

Details:
- Product Name: {product}
- Target Audience: {audience}
- Brand Tone: {tone}

Constraints:
- Max 8 words per slogan
- Clear and professional language
- No exaggerated claims
- Output as a numbered list
""",

    "social_campaign": """
Role: You are a social media marketing expert.
Task: Create 3 engaging slogans for online promotion.

Details:
- Product: {product}
- Audience: {audience}
- Tone: {tone}

Constraints:
- High-energy and catchy
- Emojis allowed if relevant
- Keep it short and impactful
- Avoid misleading statements
- Output as a numbered list
"""
}
