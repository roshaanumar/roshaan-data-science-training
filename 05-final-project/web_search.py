from ddgs import DDGS


def web_search(query):
    print(f"Searching the web for: {query}")

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        return results

    except Exception as e:
        print(f"Web search error: {e}")
        return []