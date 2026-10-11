from ollama import chat
text = """
Microsoft CEO Satya Nadella announced that the company will expand
its artificial intelligence operations in Pakistan. The company plans
to work with universities in Lahore and Islamabad.
"""
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Extract all important people, organizations, companies, and locations from the following text: {text}"
        }
    ]
)
print(response["message"]["content"])