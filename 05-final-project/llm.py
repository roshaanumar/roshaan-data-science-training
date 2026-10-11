from google import genai
import json
client = genai.Client()


def ask_gemini(prompt):
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text


def analyze_research(report, web_results):

    prompt = f"""
You are a research analysis assistant.

Analyze the research data and web search results below.

RESEARCH DATA:

{report}

WEB SEARCH RESULTS:

{web_results}

Use BOTH the research data and web search results in your analysis.

Return your answer as JSON with exactly these fields:

{{
    "entity": "name of the researched entity",
    "confidence": 0.0,
    "risk_categories": [],
    "conflicts": [],
    "evidence_reliability": "",
    "overall_assessment": ""
}}

RULES:

- Only use information contained in the research data and web search results.
- Do not invent facts.
- Do not assume that two records with the same name represent the same person.
- Compare the web search results with the research matches.
- If a web result appears to refer to a different person, mark it as unrelated.
- If evidence conflicts, mention the conflict.
- If there is not enough information to verify an identity, say so.
- Remember that this is synthetic test data.
- Return ONLY valid JSON.
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )
    clean_response = interaction.output_text.strip()

    if clean_response.startswith("```json"):
       clean_response = clean_response[7:]

    if clean_response.endswith("```"):
       clean_response = clean_response[:-3]

    result = json.loads(clean_response)

    return result