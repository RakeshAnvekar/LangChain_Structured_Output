# 📘 Structured Output vs Unstructured Output

Large Language Models (LLMs) process a given prompt and return a
response. By default, this response is usually **plain text**, which is
called **unstructured output**.

------------------------------------------------------------------------

## 🔹 Unstructured Output

When we pass an input prompt to an LLM:

    Input → LLM → Text Response

The response we receive is generally in **free-form text**, without a
fixed structure.

### ✅ Example (Unstructured Response)

**Prompt:**
"Can you create a one-day travel itinerary for Paris?"

**LLM Response:**

    Here is your itinerary:
    Morning – Visit the Eiffel Tower
    Afternoon – Walk through the Louvre Museum
    Evening – Enjoy dinner at a Seine River café

✅ Readable for humans\
❌ Not structured for machines\
❌ Difficult to parse for APIs, databases, and tools

------------------------------------------------------------------------

## 🔹 Structured Output

Now imagine we ask the LLM to return the same information in **JSON
format**.

### ✅ Example (Structured JSON Response)

``` json
[
  { "time": "Morning", "activity": "Visit the Eiffel Tower" },
  { "time": "Afternoon", "activity": "Walk through the Louvre Museum" },
  { "time": "Evening", "activity": "Dinner at a Seine River café" }
]
```

This is **structured output** --- the data follows a predictable
format.
It becomes easy to: 
- Parse
- Save
- Validate
- Send to other systems

------------------------------------------------------------------------

## 🔹 Structured Output in LangChain

In **LangChain**, structured output refers to the practice of
instructing the LLM to return responses in formats such as:

-   JSON
-   Pydantic Models
-   Dictionaries
-   Enums / Typed Fields

This makes programmatic handling of LLM output much easier.

------------------------------------------------------------------------

## ❓ Why Do We Need Structured Output?

LLMs naturally output text, which is flexible but hard to use directly
with:

-   Databases
-   External tools
-   APIs
-   Microservices
-   Calculators or code execution tools

Structured output forces the LLM to provide responses in a
**machine-friendly format**, enabling the LLM to communicate reliably
with other systems.

------------------------------------------------------------------------

## ✅ Use Cases for Structured Output

### 1️⃣ Data Extraction

You can extract specific fields and store them in a database.

**Example:** Resume Parsing
Extract: 
- Name
- Skills
- Address
- Email
- Last Company

All returned in **structured JSON** and saved in the DB.

------------------------------------------------------------------------

### 2️⃣ API Building

**Example:** Amazon Product Reviews

Unstructured reviews become: 
- Topic
- Pros
- Cons
- Sentiment
- Summary

Used for storage and analytics.

------------------------------------------------------------------------

### 3️⃣ Agents Using Tools

Tools require structured input, not free text.

**User:** "What is the square root of 144?"

``` json
{ "operation": "sqrt", "number": 144 }
```

Passed directly to a calculator tool.

------------------------------------------------------------------------

## 🧠 Summary: Why Structured Output Matters

-   LLMs naturally return unstructured text.
-   Systems need structured data.
-   Structured output enables:
    -   Databases
    -   APIs
    -   Automation
    -   Tools
    -   Agents

👉 **Essential for production-grade AI systems.**

------------------------------------------------------------------------

# 🔎 Types of LLMs (Based on Structured Output Capability)

## 1️⃣ LLMs That Natively Support Structured Output

Examples: 
- GPT-4 / GPT-4o / GPT-5
- Claude 3

They directly understand: 
- JSON
- Schemas
- Typed objects

``` python
model = ChatOpenAI(...)
structured_model = model.with_structured_output(MySchema)
```

------------------------------------------------------------------------

## 2️⃣ LLMs That Do NOT Support Structured Output Natively

Older and smaller models only return text.

### ✅ Solution: Output Parsers

-   JsonOutputParser
-   PydanticOutputParser
-   StructuredOutputParser

``` python
parser = JsonOutputParser(...)
prompt = parser.get_format_instructions()
```

------------------------------------------------------------------------

# 🧾 TypedDict (Python Type-Hint-Based Structured Dictionary)

TypedDict defines dictionary keys and types at development time.

✅ Type safety
✅ IDE hinting
❌ No runtime validation

``` python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
```

------------------------------------------------------------------------

## 🧩 Review Example Using Annotated

``` python
from typing import TypedDict, Annotated

class Review(TypedDict):
    summary: Annotated[str, "1–2 sentence summary"]
    sentiment: Annotated[str, "positive, negative, or neutral"]
```

------------------------------------------------------------------------

# ✅ Pydantic

Pydantic is a **data validation library** for Python.

-   Runtime validation
-   Default values
-   Optional fields
-   Type conversion
-   Regex & constraints

✅ Best for **production validation**

------------------------------------------------------------------------

# ✅ JSON Schema

Used when both backend and frontend need shared validation rules.

✅ Universal format
✅ No Python dependency
✅ Cross-platform compatible

------------------------------------------------------------------------

# 🧩 When to Use What?

  Tool          Use Case
  ------------- --------------------------------------
  TypedDict     Only type hints
  Pydantic      Full validation & constraints
  JSON Schema   Shared backend + frontend validation

------------------------------------------------------------------------

# ✅ Final Takeaway

-   **Unstructured Output** → Human friendly\
-   **Structured Output** → Machine friendly\
-   **Structured output is mandatory for production AI systems**
