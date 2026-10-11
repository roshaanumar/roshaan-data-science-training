def research(query, results):

    print(f"Researching {query}...")
    risk_categories = set()
    confidences = []
    sources = []
    seen_sources = set()
    countries = set()

    for result in results:

        risk = result["risk_category"]
        countries.add(result["country"])
        confidences.append(result["confidence"])

        source = {
            "title": result["source_title"],
            "organization": result["source_organization"],
            "url": result["source_url"]
        }

        source_key = (
            source["organization"],
            source["title"]
        )

        if source_key not in seen_sources:
            sources.append(source)
            seen_sources.add(source_key)

        if risk != "no_known_relevant_risk":
            risk_categories.add(risk)

    # Calculate average confidence FIRST
    if confidences:
        average_confidence = sum(confidences) / len(confidences)
    else:
        average_confidence = 0

    # Check for conflicts
    conflicts = []

    if len(countries) > 1:
        conflicts.append("Multiple countries found among matches.")

    # Calculate identity confidence AFTER average confidence exists
    if conflicts:
        identity_confidence = average_confidence * 0.7
    else:
        identity_confidence = average_confidence

    risk_categories = list(risk_categories)

    summary = f"Found {len(results)} potential matches."

    if risk_categories:
        summary += f" Risk categories identified: {', '.join(risk_categories)}."
    else:
        summary += " No relevant risk categories identified."

    report = {

        "entity": {
            "name": query
        },

        "matches": {
            "count": len(results),
            "records": results
        },

        "risk_assessment": {
            "categories": risk_categories,
            "confidence": average_confidence,
            "identity_confidence": identity_confidence
        },

        "sources": {
            "count": len(sources),
            "records": sources
        },

        "verification": {
            "conflicts": conflicts
        },

        "summary": summary
    }

    return report