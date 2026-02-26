from pydantic import BaseModel, Field
from typing import List


class TestStep(BaseModel):
    step_number: int = Field(..., description="Step execution order")
    action: str = Field(..., description="Action performed by user")
    expected_result: str = Field(..., description="Expected outcome of the step")


class TestCase(BaseModel):
    test_id: str = Field(..., description="Unique test case ID")
    title: str = Field(..., description="Short descriptive title")
    test_type: str = Field(..., description="happy / negative / edge")
    preconditions: List[str] = Field(..., description="Preconditions before execution")
    steps: List[TestStep]
    priority: str = Field(..., description="High / Medium / Low")


class TestCaseResponse(BaseModel):
    test_cases: List[TestCase]