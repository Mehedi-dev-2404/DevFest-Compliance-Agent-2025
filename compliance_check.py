import os
import json
# Import the specific module for the Gemini client
from google import genai
from PIL import Image

# --- THE SYSTEM INSTRUCTION (The Rules for the Gemini Agent) ---
# This is the core logic. It tells the model how to behave, what rules to check,
# and forces it to output structured JSON.
system_prompt = """
You are the "DevFest Booth Compliance Agent." Your task is to analyze the provided image of an event booth setup against a strict set of rules.

RULES:
1.  **Banner Visibility:** A clearly readable company/project banner must be visible. (REQUIRED)
2.  **Swag Compliance:** At least one branded item (e.g., sticker, pen) must be visible on the table. (REQUIRED)
3.  **Power Safety:** No loose, dangling cables should be visible near the floor. (MANDATORY SAFETY CHECK)
4.  **Device Count:** There must be at least one screen/laptop visible for the demo. (REQUIRED)

INSTRUCTIONS:
You must output your analysis in a structured JSON format. For each rule, state the compliance status (PASS or FAIL) and a brief justification based ONLY on the visual evidence in the image.

STRICT JSON OUTPUT FORMAT:
{
  "compliance_status": "PASS" | "FAIL",
  "justification": "Overall status of the booth.",
  "rule_checks": [
    {
      "rule_id": 1,
      "description": "Banner Visibility",
      "status": "PASS" | "FAIL",
      "evidence": "..."
    },
    {
      "rule_id": 2,
      "description": "Swag Compliance",
      "status": "PASS" | "FAIL",
      "evidence": "..."
    },
    {
      "rule_id": 3,
      "description": "Power Safety",
      "status": "PASS" | "FAIL",
      "evidence": "..."
    },
    {
      "rule_id": 4,
      "description": "Device Count",
      "status": "PASS" | "FAIL",
      "evidence": "..."
    }
  ]
}
"""

# --- THE EXECUTION LOGIC ---
# Make sure your demo photo is saved as this file name in the project directory
IMAGE_PATH = "booth_photo.jpg"

def run_compliance_check():
    """Runs the multimodal compliance check using the Gemini API."""
    try:
        # The client automatically finds your GEMINI_API_KEY environment variable
        client = genai.Client()

        # Load the local image file using PIL
        img = Image.open(IMAGE_PATH)
        print(f"Loaded image: {IMAGE_PATH}")

        # Configure the request to force a JSON output structure
        json_config = {"response_mime_type": "application/json"}

        print("Sending image and compliance rules to Gemini...")

        # Call the Gemini 2.5 Flash model with both the text rules (system_prompt) and the image
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[system_prompt, img],
            config=json_config
        )

        # Process and Print the Structured Output
        print("\n--- Compliance Check Results (JSON) ---")

        # Pretty-print the JSON response for readability
        parsed_json = json.loads(response.text)
        print(json.dumps(parsed_json, indent=2))

        # Print the final status clearly for the competition demo
        print(f"\nOVERALL STATUS: {parsed_json.get('compliance_status')}")


    except FileNotFoundError:
        print(f"ERROR: Image file not found at '{IMAGE_PATH}'. Did you save your photo as 'booth_photo.jpg'?")
    except Exception as e:
        print(f"An error occurred during the API call: {e}")
        print("HINT: Ensure the 'google-genai' and 'pillow' packages are installed in your PyCharm interpreter.")

if __name__ == "__main__":
    run_compliance_check()