import json
import os

# Load rules from JSON
def load_rules(json_path="data/requirements_fire_rescue.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Main matching logic
def match_rules(user_profile, rules):
    matched = []

    for rule in rules:
        # Filter by min size
        min_size = rule.get("min_size_sqm")
        if min_size is not None and user_profile["size_sqm"] < min_size:
            continue

        # Filter by meat requirement
        requires_meat = rule.get("requires_meat")
        if requires_meat is not None and user_profile["serves_meat"] != requires_meat:
            continue

        matched.append(rule)

    return matched

# Example usage
if __name__ == "__main__":
    user_profile = {
        "size_sqm": 85,
        "serves_meat": True,
        "has_delivery": False  # optional, not used yet
    }

    rules = load_rules()
    result = match_rules(user_profile, rules)

    for r in result:
        print(f"✔ {r['condition']}")
