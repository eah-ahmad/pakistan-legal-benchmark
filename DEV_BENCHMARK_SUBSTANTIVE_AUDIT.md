# Substantive Audit Report: Staged 80-Question Development Benchmark

**Document:** `DEV_BENCHMARK_SUBSTANTIVE_AUDIT.md`  
**Date:** November 17, 2026  
**Auditor Mode:** Strictly Read-Only Substantive & Legal Inspection  
**Target File Inspected:** `tests/staged_benchmark_dev.json` (80 questions)  
**Corpus Sources Consulted:** `chunks.json` (1,013 sections), `omitted.json`, `raw/constitution.txt`, `raw/ppc.txt`, `raw/peca.txt`, and project design documents.

---

## 1. Executive Summary & Overall Findings

A rigorous, question-by-question substantive audit of the 80 staged Development benchmark questions was performed. The audit evaluated statutory faithfulness, citation necessity, distractor exclusivity, refusal validity, scenario factual adequacy, multi-hop synthesis, and retrieval query phrasing.

### Key Audit Findings:
1. **Statutory Baseline Accuracy:**  
   All 80 questions strictly adhere to the frozen statutory baseline present in the repository (`raw/*.txt` and `chunks.json`).
   - The constitutional structure accurately incorporates the 27th Amendment Act, 2025 (`raw/constitution.txt`), recognizing the Federal Constitutional Court (`constitution-175B`, `constitution-175E`) and the Judicial Commission (`constitution-175A`).
   - The historical omission of Article 184 (Supreme Court original jurisdiction, marked as omitted in `omitted.json`) is properly accounted for; no question erroneously assigns inter-governmental original jurisdiction to the Supreme Court.
   - The PECA baseline strictly adheres to the enacted Act XL of 2016 in `raw/peca.txt`. The subsequent PECA Amendment Act 2025 is properly categorized as out-of-corpus refusal (`dev_refusal_062`).
2. **Quality Uplift over Legacy Benchmark:**  
   - Mechanical reverse-lookups (*"What is the heading of Section X?"*) have been completely eliminated.
   - Natural-language retrieval questions (`dev_ret_066`–`dev_ret_080`) achieve **0.00 verbatim heading copy**, completely resolving the 100% heading leakage found in legacy `retrieval_test.json`.
3. **Substantive Defect Identified — Missing-Context Refusal Cases:**  
   In Category 4 (Negative/Refusal, items `dev_refusal_054`–`dev_refusal_065`), all 12 items represent unanswerable questions due to non-existent sections, foreign laws, or out-of-corpus statutes. **None of the 12 items explicitly model "missing context within an otherwise valid statutory section"** (i.e. where a question asks about a real section, but retrieved context omits the subclause needed to answer). This is a critical gap for RAG refusal benchmarking.
4. **Overall Benchmark Verdict:** **REVISE (Minor Revision).**  
   The substantive core is highly solid (74/80 questions sound), but 6 specific questions require minor refinement (clarifying distractors, refining multi-hop requirements, and introducing missing-context refusal cases) before freezing.

---

## 2. Detailed Severity Classification

- **Critical Severity (0 questions):** No factually false legal assertions or fatal corpus contradictions.
- **High Severity (2 questions):**
  - `dev_refusal_054`–`dev_refusal_065` collectively: Complete absence of missing-context / incomplete-retrieval refusal cases within Category 4.
  - `dev_mhop_ft_048`: Tests Article 199(1) condition precedent, which is a single-article threshold rather than a true multi-hop cross-provision synthesis.
- **Medium Severity (4 questions):**
  - `dev_rule_ppc_004`: Distractor A ("Simple imprisonment up to two years, or fine, or both") is the general punishment for defamation under PPC 500; the question specifically asks for the "originator", making B correct, but distractor A could cause confusion if "originator" is overlooked.
  - `dev_scen_mcq_031`: Cash removed from company vault with intent to return it. In Pakistani criminal law, temporary deprivation still constitutes dishonest misappropriation under Explanation 1 to Section 403/405, but requires explicit clarification in reasoning points.
  - `dev_mhop_ft_049`: Judicial Commission structure cites only Art. 175A; combining it with Art. 175B/175C would make it a stronger multi-hop item.
  - `dev_scen_ft_044`: Cites both Section 141 and 143; needs clarification whether the question tests the definition, the punishment, or both conjointly.
- **Low Severity / Sound (74 questions):** Fully supported, single defensible answer, verified citations.

---

## 3. Question-by-Question Audit Table (All 80 IDs)

| ID | Category | Law | Cited Chunks | Statutory Faithfulness & Audit Verdict | Severity | Recommended Correction / Notes |
|---|---|:---:|---|---|:---:|---|
| `dev_rule_ppc_001` | Statutory Rule | PPC | `ppc-379` | **Sound.** Section 379 verbatim: imprisonment up to 3 years, or fine, or both. | Low | None. |
| `dev_rule_ppc_002` | Statutory Rule | PPC | `ppc-420` | **Sound.** Section 420 verbatim: imprisonment up to 7 years, and liable to fine. | Low | None. |
| `dev_rule_ppc_003` | Statutory Rule | PPC | `ppc-406` | **Sound.** Section 406 verbatim: imprisonment up to 7 years, or fine, or both. | Low | None. |
| `dev_rule_ppc_004` | Statutory Rule | PPC | `ppc-500` | **Supported.** Proviso to Sec 500 specifies 5 years and min 100k fine for originator. | Medium | Clarify prompt stem: "Under the Proviso to Section 500 PPC..." to avoid collision with general defamation rule. |
| `dev_rule_ppc_005` | Statutory Rule | PPC | `ppc-143` | **Sound.** Section 143 verbatim: imprisonment up to 6 months, or fine, or both. | Low | None. |
| `dev_rule_ppc_006` | Statutory Rule | PPC | `ppc-141` | **Sound.** Section 141 verbatim: assembly of five or more persons. | Low | None. |
| `dev_rule_ppc_007` | Statutory Rule | PPC | `ppc-392` | **Sound.** Section 392 verbatim: rigorous imprisonment not less than 3 years nor more than 10 years. | Low | None. |
| `dev_rule_ppc_008` | Statutory Rule | PPC | `ppc-391` | **Sound.** Section 391 verbatim: five or more persons conjointly. | Low | None. |
| `dev_rule_ppc_009` | Statutory Rule | PPC | `ppc-489F` | **Sound.** Section 489-F verbatim: imprisonment up to 3 years, or fine, or both. | Low | None. |
| `dev_rule_ppc_010` | Statutory Rule | PPC | `ppc-354` | **Sound.** Section 354 verbatim: imprisonment up to 2 years, or fine, or both. | Low | None. |
| `dev_rule_ppc_011` | Statutory Rule | PPC | `ppc-354A` | **Sound.** Section 354-A verbatim: death or imprisonment for life, and liable to fine. | Low | None. |
| `dev_rule_ppc_012` | Statutory Rule | PPC | `ppc-193` | **Sound.** Section 193 para 1: judicial proceeding imprisonment up to 7 years, and liable to fine. | Low | None. |
| `dev_rule_ppc_013` | Statutory Rule | PPC | `ppc-365A` | **Sound.** Section 365-A verbatim: death or imprisonment for life, and forfeiture of property. | Low | None. |
| `dev_rule_ppc_014` | Statutory Rule | PPC | `ppc-302` | **Sound.** Section 302(a) verbatim: death as qisas. | Low | None. |
| `dev_rule_const_015` | Statutory Rule | Constitution | `constitution-25A` | **Sound.** Article 25A verbatim: children of age five to sixteen years. | Low | None. |
| `dev_rule_const_016` | Statutory Rule | Constitution | `constitution-51` | **Sound.** Article 51(1) verbatim: 336 seats. | Low | None. |
| `dev_rule_const_017` | Statutory Rule | Constitution | `constitution-175E` | **Sound.** Article 175E(1) (27th Amdt) verbatim: Federal Constitutional Court has original jurisdiction to exclusion of every other court. | Low | None. |
| `dev_rule_const_018` | Statutory Rule | Constitution | `constitution-9` | **Sound.** Article 9 verbatim: save in accordance with law. | Low | None. |
| `dev_rule_const_019` | Statutory Rule | Constitution | `constitution-10` | **Sound.** Article 10(1) verbatim: consult and be defended by legal practitioner of choice. | Low | None. |
| `dev_rule_const_020` | Statutory Rule | Constitution | `constitution-10A` | **Sound.** Article 10A verbatim: fair trial and due process for civil rights/criminal charge. | Low | None. |
| `dev_rule_const_021` | Statutory Rule | Constitution | `constitution-14` | **Sound.** Article 14(2) verbatim: no person subjected to torture for extracting evidence. | Low | None. |
| `dev_rule_const_022` | Statutory Rule | Constitution | `constitution-25` | **Sound.** Article 25(2) verbatim: no discrimination on basis of sex alone. | Low | None. |
| `dev_rule_const_023` | Statutory Rule | Constitution | `constitution-203D` | **Sound.** Article 203D(1) verbatim: Injunctions of Islam as laid down in Holy Quran and Sunnah. | Low | None. |
| `dev_rule_const_024` | Statutory Rule | Constitution | `constitution-19A` | **Sound.** Article 19A verbatim: subject to regulation and reasonable restrictions imposed by law. | Low | None. |
| `dev_rule_peca_025` | Statutory Rule | PECA | `peca-3` | **Sound.** Section 3 verbatim: imprisonment up to 3 months, or fine up to 50,000 rupees, or both. | Low | None. |
| `dev_rule_peca_026` | Statutory Rule | PECA | `peca-11` | **Sound.** Section 11 verbatim: imprisonment up to 7 years, or fine, or both. | Low | None. |
| `dev_rule_peca_027` | Statutory Rule | PECA | `peca-10` | **Sound.** Section 10 verbatim: imprisonment up to 14 years, or fine up to 50 million rupees, or both. | Low | None. |
| `dev_rule_peca_028` | Statutory Rule | PECA | `peca-14` | **Sound.** Section 14 verbatim: imprisonment up to 2 years, or fine up to 10 million rupees, or both. | Low | None. |
| `dev_rule_peca_029` | Statutory Rule | PECA | `peca-16` | **Sound.** Section 16 verbatim: imprisonment up to 3 years, or fine up to 5 million rupees, or both. | Low | None. |
| `dev_rule_peca_030` | Statutory Rule | PECA | `peca-4` | **Sound.** Section 4 verbatim: imprisonment up to 6 months, or fine up to 100,000 rupees, or both. | Low | None. |
| `dev_scen_mcq_031` | Scenario (MCQ) | PPC | `ppc-405`, `ppc-406` | **Sound.** Entrustment of vault cash; misappropriation constitutes CBT under 405/406. | Medium | Add note in reasoning: temporary conversion still satisfies dishonest intent under PPC 405 Expl 1. |
| `dev_scen_mcq_032` | Scenario (MCQ) | PPC | `ppc-390`, `ppc-392` | **Sound.** Three armed persons at gunpoint = robbery (Section 390/392). Distractor Dacoity (391) requires 5+ persons. | Low | None. Excellent distractor boundary. |
| `dev_scen_mcq_033` | Scenario (MCQ) | PPC | `ppc-489F` | **Sound.** Dishonoured cheque for loan repayment squarely engages Section 489-F. | Low | None. |
| `dev_scen_mcq_034` | Scenario (MCQ) | PECA | `peca-21` | **Sound.** Face superimposed on sexually explicit photo falls under Sec 21(1)(a). 5 years max. | Low | None. Clear statutory fit. |
| `dev_scen_mcq_035` | Scenario (MCQ) | PECA | `peca-24` | **Sound.** Repeated threatening messages causing fear of safety = cyber stalking under Sec 24. | Low | None. |
| `dev_scen_mcq_036` | Scenario (MCQ) | PECA | `peca-16` | **Sound.** Stealing and offering CNIC/biometrics for sale = unauthorized identity info under Sec 16. | Low | None. |
| `dev_scen_mcq_037` | Scenario (MCQ) | Constitution | `constitution-9`, `constitution-10` | **Sound.** 48-hr detention without grounds or magistrate violates Arts 9 and 10. | Low | None. |
| `dev_scen_mcq_038` | Scenario (MCQ) | Constitution | `constitution-14` | **Sound.** Torture for extracting confession violates Art 14(2) specifically. | Low | None. |
| `dev_scen_mcq_039` | Scenario (MCQ) | Constitution | `constitution-19A` | **Sound.** Denying certified procurement records engages Art 19A (Right to information). | Low | None. |
| `dev_scen_mcq_040` | Scenario (MCQ) | PPC | `ppc-391`, `ppc-395` | **Sound.** Six armed bank robbers = dacoity (Section 391/395). Distinct from robbery (3 persons). | Low | None. |
| `dev_scen_ft_041` | Scenario (FT) | PPC | `ppc-420` | **Sound.** Inducing transfer of PKR 15m via forged property deeds = Cheating under Sec 420. | Low | None. |
| `dev_scen_ft_042` | Scenario (FT) | PECA | `peca-10` | **Sound.** Cyber attack threats on power grid = Cyber Terrorism under Sec 10 (critical infrastructure). | Low | None. |
| `dev_scen_ft_043` | Scenario (FT) | Constitution | `constitution-25A` | **Sound.** Denying free schooling to poor children violates Art 25A. | Low | None. |
| `dev_scen_ft_044` | Scenario (FT) | PPC | `ppc-141`, `ppc-143` | **Supported.** 7 armed villagers enforcing property right by force = unlawful assembly. | Medium | Clarify question: explicitly ask to "cite the section that defines the assembly and the section that prescribes the punishment". |
| `dev_scen_ft_045` | Scenario (FT) | PECA | `peca-4` | **Sound.** Copying proprietary code to USB drive = Section 4 PECA (up to 6 months, 100k fine). | Low | None. |
| `dev_mhop_ft_046` | Multi-Hop (FT) | PECA / PPC | `peca-28` | **Sound.** Cites PECA Section 28 as statutory bridge applying PPC to PECA offences. | Low | None. True multi-hop provision. |
| `dev_mhop_ft_047` | Multi-Hop (FT) | Constitution | `constitution-175E` | **Sound.** Federal-Provincial autonomy dispute falls exclusively under FCC (Art 175E, 27th Amdt). | Low | None. |
| `dev_mhop_ft_048` | Multi-Hop (FT) | Constitution | `constitution-199` | **Single-Hop Limitation.** Question asks only about Art 199 condition precedent ("no other adequate remedy"). Does not combine provisions. | High | Expand question to synthesize Art 199 with Art 175E (High Court writ jurisdiction excluded where FCC has exclusive jurisdiction under Art 175E). |
| `dev_mhop_ft_049` | Multi-Hop (FT) | Constitution | `constitution-175A` | **Single-Hop Limitation.** Cites Art 175A alone for Judicial Commission structure. | Medium | Add reference to Art 175B/175C (how Commission nominations feed FCC appointments). |
| `dev_mhop_ft_050` | Multi-Hop (FT) | PECA | `peca-43` | **Sound.** Cites Section 43 exception clauses (sections 10, 13, 14, 21) governing cognizable status. | Low | None. |
| `dev_mhop_ft_051` | Multi-Hop (FT) | PPC | `ppc-390` | **Sound.** Explains statutory transformation of theft (Sec 378) into robbery under Section 390. | Low | None. |
| `dev_mhop_ft_052` | Multi-Hop (FT) | Constitution | `constitution-203D` | **Sound.** Traces legal consequence of Federal Shariat Court declaration under Art 203D(3). | Low | None. |
| `dev_mhop_ft_053` | Multi-Hop (FT) | Constitution | `constitution-19` | **Sound.** Explains statutory qualification of free speech by state security and public order exceptions. | Low | None. |
| `dev_refusal_054` | Refusal | PPC | None | **Sound.** Section 999 PPC does not exist (PPC concludes at Sec 511). | Low | None. |
| `dev_refusal_055` | Refusal | PPC | None | **Sound.** Section 651 PPC does not exist. | Low | None. |
| `dev_refusal_056` | Refusal | Constitution | None | **Sound.** Article 400 Constitution does not exist (ends at Art 280). | Low | None. |
| `dev_refusal_057` | Refusal | Constitution | None | **Sound.** Article 580 Constitution does not exist. | Low | None. |
| `dev_refusal_058` | Refusal | PECA | None | **Sound.** Section 95 PECA does not exist (ends at Sec 56). | Low | None. |
| `dev_refusal_059` | Refusal | CrPC | None | **Sound.** CrPC 1898 appeal time limits are outside the statutory corpus. | Low | None. |
| `dev_refusal_060` | Refusal | QSO | None | **Sound.** Qanun-e-Shahadat Order 1984 electronic evidence is outside corpus. | Low | None. |
| `dev_refusal_061` | Refusal | Companies Act | None | **Sound.** Companies Act 2017 corporate registration is outside corpus. | Low | None. |
| `dev_refusal_062` | Refusal | PECA Excluded | None | **Sound.** PECA Amendment Act 2025 is absent from repository; correctly treated as out-of-corpus. | Low | None. |
| `dev_refusal_063` | Refusal | Foreign Law | None | **Sound.** Indian Bharatiya Nyaya Sanhita is foreign jurisdiction. | Low | None. |
| `dev_refusal_064` | Refusal | Foreign Law | None | **Sound.** US Constitution First Amendment is foreign jurisdiction. | Low | None. |
| `dev_refusal_065` | Refusal | Non-Legal | None | **Sound.** Medical clinical diabetes therapies is non-legal. | Low | None. |
| `dev_ret_066` | Retrieval | PPC | `ppc-489F` | **Sound.** Functional query on dishonestly bounced cheques. 0.00 heading copy. | Low | None. |
| `dev_ret_067` | Retrieval | PPC | `ppc-391` | **Sound.** Functional query on collective looting by 5+ persons. | Low | None. |
| `dev_ret_068` | Retrieval | PPC | `ppc-379` | **Sound.** Natural query on general theft penalty without using heading. | Low | None. |
| `dev_ret_069` | Retrieval | PPC | `ppc-406` | **Sound.** Natural query on fiduciary dishonest misappropriation. | Low | None. |
| `dev_ret_070` | Retrieval | PPC | `ppc-365A` | **Sound.** Natural query on capital abduction for ransom. | Low | None. |
| `dev_ret_071` | Retrieval | PPC | `ppc-141` | **Sound.** Natural query on unlawful gathering definition. | Low | None. |
| `dev_ret_072` | Retrieval | PECA | `peca-11` | **Sound.** Natural query on inciting sectarian hatred online. | Low | None. |
| `dev_ret_073` | Retrieval | PECA | `peca-21` | **Sound.** Natural query on sexually morphed explicit imagery. | Low | None. |
| `dev_ret_074` | Retrieval | PECA | `peca-24` | **Sound.** Natural query on persistent online harassment and stalking. | Low | None. |
| `dev_ret_075` | Retrieval | PECA | `peca-28` | **Sound.** Natural query on PPC applicability clause. | Low | None. |
| `dev_ret_076` | Retrieval | Constitution | `constitution-25A` | **Sound.** Natural query on free compulsory schooling for youth. | Low | None. |
| `dev_ret_077` | Retrieval | Constitution | `constitution-175B` | **Sound.** Natural query on FCC creation and office of Chief Justice. | Low | None. |
| `dev_ret_078` | Retrieval | Constitution | `constitution-203D` | **Sound.** Natural query on Shariat Court authority over legislation. | Low | None. |
| `dev_ret_079` | Retrieval | Constitution | `constitution-14` | **Sound.** Natural query on constitutional prohibition of torture for confessions. | Low | None. |
| `dev_ret_080` | Retrieval | Constitution | `constitution-199` | **Sound.** Natural query on extraordinary High Court judicial review. | Low | None. |

---

## 4. Key Substantive Analysis on Target Focus Areas

### 4.1 PPC Sections 378, 405, 392, and 395
- **Theft vs. Criminal Breach of Trust (`ppc-378` vs `ppc-405`):**  
  Tested in `dev_scen_mcq_031`. The distinguishing legal element—*lawful initial custody/entrustment followed by dishonest conversion* vs. *moving property out of another's possession without consent*—is strictly honored.
- **Robbery vs. Dacoity Thresholds (`ppc-390`, `ppc-391`, `ppc-392`, `ppc-395`):**  
  Tested in `dev_rule_ppc_007`, `dev_rule_ppc_008`, `dev_scen_mcq_032` (3 persons = Robbery), and `dev_scen_mcq_040` (6 persons = Dacoity). The statutory threshold of 5 persons under Section 391 is strictly maintained, ensuring non-overlapping, legally unambiguous distractors.

### 4.2 PECA Sections 21, 24, and 28
- **Modesty vs. Cyberstalking (`peca-21` vs `peca-24`):**  
  `dev_scen_mcq_034` tests superimposing faces over sexually explicit imagery (Section 21(1)(a)), while `dev_scen_mcq_035` tests persistent threatening communications and monitoring (Section 24). The distractors correctly reflect statutory boundaries.
- **PPC Bridge Provision (`peca-28`):**  
  `dev_mhop_ft_046` and `dev_ret_075` accurately formulate the supplementary application of the Penal Code under PECA Section 28.

### 4.3 Constitution Articles 175A, 175B, 175E, and 199
- **Federal Constitutional Court (27th Amendment Act, 2025):**  
  `dev_rule_const_017` and `dev_mhop_ft_047` correctly cite Article 175E(1), which gives original jurisdiction to the FCC *to the exclusion of every other court* in inter-governmental disputes.
- **Treatment of Article 184 (Supreme Court Original Jurisdiction):**  
  The audit confirmed that `constitution-184` is marked as omitted in `omitted.json` following the 27th Amendment. The staged benchmark avoids attributing inter-governmental dispute jurisdiction to the Supreme Court.

### 4.4 PECA Amendment Act 2025 Refusal Example
- `dev_refusal_062` specifically asks about digital warrant powers under the PECA Amendment Act 2025. Because the project corpus contains only Act XL of 2016 (`raw/peca.txt`), the question is properly categorized as `out_of_scope` with `refusal_required: true`.

### 4.5 Gap: Missing-Context Refusal Representation
- **Defect:** While Category 4 covers non-existent sections (`unsupported_provision`), external laws (`out_of_corpus_law`), and foreign jurisdictions, it lacks **partial/missing-context refusal examples** (where a query asks about a valid section like PECA Sec 21, but the prompt's `CONTEXT:\n[...]` omits subclause (b)).
- **Impact on RAG Evaluation:** Without missing-context cases, RAG refusal evaluation cannot test whether the model hallucinates when context retrieval is incomplete or irrelevant.
- **Correction:** In the future Final benchmark expansion (and minor Dev revision), 2 to 3 refusal questions should be designated as `refusal_type: "missing_context"`.

---

## 5. Questions Requiring Qualified Pakistani Legal Expert Review

While all 80 questions are traceable to `chunks.json`, the following 23 questions involve legal interpretations that should be formally reviewed by a licensed Pakistani advocate:
1. **Scenario MCQs (10 items):** `dev_scen_mcq_031` through `dev_scen_mcq_040`.
2. **Scenario Free-Text (5 items):** `dev_scen_ft_041` through `dev_scen_ft_045`.
3. **Multi-Hop Free-Text (8 items):** `dev_mhop_ft_046` through `dev_mhop_ft_053`.

---

## 6. Final Audit Recommendation

**Verdict: REVISE (Minor Revision).**

The staged 80-question Development benchmark is substantively strong, highly accurate against the statutory text, and vastly superior to the legacy prototype. It is recommended to perform the following three minor textual adjustments before freezing:
1. In `dev_mhop_ft_048`, expand the prompt to synthesize Article 199 with Article 175E (High Court writ jurisdiction excluded where FCC has exclusive jurisdiction).
2. In `dev_rule_ppc_004`, clarify the prompt to explicitly specify the "originator" under the Proviso to Section 500 PPC.
3. Reallocate 2 out-of-scope questions to represent explicit **missing-context refusal cases** to ensure comprehensive RAG evaluation.

Once these minor refinements are applied and reviewed by a legal expert, the Development benchmark will be fully approved to serve as the control baseline for expanding to the 320-question Final benchmark.
