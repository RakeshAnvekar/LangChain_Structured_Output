from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# ---- Schema ----
class Review(TypedDict):
    summary: str
    sentiment: str

# Structured model
structuredReviewModel = model.with_structured_output(Review)
## we have not asked  any specific prompt here, so it will use a default prompt to ask for a review summary and sentiment.
# behind the scenes, it will create a prompt like:
# " you are an AI asistent Please provide a summary and sentiment of the following review: {review_text}"

# ---- Input review ----
review_text = """
Ive been using this phone for a month now. The display is absolutely stunning,and the performance is smooth even with multiple apps running. 
The camera quality in daylight is excellent. However, the battery life is disappointing — it barely lasts a full day with normal usage. Also, the phone gets warm during gaming.

Pros:
- Excellent display
- Smooth performance
- Great daylight camera quality

Cons:
- Poor battery life
- Heats up during gaming
"""
# ---- Direct structured LLM call ----
result = structuredReviewModel.invoke(review_text)
print(result)
print(type(result))
print(result['summary'])
print(result['sentiment'])
