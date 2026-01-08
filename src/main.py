import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from prompt_templates import PROMPT_TEMPLATES

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT_NAME")

if not API_KEY or not ENDPOINT:
    raise RuntimeError("Azure OpenAI credentials missing in .env")

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=ENDPOINT,
    api_version="2024-02-15-preview"
)

# ---------------------------------------------------------
# SLOGAN GENERATOR
# ---------------------------------------------------------

def generate_marketing_slogans(template_id, product, audience, tone):
    if template_id not in PROMPT_TEMPLATES:
        return "Invalid template selected."

    prompt_text = PROMPT_TEMPLATES[template_id].format(
        product=product,
        audience=audience,
        tone=tone
    )

    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT,
            messages=[
                {
                    "role": "system",
                    "content": "Follow instructions carefully and respect constraints."
                },
                {
                    "role": "user",
                    "content": prompt_text
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as err:
        return f"Error generating slogans: {err}"

# ---------------------------------------------------------
# DEMO EXECUTION
# ---------------------------------------------------------

if __name__ == "__main__":
    print("CASE 1: Fitness App\n")
    print(generate_marketing_slogans(
        "social_campaign",
        "ActiveBeat App",
        "University Students",
        "Fun, Motivational, Energetic"
    ))

    print("\n" + "-" * 50 + "\n")

    print("CASE 2: Business Tool\n")
    print(generate_marketing_slogans(
        "professional_branding",
        "WorkFlowX",
        "Corporate Professionals",
        "Reliable, Clean, Professional"
    ))

