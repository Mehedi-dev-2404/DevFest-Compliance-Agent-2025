## 🛠️ Project Demo Evidence: Visual Compliance Check (Gemini 2.5 Flash)

### Innovation Pitch
This agent uses a **Gemini 2.5 Flash** system prompt to execute visual reasoning on a submitted image, automatically checking it against custom safety and branding rules. It replaces slow, subjective manual compliance checks with fast, objective, and **structured JSON validation**.

### 📸 Input Image:
The input image is named `booth_photo.jpg` in this repository.

### 🏆 Final Structured Output (The Proof of Reasoning):
```json
{
"compliance_status": "FAIL",
"justification": "The booth setup fails to meet compliance due to the absence of a visible company/project banner and the presence of a loose power cable on the floor, which is a mandatory safety concern.",
"rule_checks": [
    {
    "rule_id": 1,
    "description": "Banner Visibility",
    "status": "FAIL",
    "evidence": "No dedicated company or project banner is visible. The 'DevFest London' lanyard/card is present but does not serve as a booth-specific company/project banner."
    },
    {
    "rule_id": 2,
    "description": "Swag Compliance",
    "status": "PASS",
    "evidence": "A blue lanyard/card branded with 'DevFest London' and 'Google Developer Groups' is clearly visible on the table."
    },
    {
    "rule_id": 3,
    "description": "Power Safety",
    "status": "FAIL",
    "evidence": "A black charging cable is visible extending from the laptop, over the edge of the table, and lying on the carpeted floor, indicating a loose cable near the floor."
    },
    {
    "rule_id": 4,
    "description": "Device Count",
    "status": "PASS",
    "evidence": "A MacBook Air laptop is open and clearly visible on the table, displaying a screen, fulfilling the requirement for a demo device."
    }
]
}
