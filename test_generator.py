import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from models import TestCaseResponse

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # cost-effective model
    temperature=0
)

# Create JSON parser linked to our schema
parser = JsonOutputParser(pydantic_object=TestCaseResponse)

# Create prompt template
prompt = ChatPromptTemplate.from_template("""
You are a QA Engineer.

Generate EXACTLY 3 test cases in JSON format.

The test cases MUST be in this order:
1. Positive
2. Negative
3. Edge

test_type must be exactly:
positive
negative
edge

Return them inside "test_cases" array.

{format_instructions}

User Story:
{user_story}

Acceptance Criteria:
{acceptance_criteria}
""")

# Create chain
chain = prompt | llm | parser


def generate_test_cases(user_story, acceptance_criteria, scenario):

    result = chain.invoke({
        "user_story": user_story,
        "acceptance_criteria": acceptance_criteria,
        "format_instructions": parser.get_format_instructions()
    })

    test_cases = result["test_cases"]

    # Force exactly 3
    if len(test_cases) < 3:
        raise ValueError("Model did not return 3 test cases.")

    # Assign scenario-based IDs
    for i in range(3):
        test_cases[i]["test_id"] = f"{scenario}_TC_{i+1:03d}"

    return result

if __name__ == "__main__":
    us = "As a user, I want to log in so that I can access my dashboard."
    ac = """
    - User must enter email and password
    - System must validate credentials
    - Error message shown for invalid login
    """

    result = generate_test_cases(us, ac)
    print(result)