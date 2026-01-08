# Marketing Slogan Generator  
*(Prompt Engineering – Week 3 Assignment)*

This project showcases **prompt engineering concepts** by using a reusable
prompt library to generate short, creative marketing slogans for various
products and audiences.

The system demonstrates how well-structured prompts with clearly defined
roles, tasks, and constraints can be connected to an OpenAI-compatible API.

## ✨ Features

- Reusable prompt templates with **Role, Task, and Constraints**
- Dynamic variable insertion for:
  - Product name  
  - Target audience  
  - Tone  
- Integration with an **Azure OpenAI**
- Secure API key management using a `.env` file
- Multiple slogan styles using different prompt templates

## 🛠️ Tech Stack

- Python 3
- OpenAI Python SDK
- Azure OpenAI
- dotenv (for environment variable management)

## 🚀 Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Create a .env file:
    ```bash
    AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=endpoint
   AZURE_DEPLOYMENT_NAME=model name
3.  Run the script:
    ```bash
    python main.py