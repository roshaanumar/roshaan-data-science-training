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
            "content": f"""Classify the following news article into one of these categories: 
             Sports, Technology, Politics, Business, Entertainment, or Health. 
             Return only the category name.: {text}"""
        }
    ]
)
print(response["message"]["content"])