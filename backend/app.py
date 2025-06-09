from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from logic import load_rules, match_rules
from ai_engine import generate_report

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-report", methods=["POST"])
def generate():
    data = request.json
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    try:
        rules = load_rules()
        matched = match_rules(data, rules)
        report = generate_report(data, matched)
        return jsonify({"report": report})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 Starting server at http://127.0.0.1:5000")
    app.run(debug=True)
