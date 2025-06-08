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
You are an expert in Israeli business licensing. The following is a list of regulations that apply to a specific business.
The business has the following characteristics:
- Size: {user_profile['size_sqm']} square meters
- Serves meat: {'Yes' if user_profile['serves_meat'] else 'No'}
- Offers delivery: {'Yes' if user_profile.get('has_delivery') else 'No'}

Please generate a clear and friendly report in Hebrew for the business owner.
Explain the requirements in simple language, grouped by topic if possible, and suggest priorities.

Here are the relevant requirements:
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

