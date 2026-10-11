from ollama import chat

text = """
Pakistan's national cricket team defeated India by five wickets in an
exciting match at Lahore's Gaddafi Stadium. The Pakistani opening batsman
scored a century and helped his team successfully chase the target.
"""

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
Analyze this news article.

Return ONLY a JSON object. Do not include explanations,
markdown, code fences, or any text before or after the JSON.

Use exactly this format:
{{
    "category": "Sports",
    "risk": "Low"
}}

Category must be one of: Sports, Technology, Politics, Business, Entertainment, Health.
Risk must be one of: Low, Medium, High.

Article:
{text}
"""
        }
    ]
)

print(response["message"]["content"])