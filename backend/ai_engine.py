import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_report(user_profile, matched_rules):
    rules_text = "\n".join(
        [f"{idx + 1}. {rule['condition']}" for idx, rule in enumerate(matched_rules)]
    )

    prompt = f"""
You are an expert in Israeli business licensing and regulations.

A small business owner is asking for a personalized, clear, and practical summary of the regulations that apply to their business, based on the following profile:
- Size: {user_profile['size_sqm']} sqm
- Serves meat: {'Yes' if user_profile['serves_meat'] else 'No'}
- Offers delivery: {'Yes' if user_profile.get('has_delivery') else 'No'}

Please analyze the relevant regulations below and generate a report in **Hebrew** with the following structure:

1. **Brief introduction**: 2–3 lines addressing the business owner personally and setting expectations.
2. **Grouped requirements by topic**: (e.g., sanitation, waste, kitchen layout, signage)
   - Use **section titles** and short bullet points.
   - For each rule, include the requirement in simple Hebrew.
   - Use 🔴 for high-priority/mandatory rules, and 🟠 for medium priority.
3. **Summary with practical recommendations**: End with 2–3 clear tips on how to begin complying with the rules.

The relevant regulations are listed below:
{rules_text}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in business regulation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    
    except Exception as e:
        # fallback if OpenAI call fails
        return f"""⚠️ לא הצלחנו להתחבר ל־GPT כרגע.
        אנא נסה שוב מאוחר יותר או צור קשר עם התמיכה הטכנית.
        
"""

