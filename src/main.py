import os
from openai import OpenAI
from dotenv import load_dotenv

# ---------------------------------------------------------
# 1. CONFIGURATION & SETUP
# ---------------------------------------------------------

"""
Product Marketing Slogan Generator
Demonstrates reusable prompt templates for prompt engineering
using an OpenAI-compatible API (OpenRouter).
"""

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is missing. Please check your .env file.")

# Initialize OpenAI client (OpenRouter)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

MODEL = "openai/gpt-4o-mini"

# ---------------------------------------------------------
# 2. PROMPT TEMPLATE LIBRARY
# ---------------------------------------------------------

"""
Reusable prompts defining:
- Role
- Task
- Constraints
"""

prompt_templates = {
    "brand_minimal": """
Role: You are a professional brand strategist.
Task: Generate 3 minimal and memorable slogans for the product below.

Details:
- Product Name: {product}
- Intended Audience: {audience}
- Brand Tone: {tone}

Constraints:
- Maximum 8 words per slogan.
- Simple and clear language.
- Avoid exaggeration or false promises.
- Output as a numbered list.
""",

    "youth_marketing": """
Role: You are a creative digital marketer targeting young audiences.
Task: Create 3 catchy slogans suitable for social media promotion.

Details:
- Product Name: {product}
- Target Audience: {audience}
- Desired Tone: {tone}

Constraints:
- Can include emojis if appropriate.
- Energetic and engaging style.
- No misleading claims.
- Each slogan must be short and punchy.
- Output as a numbered list.
"""
}

# ---------------------------------------------------------
# 3. SLOGAN GENERATION FUNCTION
# ---------------------------------------------------------

def create_slogans(template_name, product, audience, tone):
    """
    Generates marketing slogans using a selected prompt template.
    """

    if template_name not in prompt_templates:
        return "Invalid template selected."

    prompt = prompt_templates[template_name].format(
        product=product,
        audience=audience,
        tone=tone
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Follow the instructions carefully and stay within constraints."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Error occurred: {error}"

# ---------------------------------------------------------
# 4. SAMPLE EXECUTION
# ---------------------------------------------------------

print("USE CASE 1: Fitness App Promotion\n")
print(create_slogans(
    template_name="youth_marketing",
    product="FitPulse App",
    audience="College Students",
    tone="Motivational, Fun, Energetic"
))

print("\n" + "=" * 45 + "\n")

print("USE CASE 2: Productivity Software\n")
print(create_slogans(
    template_name="brand_minimal",
    product="TaskFlow Pro",
    audience="Working Professionals",
    tone="Clean, Reliable, Professional"
))
