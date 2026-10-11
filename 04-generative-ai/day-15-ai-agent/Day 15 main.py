import ollama
import json
from ddgs import DDGS
#using DuckDuckGo search so i don't need another paid API.
def search_web(query):
    results = DDGS().text(query, max_results=5)

    formatted_results = ""

    for result in results:
        formatted_results += f"""
Title: {result['title']}
URL: {result['href']}
Information: {result['body']}

"""

    return formatted_results

#LLM call
company = input("Enter company name: ")

results = search_web(company)

prompt = f"""
You are a research assistant.

Research the following company using the search results provided below.

Company: {company}

Search Results:
{results}

Extract the most important findings about the company.

For each finding, assign one of these categories:

- Company Information
- Products and Services
- Business History
- Leadership
- Technology
- Other

Also identify the sources used from the search results.

Return ONLY valid JSON in this exact structure:

{{
    "company": "{company}",
    "findings": [
        {{
            "category": "Category",
            "finding": "Important finding"
        }}
    ],
    "sources": [
        {{
            "title": "Source title",
            "url": "Source URL"
        }}
    ]
}}

Do not include markdown.
Do not include explanations outside the JSON.
Do not make up information that is not supported by the search results.
Only include sources that appear in the provided search results.
"""

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

report = json.loads(response["message"]["content"])

#Clean report
print("\n" + "=" * 50)
print("RESEARCH REPORT")
print("=" * 50)

print(f"\nCompany: {report['company']}")

print("\nFindings:")
print("-" * 50)

for finding in report["findings"]:
    print(f"\n[{finding['category']}]")
    print(finding["finding"])

print("\nSources:")
print("-" * 50)

for i, source in enumerate(report["sources"], start=1):
    print(f"{i}. {source['title']}")
    print(f"   {source['url']}")

print("\n" + "=" * 50)