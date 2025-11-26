from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# ---- Schema ----
json_student_schema={
    "title": "student",
    "description": "A schema representing a student's information",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The full name of the student"
        },
        "age": {
            "type": "integer",
            "description": "The age of the student"
        },
        "grade": {
            "type": "string",
            "description": "The current grade of the student"
        },
        "courses": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A list of courses the student is enrolled in"
        }
    },
    "required": ["name", "grade", "courses"]
     
}


# Structured model
structuredReviewModel = model.with_structured_output(json_student_schema)
## we have not asked  any specific prompt here, so it will use a default prompt to ask for a review summary and sentiment.
# behind the scenes, it will create a prompt like:
# " you are an AI asistent Please provide a summary and sentiment of the following review: {review_text}"


review_text = """
John Doe is a 20-year-old student currently studying in grade A. He is enrolled in Mathematics, Physics, and Computer Science courses.
"""
# ---- Direct structured LLM call ----
result = structuredReviewModel.invoke(review_text)

print(result)
