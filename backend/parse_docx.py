from docx import Document
import json
import os

# Load the Word document
doc_path = "/mnt/data/18-07-2022_4.2A.docx"
doc = Document(doc_path)

# Flags for extracting the "Ministry of Health" section
start_phrase = "פרק 4 - משרד הבריאות"
end_phrase = "פרק 5 - הרשות הארצית לכבאות והצלה"
in_health_section = False
health_text = []

# Extract paragraphs between the start and end markers
for para in doc.paragraphs:
    text = para.text.strip()
    if not text:
        continue
    if start_phrase in text:
        in_health_section = True
        continue
    if end_phrase in text:
        break
    if in_health_section:
        health_text.append(text)

# For demo purposes: select only first 10 lines as samples
samples = health_text[:10]

# Build a simple JSON structure from selected rules
json_output = []
for idx, line in enumerate(samples):
    json_output.append({
        "id": f"health-{idx+1:02}",
        "category": "Ministry of Health",
        "condition": line,
        "keywords": [],
        "min_size_sqm": None,
        "requires_meat": None
    })

# Save output to a JSON file
output_path = "/mnt/data/requirements_health_sample.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(json_output, f, ensure_ascii=False, indent=2)

output_path
