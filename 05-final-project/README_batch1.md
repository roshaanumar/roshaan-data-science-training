# Batch 1 — AI Risk Research Assistant Dataset

**128 records** (18 VERIFIED_REAL + 110 SYNTHETIC_TEST_DATA). This is a first installment toward your 1,000–2,000 target, not the full set — see "Known limitations" in `phase3_summary_and_qc_report.md` for why, and the Phase 1 report for how to reach full volume.

## Files
- `master_dataset_batch1.csv` — **authoritative**, every record, one schema, 20 columns per your spec.
- `sanctions.csv`, `regulatory_actions.csv`, `enforcement.csv`, `court_cases.csv`, `companies.csv`, `news_evidence.csv`, `entity_matching_test_cases.csv` — convenience views filtered from the master by theme (a record can legitimately appear in more than one view, e.g. a sanctioned company appears in both `sanctions.csv` and `companies.csv`; the master file is the source of truth for record count).
- `phase3_summary_and_qc_report.md` — counts, distributions, and QC checks (Phase 3 of your spec).

## How this maps to your architecture

| Pipeline stage | What in this dataset exercises it |
|---|---|
| **Search / Provided Sources** | `source_organization`, `source_url`, `source_type` columns simulate what a search stage would retrieve — mix of primary government sources (SEC, DOJ, OFAC) and secondary commentary, so you can test source-quality weighting. |
| **Collect Documents** | `source_url` + `publication_date` give you real, dereferenceable documents for the 18 VERIFIED_REAL rows to test actual document fetching, and a placeholder for synthetic rows so that stage can be stubbed. |
| **Extract Text** | `evidence_text` stands in for what your extraction stage would produce — real rows are paraphrased extracts, synthetic rows are explicitly marked. |
| **Entity Matching** | The core of this batch. `entity_name`, `aliases`, `country`, `date_of_birth` are the inputs; `entity_match_label` (MATCH/POSSIBLE_MATCH/NO_MATCH) and `match_reason` are the ground truth. The 20 same-name-different-person pairs and 15 company name-collision triples (SYN-0001–SYN-0210 range, flagged "Scenario group..." in `notes`) are built specifically to break naive name-only matchers. |
| **LLM Classification** | `risk_category` + `event_type` are the classification targets; the ADM/Luthar (allegation, not settled), FAT Brands (charged then dismissed), and Ivan Sechin (delisted, ambiguous status) records specifically test that your classifier doesn't conflate "charged" with "guilty" or freeze a stale risk status. |
| **Generate Structured Result / Structured JSON** | Every row is already flat and typed — treat one CSV row as one target JSON object; `confidence` and `risk_label` are the fields your generation stage should reproduce or justify. |
| **UI / Report** | `notes` field carries the human-readable caveats (e.g. "litigated, not settled") that a report layer should surface rather than collapse into a bare risk score. |

## Suggested test sequence
1. Run entity matching alone first against `entity_matching_test_cases.csv` (91 rows) — check MATCH/POSSIBLE_MATCH/NO_MATCH accuracy before touching classification at all.
2. Run classification against `enforcement.csv` + `court_cases.csv` — check risk_category/event_type accuracy and, specifically, whether the model respects the allegation-vs-conviction distinction on REAL-0004 (Luthar) and REAL-0008 (FAT Brands).
3. Run the full pipeline end-to-end on `master_dataset_batch1.csv` and compare output against the `risk_label`/`confidence` columns.

## Next batch
Batch 2 would add: more geographic diversity in the VERIFIED_REAL set (EU/UK/UN sanctions, non-US court records), and can scale the synthetic entity-matching set to any size you want — that part doesn't require search, just tell me the target count. Let me know if you'd like me to proceed with Batch 2, or generate the Python script for pulling OpenSanctions/OFAC bulk data to close the volume gap directly.
