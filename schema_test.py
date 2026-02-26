from models import TestCaseResponse

sample_data = {
    "test_cases": [
        {
            "test_id": "TC_001",
            "title": "Valid Login",
            "test_type": "happy",
            "preconditions": ["User is registered"],
            "priority": "High",
            "steps": [
                {
                    "step_number": 1,
                    "action": "Enter valid email and password",
                    "expected_result": "User logged in successfully"
                }
            ]
        }
    ]
}

validated = TestCaseResponse(**sample_data)

print("Schema validation successful!")
print(validated)