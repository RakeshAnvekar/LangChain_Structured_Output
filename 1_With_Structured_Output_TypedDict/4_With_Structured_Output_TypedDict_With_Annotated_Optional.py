from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatOpenAI()

# ---- Schema ----
class Review(TypedDict):
    key_theams:Annotated[list[str],"write doen all the key theams mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The overall sentiment of the review, e.g., positive, negative, Mixed"]
    pros:Annotated[Optional[list[str]],"list down all the pros mentioned in the review"]
    cons:Annotated[Optional[list[str]],"list down all the cons mentioned in the review"]


# Structured model
structuredReviewModel = model.with_structured_output(Review)
## we have not asked  any specific prompt here, so it will use a default prompt to ask for a review summary and sentiment.
# behind the scenes, it will create a prompt like:
# " you are an AI asistent Please provide a summary and sentiment of the following review: {review_text}"


review_text = """
I’ve been using the XPro Max Ultra for nearly three months now, and while it’s an impressive device on paper, the real-world experience has been a mix of highs and frustrations. The 6.8-inch AMOLED display is stunning—bright, vibrant, and excellent under direct sunlight. Watching movies and playing games feel immersive. The speakers are loud and clear, although the bass feels a bit flat.
Performance-wise, the phone flies through everyday tasks and handles heavy apps without lag. But during long gaming sessions or 4K video recording, the phone heats up noticeably, sometimes enough to make it uncomfortable to hold. Battery life is inconsistent—on some days I easily get 6–7 hours of screen time, while on others the battery drains rapidly even with light usage. Standby drain is especially bad after the latest software update.
The camera is a mixed bag: the primary 108MP sensor captures excellent photos in good lighting with natural colors, but night mode often over-processes images, making them look artificial. The front camera is good but struggles in low light. Video stabilization is superb, but autofocus occasionally hunts during close-up shots.
The software is feature-rich but bloated. There are several preinstalled apps that can’t be removed, and the UI sometimes stutters despite the powerful hardware. On the positive side, the customization options are great and the new notification system is helpful.Connectivity has been another issue. Wi-Fi range is below average, and Bluetooth occasionally disconnects when paired with my earbuds.
Overall, the phone has great hardware potential but feels let down by inconsistent software optimization and battery performance.
"""
# ---- Direct structured LLM call ----
result = structuredReviewModel.invoke(review_text)
print(result)
print(type(result))
print(result['key_theams'])
print(result['summary'])
print(result['sentiment'])
print(result['pros'])
print(result['cons'])
