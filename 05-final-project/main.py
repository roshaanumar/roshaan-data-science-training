from Search import search
from researcher import research
from llm import analyze_research
from web_search import web_search
import logging

# Logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="research.log"
)

def main():
    logging.info("Research program started")

    # Input Validation
    query = input("\n🔎 Enter a person or company to research: ").strip()
    logging.info(f"Research query received: {query}")

    if not query:
        print("No input provided. Exiting.")
        return

    # Search
    try:
        logging.info("Starting search")
        results = search(query)
        logging.info(f"Search completed. Found {len(results)} matches")

    except Exception as e:
        logging.error(f"Search failed: {e}")
        print(f"❌ An error occurred during the search: {e}")
        return

    print("\n" + "=" * 60)
    print("🔎 DATABASE SEARCH")
    print("=" * 60)

    print(f"Entity: {query}")
    print(f"Potential matches: {len(results)}")

    # Web search

    print("\n" + "=" * 60)
    print("🌐 WEB SEARCH")
    print("=" * 60)

    try:
        web_results = web_search(query)
        for i, result in enumerate(web_results, 1):
            print(f"\n[{i}] {result.get('title')}")
            print(f"    🔗 {result.get('href')}")
            print(f"    {result.get('body')}")

    except Exception as e:
        print(f"❌ Web search failed: {e}")

    # Research

    try:
        logging.info("Starting research")
        report = research(query, results)
        logging.info("Research completed successfully")

    except Exception as e:
        logging.error(f"Research failed: {e}")
        print(f"❌ An error occurred during the research: {e}")

        return

    # Output the final report

    print("\n" + "=" * 60)
    print("📋 FINAL REPORT")
    print("=" * 60)

    print(f"\n👤 Entity: {report['entity']['name']}")
    print(f"🔍 Matches: {report['matches']['count']}")
    print(f"📚 Sources: {report['sources']['count']}")

    print("\n--- Risk Assessment ---")

    print(
        f"⚠️  Risk Categories: "
        f"{report['risk_assessment']['categories']}"
    )

    print(
        f"📊 Confidence: "
        f"{report['risk_assessment']['confidence']}"
    )

    print(
        f"🧩 Identity Confidence: "
        f"{report['risk_assessment']['identity_confidence']}"
    )

    print("\n--- Verification ---")

    print(
        f"⚡ Conflicts: "
        f"{report['verification']['conflicts']}"
    )

    print("\n--- Summary ---")

    print(report['summary'])

    # AI Analysis

    print("\n" + "=" * 60)
    print("🤖 AI RISK ANALYSIS")
    print("=" * 60)

    try:

        logging.info("Starting AI analysis")
        ai_analysis = analyze_research(report, web_results)
        logging.info("AI analysis completed successfully")
        print(f"\n👤 Entity: {ai_analysis['entity']}")

        print(f"📊 Confidence: {ai_analysis['confidence']}")

        print(
            f"⚠️  Risk Categories: "
            f"{ai_analysis['risk_categories']}"
        )

        print(
            f"⚡ Conflicts: "
            f"{ai_analysis['conflicts']}"
        )

        print(
            f"📚 Evidence Reliability: "
            f"{ai_analysis['evidence_reliability']}"
        )

        print("\n📝 Overall Assessment:")

        print(ai_analysis['overall_assessment'])

    except Exception as e:

        logging.error(f"AI analysis failed: {e}")

        print(f"❌ AI analysis failed: {e}")

    print("\n" + "=" * 60)
    print("✅ RESEARCH COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()