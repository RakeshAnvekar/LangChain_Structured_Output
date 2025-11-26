from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

load_dotenv()

model = ChatOpenAI()

# ---- Schema ----
class Review(TypedDict):
    key_theams:Annotated[list[str],"write doen all the key theams mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["POS","NEG"], "The overall sentiment of the review, e.g., positive, negative, Mixed"]
    pros:Annotated[Optional[list[str]],"list down all the pros mentioned in the review"]
    cons:Annotated[Optional[list[str]],"list down all the cons mentioned in the review"]
    name:Annotated[Optional[str],"name of the product being reviewed"]


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

print(result['sentiment'])
