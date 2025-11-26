from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# ---- Schema ----
class Review(BaseModel):
    key_theams: list[str] = Field(description="write doen all the key theams mentioned in the review",default=[])
    summary:str=Field(description="A brief summary of the review",default="No summary")
    sentiment:Literal["POS","NEG"]=Field(description="The overall sentiment of the review, e.g., POS, NEG, Mixed",default="None")
    pros:Optional[list[str]]=Field(description="list down all the pros mentioned in the review",default=None)
    cons:Optional[list[str]]=Field(description="list down all the cons mentioned in the review",default=None)
    name:Optional[str]=Field(description="name of the product being reviewed",default=None)


# Structured model
structuredReviewModel = model.with_structured_output(Review)
## we have not asked  any specific prompt here, so it will use a default prompt to ask for a review summary and sentiment.
# behind the scenes, it will create a prompt like:
# " you are an AI asistent Please provide a summary and sentiment of the following review: {review_text}"


review_text = """
I’ve been using this phone for two weeks, and I absolutely love it. The screen is bright and clear, and the battery easily lasts me the whole day. The fingerprint sensor is also very fast and accurate."

Pros:
Bright and clear display
All-day battery life
Fast fingerprint sensor
Cons:
None so far
"""
# ---- Direct structured LLM call ----
result = structuredReviewModel.invoke(review_text)

print(result.sentiment)
