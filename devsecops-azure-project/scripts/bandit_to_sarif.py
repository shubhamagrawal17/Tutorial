# This script converts a Bandit JSON security scan report into a SARIF 2.1.0 file so vulnerabilities can be shown as code-scanning issues in CI/CD tools like GitHub or Azure DevOps.
import json
import sys
import os

def convert_bandit_to_sarif(bandit_file, sarif_file):
    if not os.path.exists(bandit_file):
        print(f"Error: {bandit_file} not found")
        return

    with open(bandit_file) as f:
        bandit = json.load(f)

    # Map Bandit severity to SARIF levels
    level_map = {
        "HIGH": "error",
        "MEDIUM": "warning",
        "LOW": "note",
        "UNDEFINED": "warning"
    }

    sarif = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "Bandit",
                        "informationUri": "https://bandit.readthedocs.io/",
                        "rules": []
                    }
                },
                "results": []
            }
        ]
    }

    rules = {}
    for issue in bandit.get("results", []):
        rule_id = issue["test_id"]
        severity = issue.get("issue_severity", "MEDIUM").upper()
        sarif_level = level_map.get(severity, "warning")

        if rule_id not in rules:
            rules[rule_id] = {
                "id": rule_id,
                "shortDescription": {"text": issue["issue_text"]},
                "helpUri": issue.get("more_info")
            }

        sarif["runs"][0]["results"].append({
            "ruleId": rule_id,
            "level": sarif_level,
            "message": {"text": issue["issue_text"]},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {"uri": issue["filename"]},
                    "region": {"startLine": issue["line_number"]}
                }
            }]
        })

    sarif["runs"][0]["tool"]["driver"]["rules"] = list(rules.values())

    with open(sarif_file, "w") as f:
        json.dump(sarif, f, indent=2)
    print(f"Successfully converted {bandit_file} to {sarif_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bandit_to_sarif.py <input_json> <output_sarif>")
    else:
        convert_bandit_to_sarif(sys.argv[1], sys.argv[2])