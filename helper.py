import json
from test_generator import generate_test_cases


def call_api(prompt, options, context):
    user_story = context["vars"]["user_story"]
    acceptance_criteria = context["vars"]["acceptance_criteria"]
    scenario = context["vars"]["scenario"]

    result = generate_test_cases(user_story, acceptance_criteria, scenario)

    return {
        "output": json.dumps(result, indent=2)
    }
