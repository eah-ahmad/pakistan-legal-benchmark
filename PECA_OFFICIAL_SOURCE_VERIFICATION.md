# Legal Source Verification Report: Prevention of Electronic Crimes Act (PECA) Corpus

> **Audit Type:** Read-Only Statutory Baseline & Legal Source Verification  
> **Target Corpus Files:** `raw/peca.txt` (103,283 characters, 1,952 lines), `chunks.json` (91 PECA chunks)  
> **Official Primary Sources Consulted:**
> 1. **Principal Act:** *The Prevention of Electronic Crimes Act, 2016* (Act No. XL of 2016), enacted 19 August 2016, Gazette of Pakistan (Extraordinary). Official Repository: [Pakistan Code (pakistancode.gov.pk)](https://pakistancode.gov.pk).
> 2. **Amendment Act:** *The Prevention of Electronic Crimes (Amendment) Act, 2025* (Act No. II of 2025), assented to by the President of Pakistan on 29 January 2025, published in the Gazette of Pakistan (Extraordinary). Official Repository: [National Assembly of Pakistan (na.gov.pk)](https://na.gov.pk) and [Senate of Pakistan (senate.gov.pk)](https://senate.gov.pk).
> 3. **Interim Enactments Noted in Source:** Act No. XXXVII of 2023, Act No. XXV of 2024.
>
> **Audit Status:** Complete  
> **Audit Finding:** **The repository's PECA corpus is NOT the 2016 original act; it is an amended, consolidated text fully incorporating the Prevention of Electronic Crimes (Amendment) Act, 2025 (Act No. II of 2025).**

---

## 1. Executive Summary & Core Discrepancy

A fundamental divergence exists between the project's **declared legal scope** and the **actual physical contents** of the corpus:

1. **Declared Scope in Project Documentation:**  
   `SFT_DATASET_PLAN.md`, `BENCHMARK_EXPANSION_PLAN.md`, `DEV_BENCHMARK_FINAL_AUDIT.md`, and `DEV_LEGAL_REVIEW_PACKAGE.md` repeatedly state:
   > *"PECA 2016 baseline; PECA Amendment Act 2025 excluded as out-of-corpus."*
2. **Actual Physical Contents in Repository:**  
   Both `raw/peca.txt` and `chunks.json` **already incorporate the 2025 Amendment Act (Act No. II of 2025)**. 
   - `raw/peca.txt` contains 24 explicit legislative footnotes citing `Act No. II of 2025` and prints the text of all new chapters and sections.
   - `chunks.json` parses and indexes **91 PECA sections**, including Sections 2A–2W (Social Media Protection and Regulatory Authority), 22A–22C (Child exploitation/grooming), 24A (Cyberbullying), 26A (False/fake information), 29–30 (NCCIA replacement of FIA), 30A–30D (Child protection investigation and trials), 43A (Complaints regarding child cybercrimes), and 50A (Transitory provisions).

This means the corpus accurately represents PECA as amended in 2025, but the **project documentation and benchmark metadata are misaligned with the corpus**. Specifically, question `dev_refusal_062` in the benchmark demands an ungrounded refusal on NCCIA digital warrants on the erroneous pretext that PECA 2025 is absent.

---

## 2. Official Statutory Source Details

| Instrument | Official Citation | Enactment / Assent Date | Official Gazette Publication | Source Authority & URL |
|:---|:---|:---:|:---:|:---|
| **Principal Act** | Act No. XL of 2016 | 19 August 2016 | Gazette of Pakistan, Extraordinary, Part I | Ministry of Law and Justice / [Pakistan Code](https://pakistancode.gov.pk) |
| **Amendment Act 2025** | Act No. II of 2025 | 29 January 2025 | Gazette of Pakistan, Extraordinary, Part I | Majlis-e-Shoora (Parliament) / [National Assembly of Pakistan](https://na.gov.pk) & [Senate of Pakistan](https://senate.gov.pk) |
| **Interim Criminal Law Amdt** | Act No. XXXVII of 2023 | 2023 | Gazette of Pakistan, Extraordinary | National Assembly / Senate of Pakistan |
| **Election/Judicial Amdts** | Act No. XXV of 2024 | 2024 | Gazette of Pakistan, Extraordinary | National Assembly / Senate of Pakistan |

---

## 3. Statutory Verification Matrix: Enacted Provisions vs. Corpus Files

Below is the section-by-section verification of the specific 2025 amendments against `raw/peca.txt` and `chunks.json`:

| Statutory Provision | Official Enacted Title / Subject (Act No. II of 2025) | Presence in `raw/peca.txt` (Page / Line) | Chunk ID in `chunks.json` | Corpus Text Status |
|:---|:---|:---|:---|:---:|
| **Chapter 1A / Sec 2A** | Establishment of the Social Media Protection and Regulatory Authority | Page 11; `raw/peca.txt` | `peca-2A` | **VERIFIED & ACCURATE** |
| **Sections 2B–2W** | Powers, functions, composition, Tribunals, and Complaint Council | Pages 11–21; `raw/peca.txt` | `peca-2B` to `peca-2W` | **VERIFIED & ACCURATE** |
| **Section 22A** | Online grooming, solicitation, and cyber enticement of children | Page 23; `raw/peca.txt` | `peca-22A` | **VERIFIED & ACCURATE** |
| **Section 22B** | Commercial sexual exploitation of children | Page 23; `raw/peca.txt` | `peca-22B` | **VERIFIED & ACCURATE** |
| **Section 22C** | Use of information system for kidnapping, abduction or trafficking of minor | Page 24; `raw/peca.txt` | `peca-22C` | **VERIFIED & ACCURATE** |
| **Section 24A** | Cyberbullying (harassment directed at minors/individuals) | Page 24; `raw/peca.txt` | `peca-24A` | **VERIFIED & ACCURATE** |
| **Section 26A** | Punishment for false and fake information (up to 3 years / 2M PKR fine) | Page 25; `raw/peca.txt` | `peca-26A` | **VERIFIED & ACCURATE** |
| **Section 29** | Investigation agency: Establishment of National Cyber Crime Investigation Agency (NCCIA) replacing FIA | Page 26; `raw/peca.txt` | `peca-29` | **VERIFIED & ACCURATE** |
| **Section 30** | Power to investigate: Joint Investigation Teams comprising NCCIA officers | Page 27; `raw/peca.txt` | `peca-30` | **VERIFIED & ACCURATE** |
| **Section 30A** | Remand procedures for electronic offences | Page 27; `raw/peca.txt` | `peca-30A` | **VERIFIED & ACCURATE** |
| **Section 30B** | Victim and witness protection | Page 27; `raw/peca.txt` | `peca-30B` | **VERIFIED & ACCURATE** |
| **Section 30C** | In-camera trial for offences involving minors/modesty | Page 28; `raw/peca.txt` | `peca-30C` | **VERIFIED & ACCURATE** |
| **Section 30D** | Investigation into child sexual content referred to PTA | Page 28; `raw/peca.txt` | `peca-30D` | **VERIFIED & ACCURATE** |
| **Section 31** | Expedited preservation and acquisition of data | Page 28; `raw/peca.txt` | `peca-31` | **VERIFIED & ACCURATE** |
| **Section 32** | Retention of traffic data | Page 29; `raw/peca.txt` | `peca-32` | **VERIFIED & ACCURATE** |
| **Section 33** | Warrant for search or seizure | Page 29; `raw/peca.txt` | `peca-33` | **VERIFIED & ACCURATE** |
| **Section 34** | Warrant for disclosure of content data | Page 30; `raw/peca.txt` | `peca-34` | **VERIFIED & ACCURATE** |
| **Section 35** | Powers of an authorized officer executing judicial warrant | Page 30; `raw/peca.txt` | `peca-35` | **VERIFIED & ACCURATE** |
| **Section 39** | Real-time collection and recording of information under warrant | Page 32; `raw/peca.txt` | `peca-39` | **VERIFIED & ACCURATE** |
| **Section 43A** | Complaint against cybercrimes against children | Page 34; `raw/peca.txt` | `peca-43A` | **VERIFIED & ACCURATE** |
| **Section 50A** | Transitory provisions transferring functions from prior agency to NCCIA | Page 37; `raw/peca.txt` | `peca-50A` | **VERIFIED & ACCURATE** |

---

## 4. Specific Discrepancies and Evidence

### Discrepancy 1: Legislative Footnotes and Consolidated Formatting
- **Finding:** The source document `raw/peca.txt` is an official, consolidated text formatted with standard parliamentary numbering and legislative insertion footnotes (e.g., `1Ins. by Act No. II of 2025, s.2.`, `1Subs. by Act No. II of 2025, s.5-6.`).
- **Impact:** The text in `raw/peca.txt` is a faithful consolidated copy of the amended Act. It is not an unverified drafting bill or unofficial blog summary.

### Discrepancy 2: Section Count (55 original vs. 91 indexed chunks)
- **Finding:** In the unamended PECA 2016, there were 55 sections. In `chunks.json`, there are **91 PECA chunks**. The additional 36 chunks consist entirely of 2025 amendment insertions:
  - Sections 2A through 2W (23 chunks for Chapter 1A Authority).
  - Sections 22A, 22B, 22C (3 chunks for child offenses).
  - Section 24A (1 chunk for cyberbullying).
  - Section 26A (1 chunk for fake information).
  - Sections 30A, 30B, 30C, 30D (4 chunks for trial/investigation).
  - Section 43A (1 chunk for complaints).
  - Section 50A (1 chunk for transitory authority).
  - Section 51A (1 chunk for regulations).
  - Plus multiple sub-part splits of Section 2 and preliminary sections.

### Discrepancy 3: Contradiction in Benchmark Item `dev_refusal_062`
- **Finding:** In `tests/staged_benchmark_dev.json`, item `dev_refusal_062` reads:
  > **Question:** *"How did the PECA (Amendment) Act, 2025 modify the powers of the National Cyber Crime Investigation Agency regarding digital warrants?"*  
  > **Gold Answer:** `"I don't know - this is not in the provided text."`  
  > **Reasoning:** `["The PECA (Amendment) Act, 2025 is absent from the project's frozen baseline corpus and must be refused."]`
- **Evidence of Error:** Both `peca-29`, `peca-30`, and `peca-50A` in `chunks.json` explicitly define the NCCIA, its powers to investigate, its Joint Investigation Teams, and its transitory succession to digital warrant operations. A retrieval model executing a dense or hybrid search over `chunks.json` will successfully retrieve `peca-29`, `peca-30`, and `peca-33`–`35`, leading a factual model to generate an answer instead of refusing. The benchmark item is therefore invalid under the actual corpus.

---

## 5. Reliability Assessment & Conclusion

### Is the PECA Corpus Reliable as a Legal Baseline?
**YES, with documentation realignment.**

- **Textual Reliability:** `raw/peca.txt` and `chunks.json` accurately represent **PECA 2016 as amended by Act No. II of 2025**. The statutory wording, definitions, penalties, institutional mandates (SMPRA, NCCIA), and special trial procedures match the enacted gazetted text of Act No. II of 2025.
- **Corpus Integrity:** The parsing into `chunks.json` preserved section titles, numbers, and verbatim text without hallucinations or truncations of operative penal language.
- **Project Defect:** The error lies entirely in the **epistemic declaration** within the project's documentation (`SFT_DATASET_PLAN.md`, `BENCHMARK_EXPANSION_PLAN.md`, etc.), which incorrectly claimed that PECA 2025 was omitted, when in fact it had been successfully ingested.

---

## 6. Required Corrections (When Ready to Edit)

1. **Update Corpus Baseline Registries:**
   Update all project plans and review packages to state:
   > *"PECA Baseline: Prevention of Electronic Crimes Act, 2016, as amended by the Prevention of Electronic Crimes (Amendment) Act, 2025 (Act No. II of 2025)."*
2. **Reclassify Benchmark Question `dev_refusal_062`:**
   Because PECA 2025 is inside the corpus, question `dev_refusal_062` cannot serve as an `out_of_corpus_law` refusal. It should be replaced with a genuine out-of-corpus Pakistani statute, such as:
   - *Anti-Terrorism Act, 1997 (Act XXVII of 1997)*
   - *National Accountability Ordinance, 1999 (XVIII of 1999)*
   - *Control of Narcotic Substances Act, 1997 (XXV of 1997)*
3. **No Index Rebuild Necessary:**
   The chunks in `chunks.json` already contain the enacted 2025 text. No re-chunking, re-scraping, or corpus re-indexing of PECA is required.
