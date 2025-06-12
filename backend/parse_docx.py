import re
import json
import os
from docx import Document

# נתיב לקובץ docx ביחס למיקום הקובץ (בתוך backend/)
doc_path = "data/18-07-2022_4.2A.docx"

doc = Document(doc_path)

# נתחיל מפרק 5 ועד סוף המסמך
start_phrase = "פרק 5 - הרשות הארצית לכבאות והצלה"

inside = False
paragraphs = []

for para in doc.paragraphs:
    text = para.text.strip()
    if start_phrase in text:
        inside = True
        continue
    if inside and text:
        paragraphs.append(text)

# עיבוד וסינון – מוגבל ל-100
structured_rules = []
rule_id = 1

for text in paragraphs:
    if len(structured_rules) >= 100:
        break

    if len(text) < 15:
        continue

    min_size = None
    min_seats = None

    # זיהוי מ"ר
    sqm_match = re.search(r'(\d{2,4})\s*מ"ר', text)
    if sqm_match:
        min_size = int(sqm_match.group(1))

    # זיהוי אנשים / תפוסה
    seats_match = re.search(r'(?:יותר מ-|מעל)\s*(\d{1,3})\s*(?:אדם|אנשים|נוכחים)', text)
    if seats_match:
        min_seats = int(seats_match.group(1))

    structured_rules.append({
        "id": f"fire-{rule_id:03}",
        "category": "Fire and Rescue",
        "condition": text,
        "keywords": [],
        "min_size_sqm": min_size,
        "min_seats": min_seats,
        "requires_meat": None
    })

    rule_id += 1

# שמירה ל-json בתיקייה data/
output_path = "data/requirements_fire_rescue.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(structured_rules, f, ensure_ascii=False, indent=2)

print(f"✔ Created file with {len(structured_rules)} rules at {output_path}")
