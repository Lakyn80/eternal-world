# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch B`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `qwen3_embedding_0_6b`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated providers: `qwen3_embedding_0_6b`
- Comparison scope: Only multilingual_e5_base and qwen3_embedding_0_6b are included in the final Batch B comparison; weaker historical providers, Jina, and larger Qwen candidates are excluded.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_4b, qwen3_embedding_8b
- Winner: `qwen3_embedding_0_6b`
- Recommendation: Batch B indicates `qwen3_embedding_0_6b` beat the baseline `multilingual_e5_base`; review the successful BGE-M3 hybrid candidate for promotion.

## Technical Summary
- Run type: `full_version_batch_b`
- Execution mode: `full_version_batch_b_real_eval`
- Benchmark status: `completed`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `n/a`
- Preflight validation: `n/a`
- Preflight missing marker count: `n/a`
- Used fake models: `false`
- Historical current winner before Batch B: `bge_m3`
- Any new provider beat baseline/current winner: `true`
- Timestamp: 2026-07-03T18:53:40.657850+00:00
- Note: Jina Embeddings v3 was not rerun and is not compared in Batch B.

## Dataset Questions Used
- Question 1: `distractor-twin-innkeepers` -> Which Marta kept the North Inn ledger, and what detail identified her apron?
- Question 2: `distractor-june-market-date` -> Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?
- Question 3: `distractor-two-levs` -> Which Lev repaired the oak barrels, not the one who worked by the ferry?
- Question 4: `distractor-similar-islands` -> Which island shed kept the painted blue oar, and which similar island name is only a distractor?
- Question 5: `distractor-letter-mixup` -> Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?
- Question 6: `distractor-006` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 7: `distractor-007` -> Which place held the true profile detail for Nikola, not the nearly identical place name?
- Question 8: `distractor-008` -> Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 9: `distractor-009` -> Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?
- Question 10: `distractor-010` -> Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?
- Question 11: `distractor-011` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 12: `distractor-012` -> Which place held the true profile detail for Zora, not the nearly identical place name?
- Question 13: `distractor-013` -> Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 14: `distractor-014` -> Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?
- Question 15: `distractor-015` -> Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?
- Question 16: `distractor-016` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 17: `distractor-017` -> Which place held the true profile detail for Boris, not the nearly identical place name?
- Question 18: `distractor-018` -> Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 19: `distractor-019` -> Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?
- Question 20: `distractor-020` -> Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?
- Question 21: `distractor-021` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 22: `distractor-022` -> Which place held the true profile detail for Talia, not the nearly identical place name?
- Question 23: `distractor-023` -> Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 24: `distractor-024` -> Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?
- Question 25: `distractor-025` -> Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?
- Question 26: `distractor-026` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 27: `distractor-027` -> Which place held the true profile detail for Tomas, not the nearly identical place name?
- Question 28: `distractor-028` -> Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 29: `distractor-029` -> Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?
- Question 30: `distractor-030` -> Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?
- Question 31: `distractor-031` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 32: `distractor-032` -> Which place held the true profile detail for Yara, not the nearly identical place name?
- Question 33: `distractor-033` -> Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 34: `distractor-034` -> Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?
- Question 35: `distractor-035` -> Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?
- Question 36: `distractor-036` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 37: `distractor-037` -> Which place held the true profile detail for Damir, not the nearly identical place name?
- Question 38: `distractor-038` -> Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 39: `distractor-039` -> Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?
- Question 40: `distractor-040` -> Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?
- Question 41: `distractor-041` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 42: `distractor-042` -> Which place held the true profile detail for Kira, not the nearly identical place name?
- Question 43: `distractor-043` -> Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 44: `distractor-044` -> Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?
- Question 45: `distractor-045` -> Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?
- Question 46: `distractor-046` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 47: `distractor-047` -> Which place held the true profile detail for Nikola, not the nearly identical place name?
- Question 48: `distractor-048` -> Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 49: `distractor-049` -> Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?
- Question 50: `distractor-050` -> Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?
- Question 51: `distractor-051` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 52: `distractor-052` -> Which place held the true profile detail for Zora, not the nearly identical place name?
- Question 53: `distractor-053` -> Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 54: `distractor-054` -> Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?
- Question 55: `distractor-055` -> Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?
- Question 56: `distractor-056` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 57: `distractor-057` -> Which place held the true profile detail for Boris, not the nearly identical place name?
- Question 58: `distractor-058` -> Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 59: `distractor-059` -> Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?
- Question 60: `distractor-060` -> Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?
- Question 61: `distractor-061` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 62: `distractor-062` -> Which place held the true profile detail for Talia, not the nearly identical place name?
- Question 63: `distractor-063` -> Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 64: `distractor-064` -> Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?
- Question 65: `distractor-065` -> Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?
- Question 66: `distractor-066` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 67: `distractor-067` -> Which place held the true profile detail for Tomas, not the nearly identical place name?
- Question 68: `distractor-068` -> Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 69: `distractor-069` -> Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?
- Question 70: `distractor-070` -> Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?
- Question 71: `distractor-071` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 72: `distractor-072` -> Which place held the true profile detail for Yara, not the nearly identical place name?
- Question 73: `distractor-073` -> Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 74: `distractor-074` -> Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?
- Question 75: `distractor-075` -> Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?
- Question 76: `distractor-076` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 77: `distractor-077` -> Which place held the true profile detail for Damir, not the nearly identical place name?
- Question 78: `distractor-078` -> Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 79: `distractor-079` -> Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?
- Question 80: `distractor-080` -> Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?
- Question 81: `distractor-081` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 82: `distractor-082` -> Which place held the true profile detail for Kira, not the nearly identical place name?
- Question 83: `distractor-083` -> Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 84: `distractor-084` -> Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?
- Question 85: `distractor-085` -> Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?
- Question 86: `distractor-086` -> Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Question 87: `distractor-087` -> Which place held the true profile detail for Nikola, not the nearly identical place name?
- Question 88: `distractor-088` -> Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Question 89: `distractor-089` -> Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?
- Question 90: `distractor-090` -> Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?
- Question 91: `distractor-091` -> Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Question 92: `distractor-092` -> Which place held the true profile detail for Zora, not the nearly identical place name?
- Question 93: `distractor-093` -> Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Question 94: `distractor-094` -> Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?
- Question 95: `distractor-095` -> Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?
- Question 96: `distractor-096` -> Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Question 97: `distractor-097` -> Which place held the true profile detail for Boris, not the nearly identical place name?
- Question 98: `distractor-098` -> Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Question 99: `distractor-099` -> Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?
- Question 100: `distractor-100` -> Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Providers
- `qwen3_embedding_0_6b`

## Per-Question Result Comparison
### Question 1 - distractor-twin-innkeepers
- Question text: Which Marta kept the North Inn ledger, and what detail identified her apron?
- Final evaluated answer: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Correctness verdict: grounded
- Evidence used: Marta of North Inn, green apron
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 1).
- Losing model issue: qwen3_embedding_0_6b distractors Marta of River Inn
- Distractors / false positives: Marta of River Inn

### Question 2 - distractor-june-market-date
- Question text: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, June 14 night market
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 1).
- Losing model issue: qwen3_embedding_0_6b distractors June 4 noon market
- Distractors / false positives: June 4 noon market

### Question 3 - distractor-two-levs
- Question text: Which Lev repaired the oak barrels, not the one who worked by the ferry?
- Final evaluated answer: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Lev the cooper, oak barrel hoops
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 1).
- Losing model issue: qwen3_embedding_0_6b distractors Lev the ferryman
- Distractors / false positives: Lev the ferryman

### Question 4 - distractor-similar-islands
- Question text: Which island shed kept the painted blue oar, and which similar island name is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Correctness verdict: grounded
- Evidence used: Fog Island ferry shed, painted blue oar
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors Fox Island ferry shed
- Distractors / false positives: Fox Island ferry shed

### Question 5 - distractor-letter-mixup
- Question text: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?
- Final evaluated answer: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Correctness verdict: grounded
- Evidence used: Ada's winter letter, violet wax thread
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors Alda's spring letter
- Distractors / false positives: Alda's spring letter

### Question 6 - distractor-006
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 16 Bellwater Fair
- Distractors / false positives: none

### Question 7 - distractor-007
- Question text: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, brass compass
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 8 - distractor-008
- Question text: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Correctness verdict: grounded
- Evidence used: Sonya of North Orchard lane, linen wick
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors tuning fork
- Distractors / false positives: tuning fork

### Question 9 - distractor-009
- Question text: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, star ledger page
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 10 - distractor-010
- Question text: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Correctness verdict: grounded
- Evidence used: Selma of Birch Ferry shed, lantern hook
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 11 - distractor-011
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 21 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 12 - distractor-012
- Question text: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, wax thread.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, wax thread
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 13 - distractor-013
- Question text: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Correctness verdict: grounded
- Evidence used: Vesna of Ridge Post loft, tin key
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 14 - distractor-014
- Question text: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, blue oar
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 15 - distractor-015
- Question text: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Correctness verdict: grounded
- Evidence used: Ilya of Bell Bridge square, willow basket
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 16 - distractor-016
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 26 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_base`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: qwen3_embedding_0_6b missing March 26 Bellwater Fair
- Distractors / false positives: none

### Question 17 - distractor-017
- Question text: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Moon Mill yard, glass ink bottle.
- Correctness verdict: partial
- Evidence used: Moon Mill yard, glass ink bottle
- Model comparison: multilingual_e5_base -> verdict=no_evidence coverage=0.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- Losing model issue: multilingual_e5_base missing Moon Mill yard, glass ink bottle
- Distractors / false positives: none

### Question 18 - distractor-018
- Question text: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Daria of Winter Chapel porch, copper wind vane pin
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 19 - distractor-019
- Question text: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 20 - distractor-020
- Question text: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Ada of Star Basin gallery, violet ribbon
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 21 - distractor-021
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 13 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_base`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: qwen3_embedding_0_6b missing March 13 Bellwater Fair
- Distractors / false positives: none

### Question 22 - distractor-022
- Question text: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, rope bridge permit
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 23 - distractor-023
- Question text: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Viktor of North Orchard lane, oak barrel hoops
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 24 - distractor-024
- Question text: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, blue glass jar
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 25 - distractor-025
- Question text: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Correctness verdict: grounded
- Evidence used: Anton of Birch Ferry shed, canal route map
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 26 - distractor-026
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 18 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 18 Bellwater Fair
- Distractors / false positives: none

### Question 27 - distractor-027
- Question text: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, copper token.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, copper token
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 28 - distractor-028
- Question text: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Vera of Ridge Post loft, moonflower cutting
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors star ledger page
- Distractors / false positives: star ledger page

### Question 29 - distractor-029
- Question text: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 30 - distractor-030
- Question text: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Lina of Bell Bridge square, saffron scarf
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 31 - distractor-031
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Correctness verdict: partial
- Evidence used: Cedar Hill station
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: multilingual_e5_base missing March 23 Bellwater Fair
- Distractors / false positives: none

### Question 32 - distractor-032
- Question text: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, amber lantern
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 33 - distractor-033
- Question text: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Lev of Winter Chapel porch, basalt sketch
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 34 - distractor-034
- Question text: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, green apron
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 35 - distractor-035
- Question text: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Correctness verdict: grounded
- Evidence used: Pavel of Star Basin gallery, silver booth token
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 36 - distractor-036
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 10 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 10 Bellwater Fair
- Distractors / false positives: none

### Question 37 - distractor-037
- Question text: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, juniper bundles
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 38 - distractor-038
- Question text: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Nessa of North Orchard lane, smoke vent chain
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 39 - distractor-039
- Question text: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, brass compass
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 40 - distractor-040
- Question text: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Correctness verdict: grounded
- Evidence used: Mira of Birch Ferry shed, linen wick
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors Tomas of Birch Ferry shed
- Distractors / false positives: Tomas of Birch Ferry shed

### Question 41 - distractor-041
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 15 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 15 Bellwater Fair
- Distractors / false positives: none

### Question 42 - distractor-042
- Question text: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, lantern hook
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 43 - distractor-043
- Question text: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Petar of Ridge Post loft, weathered camera strap
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 44 - distractor-044
- Question text: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, wax thread
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 45 - distractor-045
- Question text: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Correctness verdict: grounded
- Evidence used: Stefan of Bell Bridge square, tin key
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 46 - distractor-046
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 20 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 20 Bellwater Fair
- Distractors / false positives: none

### Question 47 - distractor-047
- Question text: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Moon Mill yard, willow basket.
- Correctness verdict: partial
- Evidence used: Moon Mill yard, willow basket
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 4).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 48 - distractor-048
- Question text: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Sonya of Winter Chapel porch, paper moon mask
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 49 - distractor-049
- Question text: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 50 - distractor-050
- Question text: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Selma of Star Basin gallery, copper wind vane pin
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 51 - distractor-051
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 25 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_base`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: qwen3_embedding_0_6b missing March 25 Bellwater Fair
- Distractors / false positives: none

### Question 52 - distractor-052
- Question text: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, violet ribbon
- Model comparison: multilingual_e5_base -> verdict=no_evidence coverage=0.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- Losing model issue: multilingual_e5_base missing Blue Trunk cabin, violet ribbon
- Distractors / false positives: none

### Question 53 - distractor-053
- Question text: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Correctness verdict: grounded
- Evidence used: Vesna of North Orchard lane, tuning fork
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 54 - distractor-054
- Question text: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 55 - distractor-055
- Question text: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Ilya of Birch Ferry shed, oak barrel hoops
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 56 - distractor-056
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 12 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 12 Bellwater Fair
- Distractors / false positives: none

### Question 57 - distractor-057
- Question text: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, canal route map.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, canal route map
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 58 - distractor-058
- Question text: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Daria of Ridge Post loft, cedar shovel
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 59 - distractor-059
- Question text: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, copper token
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 60 - distractor-060
- Question text: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Ada of Bell Bridge square, moonflower cutting
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 61 - distractor-061
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 17 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 62 - distractor-062
- Question text: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, saffron scarf
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 3).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 63 - distractor-063
- Question text: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Viktor of Winter Chapel porch, carved shell comb
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 64 - distractor-064
- Question text: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, amber lantern
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 65 - distractor-065
- Question text: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Anton of Star Basin gallery, basalt sketch
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 66 - distractor-066
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 22 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 22 Bellwater Fair
- Distractors / false positives: none

### Question 67 - distractor-067
- Question text: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, silver booth token
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 68 - distractor-068
- Question text: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Vera of North Orchard lane, clay watering cup
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 69 - distractor-069
- Question text: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, juniper bundles
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 70 - distractor-070
- Question text: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Lina of Birch Ferry shed, smoke vent chain
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 71 - distractor-071
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 27 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_base`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: qwen3_embedding_0_6b missing March 27 Bellwater Fair
- Distractors / false positives: none

### Question 72 - distractor-072
- Question text: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, linen wick.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, linen wick
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 73 - distractor-073
- Question text: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Correctness verdict: grounded
- Evidence used: Lev of Ridge Post loft, star ledger page
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 74 - distractor-074
- Question text: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 75 - distractor-075
- Question text: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Pavel of Bell Bridge square, weathered camera strap
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 76 - distractor-076
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 14 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 14 Bellwater Fair
- Distractors / false positives: none

### Question 77 - distractor-077
- Question text: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, tin key.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, tin key
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 78 - distractor-078
- Question text: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Correctness verdict: grounded
- Evidence used: Nessa of Winter Chapel porch, blue oar
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 79 - distractor-079
- Question text: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, willow basket
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 80 - distractor-080
- Question text: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Mira of Star Basin gallery, paper moon mask
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors Tomas of Star Basin gallery
- Distractors / false positives: Tomas of Star Basin gallery

### Question 81 - distractor-081
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 19 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 82 - distractor-082
- Question text: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, copper wind vane pin
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 83 - distractor-083
- Question text: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Petar of North Orchard lane, coal stove hiss
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 84 - distractor-084
- Question text: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, violet ribbon
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 85 - distractor-085
- Question text: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Correctness verdict: grounded
- Evidence used: Stefan of Birch Ferry shed, tuning fork
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 86 - distractor-086
- Question text: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 24 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 24 Bellwater Fair
- Distractors / false positives: none

### Question 87 - distractor-087
- Question text: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, oak barrel hoops
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 88 - distractor-088
- Question text: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Sonya of Ridge Post loft, blue glass jar
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 89 - distractor-089
- Question text: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, canal route map
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 90 - distractor-090
- Question text: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Selma of Bell Bridge square, cedar shovel
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 91 - distractor-091
- Question text: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 11 Bellwater Fair
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 11 Bellwater Fair
- Distractors / false positives: none

### Question 92 - distractor-092
- Question text: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Moon Mill yard, moonflower cutting.
- Correctness verdict: partial
- Evidence used: Moon Mill yard, moonflower cutting
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 4).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 93 - distractor-093
- Question text: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Vesna of Winter Chapel porch, birch tea flask
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 94 - distractor-094
- Question text: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, saffron scarf
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 95 - distractor-095
- Question text: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Ilya of Star Basin gallery, carved shell comb
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 96 - distractor-096
- Question text: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_base -> verdict=partial coverage=0.5; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: multilingual_e5_base missing March 16 Bellwater Fair
- Distractors / false positives: none

### Question 97 - distractor-097
- Question text: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, basalt sketch
- Model comparison: multilingual_e5_base -> verdict=partial coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (3 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 98 - distractor-098
- Question text: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Correctness verdict: grounded
- Evidence used: Daria of North Orchard lane, green apron
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Fewer distractors (2 vs 0).
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 99 - distractor-099
- Question text: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, silver booth token
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `qwen3_embedding_0_6b`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 100 - distractor-100
- Question text: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Ada of Birch Ferry shed, clay watering cup
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Fewer distractors (0 vs 2).
- Losing model issue: qwen3_embedding_0_6b distractors Nikola of Birch Ferry shed
- Distractors / false positives: Nikola of Birch Ferry shed

## Aggregate Metrics

### multilingual_e5_base
- Question wins: 35
- Passed questions: 72
- Evidence coverage: 0.92
- Missing evidence count: 16
- False-positive count: 0
- Latency comparison value: 212.31009999999998
- First relevant rank average: 1.102

### qwen3_embedding_0_6b
- Question wins: 65
- Passed questions: 82
- Evidence coverage: 0.975
- Missing evidence count: 5
- False-positive count: 10
- Latency comparison value: 420.09574999999995
- First relevant rank average: 1.19

## Winner
- Batch B winner: `qwen3_embedding_0_6b`

## Recommendation
- Recommended active model: `qwen3_embedding_0_6b`
- Production recommendation: Batch B indicates `qwen3_embedding_0_6b` beat the baseline `multilingual_e5_base`; review the successful BGE-M3 hybrid candidate for promotion.

## Safety Notes
- Newly run providers requested: `qwen3_embedding_0_6b`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_4b, qwen3_embedding_8b
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`
- Latest full-version Batch A artifacts overwritten: `false`
- Latest full-version Batch B artifacts overwritten: `false`
- Latest full-version Batch C artifacts overwritten: `false`
- Jina Embeddings v3 was not rerun and is not compared in Batch B.

## Artifact Files
- Latest Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_b/real_question_eval_report.md`
- Latest JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_b/real_question_eval_result.json`
- Latest Summary Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_b/real_question_eval_summary.md`
- Latest Summary JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_b/real_question_eval_summary.json`
- Archived Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_185340Z_full_version_batch_b/real_question_eval_report.md`
- Archived JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_185340Z_full_version_batch_b/real_question_eval_result.json`
- Archived Summary Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_185340Z_full_version_batch_b/real_question_eval_summary.md`
- Archived Summary JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_185340Z_full_version_batch_b/real_question_eval_summary.json`

## Developer Details

### distractor-twin-innkeepers
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 1).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: Marta of River Inn
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Marta of North Inn, green apron. Distractors present: Marta of River Inn.
- Verdict: partial

### distractor-june-market-date
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 1).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: June 4 noon market
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Bell Bridge square, June 14 night market. Distractors present: June 4 noon market.
- Verdict: partial

### distractor-two-levs
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 1).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: Lev the ferryman
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Lev the cooper, oak barrel hoops. Distractors present: Lev the ferryman.
- Verdict: partial

### distractor-similar-islands
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: Fox Island ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Fog Island ferry shed, painted blue oar. Distractors present: Fox Island ferry shed.
- Verdict: partial

### distractor-letter-mixup
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: Alda's spring letter
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ada's winter letter, violet wax thread. Distractors present: Alda's spring letter.
- Verdict: partial

### distractor-006
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

### distractor-007
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Blue Trunk cabin, brass compass.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Verdict: grounded

### distractor-008
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: tuning fork
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Sonya of North Orchard lane, linen wick. Distractors present: tuning fork.
- Verdict: partial

### distractor-009
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

### distractor-010
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

### distractor-011
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

### distractor-012
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, wax thread.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, wax thread.
- Verdict: grounded

### distractor-013
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

### distractor-014
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

### distractor-015
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

### distractor-016
- Winner: `multilingual_e5_base`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 26 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 26 Bellwater Fair.
- Verdict: partial

### distractor-017
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.00).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 4
- Answer summary: Partially grounded by: Moon Mill yard, glass ink bottle.
- Verdict: partial

### distractor-018
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

### distractor-019
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

### distractor-020
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

### distractor-021
- Winner: `multilingual_e5_base`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 13 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 13 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 13 Bellwater Fair.
- Verdict: partial

### distractor-022
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, rope bridge permit.
- Verdict: grounded

### distractor-023
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Verdict: grounded

### distractor-024
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

### distractor-025
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Verdict: grounded

### distractor-026
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk
- Missing markers: March 18 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 18 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 18 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Verdict: grounded

### distractor-027
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, copper token.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, copper token.
- Verdict: grounded

### distractor-028
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: star ledger page
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Vera of Ridge Post loft, moonflower cutting. Distractors present: star ledger page.
- Verdict: partial

### distractor-029
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

### distractor-030
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

### distractor-031
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 23 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 23 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Verdict: partial

### distractor-032
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

### distractor-033
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

### distractor-034
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

### distractor-035
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

### distractor-036
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 10 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 10 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 10 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Verdict: grounded

### distractor-037
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, juniper bundles.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Verdict: grounded

### distractor-038
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

### distractor-039
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

### distractor-040
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: Tomas of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Mira of Birch Ferry shed, linen wick. Distractors present: Tomas of Birch Ferry shed.
- Verdict: partial

### distractor-041
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk
- Missing markers: March 15 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 15 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 15 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Verdict: grounded

### distractor-042
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, lantern hook.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Verdict: grounded

### distractor-043
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

### distractor-044
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

### distractor-045
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

### distractor-046
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 20 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 20 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 20 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Verdict: grounded

### distractor-047
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 4).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 4
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

### distractor-048
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

### distractor-049
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

### distractor-050
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: grounded

### distractor-051
- Winner: `multilingual_e5_base`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 25 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 25 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 25 Bellwater Fair.
- Verdict: partial

### distractor-052
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.00).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: none
- Missing markers: Blue Trunk cabin, violet ribbon
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

### distractor-053
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

### distractor-054
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

### distractor-055
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

### distractor-056
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk
- Missing markers: March 12 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 12 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 12 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Verdict: grounded

### distractor-057
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, canal route map.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, canal route map.
- Verdict: grounded

### distractor-058
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

### distractor-059
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

### distractor-060
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

### distractor-061
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 17 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 17 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Verdict: grounded

### distractor-062
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 3).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Verdict: grounded

### distractor-063
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

### distractor-064
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

### distractor-065
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

### distractor-066
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 22 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 22 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 22 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Verdict: grounded

### distractor-067
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, silver booth token.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

### distractor-068
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

### distractor-069
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

### distractor-070
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

### distractor-071
- Winner: `multilingual_e5_base`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk
- Missing markers: March 27 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 27 Bellwater Fair.
- Verdict: partial

### distractor-072
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, linen wick.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, linen wick.
- Verdict: grounded

### distractor-073
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

### distractor-074
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

### distractor-075
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: grounded

### distractor-076
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 14 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 14 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 14 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Verdict: grounded

### distractor-077
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, tin key.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, tin key.
- Verdict: grounded

### distractor-078
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

### distractor-079
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

### distractor-080
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: Tomas of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Mira of Star Basin gallery, paper moon mask. Distractors present: Tomas of Star Basin gallery.
- Verdict: partial

### distractor-081
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

### distractor-082
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

### distractor-083
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

### distractor-084
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

### distractor-085
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

### distractor-086
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk
- Missing markers: March 24 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 24 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Lantern Row kiosk, March 24 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Verdict: grounded

### distractor-087
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, oak barrel hoops.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, oak barrel hoops.
- Verdict: grounded

### distractor-088
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

### distractor-089
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

### distractor-090
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

### distractor-091
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station
- Missing markers: March 11 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 11 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Cedar Hill station, March 11 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Verdict: grounded

### distractor-092
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 4).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, moonflower cutting.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Moon Mill yard, moonflower cutting.
- Verdict: partial

### distractor-093
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

### distractor-094
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

### distractor-095
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Verdict: grounded

### distractor-096
- Winner: `qwen3_embedding_0_6b`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

### distractor-097
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (3 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, basalt sketch.
- Verdict: partial

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Verdict: grounded

### distractor-098
- Winner: `qwen3_embedding_0_6b`
- Reason: Fewer distractors (2 vs 0).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

### distractor-099
- Winner: `qwen3_embedding_0_6b`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

### distractor-100
- Winner: `multilingual_e5_base`
- Reason: Fewer distractors (0 vs 2).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: Nikola of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ada of Birch Ferry shed, clay watering cup. Distractors present: Nikola of Birch Ferry shed.
- Verdict: partial
