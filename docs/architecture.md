# Project Architecture – business-license-ai

This document provides a high-level overview of the architecture and structure of the **business-license-ai** project.

---

## Backend Architecture

The system is built as a modular **Python backend** application, designed to:

1. Parse raw regulatory documents.
2. Match rules to specific business inputs.
3. Use AI to generate customized compliance reports.

---

## Main Components

### 1. `parse_docx.py`
**Role:**  
Extracts and cleans relevant regulatory data from a `.docx` file.

**Process:**
- Loads paragraphs from the source document.
- Identifies the relevant chapter.
- Filters and structures the rules into JSON format.

---

### 2. `logic.py`
**Role:**  
Matches business user inputs to relevant rules from the preprocessed dataset.

---

### 3. `ai_engine.py`
**Role:**  
Handles communication with the OpenAI API to generate the final human-readable report.

**Steps:**
- Loads the appropriate prompt template.
- Injects matched rules and user data.
- Sends the request to GPT and returns the response.

---

### 4. `app.py`
**Role:**  
Runs the Flask server and exposes API endpoints.

**Endpoints:**
- `POST /generate`: Accepts user input, runs logic and AI engine, returns report.
- Future endpoints may support document upload, multi-language generation, etc.
