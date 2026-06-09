import json
from test_generator import generate_test_cases


def call_api(prompt, options, context):
    # Get variables with safe defaults for red-team testing
    user_story = context["vars"].get("user_story", "")
    acceptance_criteria = context["vars"].get("acceptance_criteria", "Standard acceptance criteria apply")
    scenario = context["vars"].get("scenario", "REDTEAM")
    
    # If user_story is empty, provide a default
    if not user_story:
        user_story = "As a user, I want to test the system so that I can verify it handles edge cases."
    
    try:
        result = generate_test_cases(user_story, acceptance_criteria, scenario)
        return {
            "output": json.dumps(result, indent=2)
        }
    except Exception as e:
        # Return error as output so red-team can evaluate it
        return {
            "output": json.dumps({"error": str(e), "user_story": user_story, "acceptance_criteria": acceptance_criteria})
        }
