import pandas as pd

try:
    data = pd.read_csv("entity_matching_test_cases.csv")
except FileNotFoundError:
    print("Error: CSV file not found.")
    data = pd.DataFrame()
except Exception as e:
    print(f"Error loading CSV: {e}")
    data = pd.DataFrame()


def search(query):

    if not query:
        return []

    # Normalize whitespace
    query = " ".join(query.split())
    
    print(f"Searching for: {query}")

    try:
        results = data[
            data["entity_name"].str.contains(
                query,
                case=False,
                na=False
            )
        ]

        results = results[
            [
                "entity_name",
                "entity_type",
                "country",
                "risk_category",
                "event_type",
                "evidence_text",
                "confidence",
                "data_status",
                "source_title",
                "source_organization",
                "source_url"
            ]
        ]
        if results.empty:
           print("No matching entities found.")
           return []

        return results.to_dict(orient="records")

    except Exception as e:
        print(f"Search error: {e}")
        return []