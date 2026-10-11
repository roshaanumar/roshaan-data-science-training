# Phase 3: Dataset Summary & Data-Quality Report -- Batch 1

## Overall counts
- Total records: 128
- PERSON: 73 (57.0%)
- COMPANY: 55 (43.0%)
- VERIFIED_REAL: 18 (14.1%)
- SYNTHETIC_TEST_DATA: 110 (85.9%)

## Entity-match distribution
- MATCH: 73 (57.0%)
- POSSIBLE_MATCH: 20 (15.6%)
- NO_MATCH: 35 (27.3%)

## Risk-label distribution
- RISK_IDENTIFIED: 51 (39.8%)
- NO_RELEVANT_RISK: 55 (43.0%)
- UNCERTAIN: 22 (17.2%)

## Risk-category distribution
- no_known_relevant_risk: 55
- money_laundering: 12
- financial_crime: 11
- regulatory_action: 10
- sanctions: 8
- terrorism_financing: 7
- legal_action: 6
- organized_crime: 6
- criminal_investigation: 5
- fraud: 4
- corruption: 4

## Country distribution (top entries)
- United States: 15
- China: 10
- Germany: 10
- Spain: 10
- Russia: 8
- Australia: 7
- United Arab Emirates: 7
- Mexico: 7
- Turkey: 6
- South Africa: 6
- Canada: 6
- Pakistan: 5
- Nigeria: 4
- Brazil: 4
- India: 4

## Source organization distribution (VERIFIED_REAL only)
- U.S. Securities and Exchange Commission: 8
- U.S. Department of Justice: 3
- U.S. Attorney's Office, Western District of Kentucky: 3
- U.S. Department of the Treasury, Office of Foreign Assets Control (OFAC): 3
- Summarized via FesenkoLaw.com (secondary legal-commentary source on an OFAC action): 1

## Data-quality checks
- Duplicate record_id values: 0 (none found)
- Records missing source_url: 0 (expected -- synthetic records use an explicit 'N/A -- synthetic' placeholder rather than a blank or fabricated URL)
- VERIFIED_REAL records with a missing/placeholder URL: 0 (should be 0 -- PASS)
- Records missing country: 0
- Records where risk_label=RISK_IDENTIFIED but risk_category=no_known_relevant_risk (contradiction check): 0 PASS
- All 18 VERIFIED_REAL source URLs point to primary or named secondary sources actually retrieved via search during this session -- none fabricated. Each was individually confirmed before being added.
- All SYNTHETIC_TEST_DATA rows: entity names, companies, and evidence text are fictional constructions, explicitly labeled in evidence_text (prefixed "SYNTHETIC paraphrase:") and in data_status. No real individuals' or companies' names were reused for fictional allegations.

## Known limitations of this batch (read before use)
- **Scale:** this is 128 records, well below your 1,000-2,000 target. Reaching that volume with genuine VERIFIED_REAL data at this level of hand-verification isn't feasible in a single pass -- see the Phase 1 report's recommendation to bulk-download from OpenSanctions/OFAC directly for real volume, which this batch complements rather than replaces.
- **VERIFIED_REAL depth:** the 18 real records are individually verified but represent a narrow slice (mostly 2024-2026 U.S. enforcement/sanctions actions) -- not the geographic or historical diversity a full dataset would have.
- **Evidence text:** all VERIFIED_REAL evidence_text fields are paraphrased, not quoted, per copyright practice -- if your pipeline needs to test exact-quote extraction, that's not covered here.
- **entity_match_label on real records:** all 18 real records are labeled MATCH because each is individually confirmed as the correct entity from its primary source -- this batch's NO_MATCH/POSSIBLE_MATCH coverage comes entirely from the synthetic set, so don't treat "MATCH" as correlated with "VERIFIED_REAL" when training/testing -- that correlation is an artifact of this batch's construction, not a real-world pattern.
