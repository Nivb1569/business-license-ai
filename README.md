# business-license-ai

A tool for generating personalized regulatory reports for businesses based on Israeli Ministry of Health and Fire Department guidelines. This project parses regulatory documents, structures them into JSON, and uses OpenAI's models to provide customized insights based on specific business details.

---

## Project Goals

- Simplify the process of understanding health and fire regulations for new businesses.
- Automatically extract relevant clauses from official documents and convert them into a structured format.
- Use GPT to generate tailored summaries and tips for business owners.
- Minimize human error and time spent on reading complex legal texts.

---

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nivb1569/business-license-ai.git
   cd business-license-ai/backend

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Create .env file:**
    You need to manually create a `.env` file inside the `backend` folder. You can use this template as example:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
4. **Run:**
    ```bash
    python app.py
