import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_report(user_profile, matched_rules):
    #print(user_profile)
    if user_profile['serves_meat']:
        print("Serves meat: Yes")
    if user_profile.get('has_delivery'):
        print("Offers delivery: Yes")
    rules_text = "\n".join(
        [f"{idx + 1}. {rule['condition']}" for idx, rule in enumerate(matched_rules)]
    )

    prompt = f"""
You are an expert in Israeli business licensing and regulation.

A small business owner is asking for a personalized, **detailed** and **actionable** summary of the regulatory requirements for their business, based on the following profile:

- Business area: {user_profile['size_sqm']} sqm
- Number of seats: {user_profile.get('num_seats', 'Not specified')}
- Serves meat: {'Yes' if user_profile['serves_meat'] else 'No'}
- Offers delivery: {'Yes' if user_profile.get('has_delivery') else 'No'}

Below is a list of all possible regulatory requirements (in Hebrew).  
Please **analyze each one**, and select only the rules that are **relevant to this specific business**, based on the business size, seating capacity, type of food, services, etc.

Then, generate a report in **Hebrew**, with the following structure:

---

1. **Short introduction**: 2–3 lines written personally to the business owner, setting expectations.

2. **Grouped requirements by topic** (e.g. Fire Safety, Gas, Emergency Exits, Signage):
   - For each group, list **only the rules relevant to the business**.
   - For each rule, explain **why it's relevant**, and **what the business must do** to comply.
   - Use 🔴 for mandatory/critical rules, and 🟠 for medium-priority/recommended ones.
   - Use simple, clear Hebrew.
   - Include **at least 6–10 rules** total to ensure the report is useful.

3. **Summary with practical next steps**:
   - Give 2–3 specific tips based on the business’s details.
   - Start each tip with: "כדאי להתחיל מ־..."

---

Here are the relevant rules to choose from:
{rules_text}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
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

