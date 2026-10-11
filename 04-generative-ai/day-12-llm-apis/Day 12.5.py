from ollama import chat
text = """
Apple announced that it will invest $1 billion in artificial intelligence
research and development over the next three years. The company plans to
expand its AI teams and develop new AI-powered products.
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
               "company": "",
               "investment": "",
               "time_period": "",
               "purpose": ""
           }}
           
           Article:
           {text}
           """
        }
    ]
)
print(response["message"]["content"])