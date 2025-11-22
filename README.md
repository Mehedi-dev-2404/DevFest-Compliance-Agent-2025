# 🤖 DevFest Booth Compliance Agent

![Project Status](https://img.shields.io/badge/Status-Submitted-brightgreen)
![Technology](https://img.shields.io/badge/Powered%20By-Gemini%202.5%20Flash-blue)
![Competition](https://img.shields.io/badge/DevFest%20London%202025-AI%20Innovation%20Lab-orange)

## 🚀 Project Elevator Pitch

The **DevFest Booth Compliance Agent** is a **multimodal AI application** designed to instantly audit event booth setups against strict safety and branding rules. By leveraging **Gemini 2.5 Flash's visual reasoning capabilities**, the agent converts subjective, time-consuming manual checks into an **objective, scalable, and instant validation** system.

We replace a clipboard and a weary inspector with a camera and a structured JSON report.

---

## ✨ Features

* **Multimodal Analysis:** Processes and reasons over both the **textual rules** (via System Instruction) and the **visual evidence** (via the input image).
* **Structured Output:** Delivers the audit result in a clean, predictable **JSON format**, ready for integration into backend databases or immediate display.
* **Objective Evidence:** For every rule, the agent provides a clear **PASS** or **FAIL** status along with the specific **visual evidence** found in the image.
* **Focus on Safety:** Prioritizes mandatory safety checks (e.g., loose cables) as specified in the rule set.

---

## 💻 Technology Stack

* **Core AI Engine:** Google Gemini 2.5 Flash API
* **Language:** Python
* **Libraries:** `google-genai` (for API calls), `Pillow` (for image handling)

---

## 🛠️ Setup and Installation

### Prerequisites
1.  **Python 3.x**
2.  A **Gemini API Key** (Obtained from Google AI Studio).

### Installation

1.  Clone this repository:
    ```bash
    git clone [YOUR-REPO-URL-HERE]
    cd DevFest-Compliance-Agent-2025
    ```
2.  Install required libraries:
    ```bash
    python3 -m pip install google-genai pillow
    ```
3.  Set your API Key as an environment variable (crucial step for security):
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

### Execution

1.  Place your demo image file in the project directory and name it **`booth_photo.jpg`**.
2.  Run the script from your terminal:
    ```bash
    python3 compliance_check.py
    ```

---

## 🏆 Demo and Evidence

The following output demonstrates the agent successfully enforcing the rules defined in the Python script (`compliance_check.py`) against a sample image (available as `booth_photo.jpg` in this repository).

### Rules Being Checked

1.  **Banner Visibility:** A clearly readable company/project banner must be visible.
2.  **Swag Compliance:** At least one branded item must be visible on the table.
3.  **Power Safety:** No loose, dangling cables should be visible near the floor. (MANDATORY)
4.  **Device Count:** There must be at least one screen/laptop visible for the demo.

### Final Structured Output

```json
--- Compliance Check Results (JSON) ---
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

OVERALL STATUS: FAIL
