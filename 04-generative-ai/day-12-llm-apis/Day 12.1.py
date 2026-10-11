from ollama import chat
text = """
Artificial intelligence is rapidly changing the healthcare industry.
Hospitals are using AI to analyze medical images, help doctors identify
diseases, predict patient risks, and manage large amounts of medical data.
Although AI can improve efficiency and accuracy, doctors still need to
review important decisions and ensure that patients receive appropriate care.
"""
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Summarize the following text in one sentence: {text}"
        }
    ]
)
print(response["message"]["content"])