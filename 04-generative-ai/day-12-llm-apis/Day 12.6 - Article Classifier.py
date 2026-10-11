from ollama import chat
article = """
Pakistan's national cricket team defeated India by five wickets at
Gaddafi Stadium in Lahore. Babar Azam scored a century and helped
Pakistan chase the target successfully.
"""
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
Analyze the following news article and return the results as JSON.

Return ONLY valid JSON. Do not include explanations, markdown,
code fences, or any text outside the JSON.

Use exactly this structure:
{{
    "category": "",
    "risk": "",
    "entities": [],
    "summary": ""
}}

Rules:
- category must be exactly ONE of:
  Sports, Technology, Politics, Business, Entertainment, Health.
- risk must be exactly ONE of:
  Low, Medium, High.
- Read the entire article carefully and extract every relevant entity.
- Entities should include names of people, companies, organizations,
  locations, countries, products, technologies, and other important
  named entities.
- Never return an empty entities array if the article contains
  identifiable named entities.
- summary must be a short, clear summary of the article.

Article:
{article}
"""
        }
    ]
)

print(response["message"]["content"])