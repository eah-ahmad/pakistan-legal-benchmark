# Dev Benchmark Legal Expert Review Package

> **Document Purpose:** This package presents all 80 questions of the Development
> benchmark (`tests/staged_benchmark_dev.json`) for formal review by a qualified
> Pakistani legal advocate or jurist. Each question includes the proposed answer,
> expected citations, and the verbatim statutory excerpt from the frozen experimental corpus.
>
> **This document does NOT constitute legal expert approval.** All `legal_expert_verified`
> fields remain `false`. No benchmark data has been modified to produce this package.

---

## Review Instructions

1. For each question, verify that the **proposed gold answer** is legally correct
   under the cited statutory provisions.
2. For MCQs, verify that exactly **one option** is defensibly correct and all
   distractors are genuinely incorrect.
3. For scenario questions, verify that the **legal characterisation** (offence,
   applicable section, penalty) follows from the facts stated in the question
   and the cited statutory text, without requiring unstated assumptions.
4. For multi-hop questions, verify that the **synthesis** across multiple provisions
   is logically necessary and legally sound.
5. For refusal questions, verify that the **expected refusal** is appropriate and
   that the question cannot be answered from the supplied context or corpus.
6. Record your decision in the **Reviewer Decision** field:
   - **Approved** — The question, answer, and citations are legally correct.
   - **Correction Required** — The answer or citations need specific amendment (provide details).
   - **Disputed** — The legal characterisation is debatable or jurisdiction-dependent (explain).
7. Use the **Reviewer Comments** field for proposed corrections, qualifications,
   or notes on legal interpretation.

---

## Corpus Baseline

| Statute | Version in Corpus | Corpus File |
|:---|:---|:---|
| Constitution of the Islamic Republic of Pakistan, 1973 | Incorporating 26th Amendment Act 2024 and 27th Amendment Act 2025 | `raw/constitution.txt` |
| Pakistan Penal Code 1860 (Act XLV of 1860) | Incorporating Criminal Laws (Amendment) Act 2025 | `raw/ppc.txt` |
| Prevention of Electronic Crimes Act 2016 (Act XL of 2016) | Incorporating Criminal Laws (Amdt) Act 2023 and PECA (Amdt) Act 2025 (Act No. II of 2025) | `raw/peca.txt` |

---

## Summary Statistics

- **Total questions:** 80
- **Statutory Rule:** 31
- **Factual Legal Scenario:** 15
- **Complex Multi-Hop:** 7
- **Negative / Refusal:** 12
- **Retrieval:** 15
- **Questions flagged for expert legal review:** 22
- **Questions requiring only corpus-verification confirmation:** 58

---

## Question 1: `dev_rule_ppc_001`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 379 of the Pakistan Penal Code, what is the maximum term of imprisonment prescribed for the offence of theft?

### Options

- **A.** Two years, or with fine, or with both
- **B.** Three years, or with fine, or with both ✅
- **C.** Five years, or with fine, or with both
- **D.** Seven years, and also liable to fine

### Proposed Gold Answer

**B** — Three years, or with fine, or with both

### Expected Citations

- `ppc-379` — [PPC] Section/Article 379: Punishment for theft

### Required Reasoning Points

- Section 379 PPC provides imprisonment up to three years, or with fine, or with both.

### Statutory Excerpts from Frozen Corpus

#### `ppc-379` — Punishment for theft

```
Punishment for theft. Whoever commits theft shall be punished with imprisonment of either description for a term which may extend to three years, or with fine or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-379`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 2: `dev_rule_ppc_002`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 420 of the Pakistan Penal Code, what is the maximum term of imprisonment for cheating and dishonestly inducing delivery of property?

### Options

- **A.** Three years, and fine
- **B.** Five years, and fine
- **C.** Seven years, and shall also be liable to fine ✅
- **D.** Ten years, without fine

### Proposed Gold Answer

**C** — Seven years, and shall also be liable to fine

### Expected Citations

- `ppc-420` — [PPC] Section/Article 420: Cheating and dishonestly inducing delivery of property

### Required Reasoning Points

- Section 420 PPC prescribes imprisonment up to seven years, and shall also be liable to fine.

### Statutory Excerpts from Frozen Corpus

#### `ppc-420` — Cheating and dishonestly inducing delivery of property

```
Cheating and dishonestly inducing delivery of property. Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security, or anything which is signed or sealed, and which is capable of being converted into a valuable security, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-420`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 3: `dev_rule_ppc_003`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> What is the maximum punishment of imprisonment provided under Section 406 of the Pakistan Penal Code for criminal breach of trust?

### Options

- **A.** Three years, or fine, or both
- **B.** Five years, or fine, or both
- **C.** Seven years, or fine, or both ✅
- **D.** Ten years, and fine

### Proposed Gold Answer

**C** — Seven years, or fine, or both

### Expected Citations

- `ppc-406` — [PPC] Section/Article 406: Punishment for criminal breach of trust

### Required Reasoning Points

- Section 406 PPC provides imprisonment of either description up to seven years, or with fine, or with both.

### Statutory Excerpts from Frozen Corpus

#### `ppc-406` — Punishment for criminal breach of trust

```
Punishment for criminal breach of trust. Whoever commits criminal breach of trust shall be punished with imprisonment of either description for a term which may extend to seven years, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-406`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 4: `dev_rule_ppc_004`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under the Proviso to Section 500 of the Pakistan Penal Code, what specific punishment is prescribed for the originator of a defamatory imputation?

### Options

- **A.** Simple imprisonment up to two years, or fine, or both
- **B.** Imprisonment of either description up to five years, or fine not less than one hundred thousand rupees, or both ✅
- **C.** Rigorous imprisonment up to seven years, and fine
- **D.** Simple imprisonment up to one year, without fine

### Proposed Gold Answer

**B** — Imprisonment of either description up to five years, or fine not less than one hundred thousand rupees, or both

### Expected Citations

- `ppc-500` — [PPC] Section/Article 500: Punishment for defamation

### Required Reasoning Points

- Proviso to Section 500 PPC explicitly provides that the originator of the defamatory imputation shall be punished with imprisonment of either description for a term which may extend to five years, or with fine not less than one hundred thousand rupees, or with both.
- Distinguishes originator from general defamer (who faces simple imprisonment up to two years under the main paragraph of Section 500).

### Statutory Excerpts from Frozen Corpus

#### `ppc-500` — Punishment for defamation

```
Punishment for defamation. Whoever defames another shall be punished with simple imprisonment for a term which may extend to two years, or with fine, or with both :
Provided that the originator of the defamatory imputation shall be punished with imprisonment of either description for a term which may extend to five years, or with fine which shall not be less than one hundred thousand rupees, or with both.
Explanation. “Originator” means the initiator of a defamatory imputation. 1In this section for the word "simple" the word "rigorous" has been subs. in its application to the Province of West Pakistan by (W. P. Act 32 of 1964), s. 2.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-500`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 5: `dev_rule_ppc_005`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 143 of the Pakistan Penal Code, what is the maximum punishment for being a member of an unlawful assembly?

### Options

- **A.** Imprisonment up to six months, or fine, or both ✅
- **B.** Imprisonment up to one year, or fine, or both
- **C.** Imprisonment up to two years, and fine
- **D.** Fine only up to ten thousand rupees

### Proposed Gold Answer

**A** — Imprisonment up to six months, or fine, or both

### Expected Citations

- `ppc-143` — [PPC] Section/Article 143: Punishment

### Required Reasoning Points

- Section 143 PPC provides imprisonment up to six months, or fine, or both.

### Statutory Excerpts from Frozen Corpus

#### `ppc-143` — Punishment

```
Punishment. Whoever is a member of an unlawful assembly, shall be punished with imprisonment of either description for a term which may extend to six months, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-143`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 6: `dev_rule_ppc_006`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 141 of the Pakistan Penal Code, an assembly is designated as an unlawful assembly if it consists of at least how many persons?

### Options

- **A.** Three or more persons
- **B.** Five or more persons ✅
- **C.** Seven or more persons
- **D.** Ten or more persons

### Proposed Gold Answer

**B** — Five or more persons

### Expected Citations

- `ppc-141` — [PPC] Section/Article 141: Unlawful assembly

### Required Reasoning Points

- Section 141 PPC defines an unlawful assembly as an assembly of five or more persons with common unlawful object.

### Statutory Excerpts from Frozen Corpus

#### `ppc-141` — Unlawful assembly

```
Unlawful assembly. An assembly of five or more persons is designated an “unlawful assembly,” if the common object of the persons composing that assembly is First. To overawe by criminal force, or show of criminal force, the Federal or any Provincial Government or Legislature, or any public servant in the exercise of the lawful power of such public servant ; or Second. To resist the execution of any law, or of any legal process ; or Third. To commit any mischief or criminal trespass, or other offence ; or Fourth. By means of criminal force, or show of criminal force, to any person to take or obtain possession of any property, or to deprive any person of the enjoyment of a right of way, or of the use of water or other incorporeal right of which he is in possession or enjoyment, or to enforce any right or supposed right ; or Fifth. By means of criminal force, or show of criminal force, to compel any person to do what he is not legally bound to do, or to omit to do what he is legally entitled to do.
Explanation. An assembly which was not unlawful when it assembled, may subsequently become an unlawful assembly.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-141`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 7: `dev_rule_ppc_007`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 392 of the Pakistan Penal Code, what is the mandatory minimum term of rigorous imprisonment for committing robbery?

### Options

- **A.** Not less than one year
- **B.** Not less than two years
- **C.** Not less than three years ✅
- **D.** Not less than five years

### Proposed Gold Answer

**C** — Not less than three years

### Expected Citations

- `ppc-392` — [PPC] Section/Article 392: Punishment for robbery

### Required Reasoning Points

- Section 392 PPC specifies rigorous imprisonment for a term which shall not be less than three years nor more than ten years.

### Statutory Excerpts from Frozen Corpus

#### `ppc-392` — Punishment for robbery

```
Punishment for robbery. Whoever commits robbery shall be punished with rigorous imprisonment for a term which shall not be less than three years nor more than ten years, and shall also be liable to fine ; and, if the robbery be committed on the highway the imprisonment may be extended to fourteen years.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-392`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 8: `dev_rule_ppc_008`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 391 of the Pakistan Penal Code, what is the minimum number of persons acting conjointly required to constitute the offence of dacoity?

### Options

- **A.** Three persons
- **B.** Four persons
- **C.** Five persons ✅
- **D.** Seven persons

### Proposed Gold Answer

**C** — Five persons

### Expected Citations

- `ppc-391` — [PPC] Section/Article 391: Dacoity

### Required Reasoning Points

- Section 391 PPC specifies when five or more persons conjointly commit or attempt robbery, it constitutes dacoity.

### Statutory Excerpts from Frozen Corpus

#### `ppc-391` — Dacoity

```
Dacoity. When five or more persons conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more every person so committing, attempting or aiding, is said to commit “dacoity”.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-391`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 9: `dev_rule_ppc_009`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 489-F of the Pakistan Penal Code, what is the maximum term of imprisonment for dishonestly issuing a cheque that is dishonoured on presentation?

### Options

- **A.** One year, or with fine, or with both
- **B.** Two years, or with fine, or with both
- **C.** Three years, or with fine, or with both ✅
- **D.** Five years, and fine

### Proposed Gold Answer

**C** — Three years, or with fine, or with both

### Expected Citations

- `ppc-489F` — [PPC] Section/Article 489-F: Dishonestly issuing a cheque

### Required Reasoning Points

- Section 489-F PPC provides imprisonment which may extend to three years, or with fine, or with both.

### Statutory Excerpts from Frozen Corpus

#### `ppc-489F` — Dishonestly issuing a cheque

```
Dishonestly issuing a cheque. Whoever dishonestly issues a cheque towards re-payment of a loan or fulfillment of an obligation which is dishonoured on presentation, shall be punishable with imprisonment which may extend to three years, or with fine, or with both, unless he can establish, for which the burden of proof shall rest on him, that he had made arrangements with his bank to ensure that the cheque would be honoured and that the bank was at fault in not honouring the cheque.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-489F`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 10: `dev_rule_ppc_010`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 354 of the Pakistan Penal Code, what punishment is prescribed for assaulting or using criminal force to a woman with intent to outrage her modesty?

### Options

- **A.** Imprisonment up to two years, or with fine, or with both ✅
- **B.** Imprisonment up to five years, and mandatory fine
- **C.** Death or imprisonment for life
- **D.** Rigorous imprisonment up to seven years

### Proposed Gold Answer

**A** — Imprisonment up to two years, or with fine, or with both

### Expected Citations

- `ppc-354` — [PPC] Section/Article 354: Assault or criminal force to woman with intent to outrage her modesty

### Required Reasoning Points

- Section 354 PPC provides imprisonment of either description up to two years, or with fine, or with both.

### Statutory Excerpts from Frozen Corpus

#### `ppc-354` — Assault or criminal force to woman with intent to outrage her modesty

```
Assault or criminal force to woman with intent to outrage her modesty. Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty, shall be punished with imprisonment of either description for a term which may extend to two years, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-354`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 11: `dev_rule_ppc_011`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 354-A of the Pakistan Penal Code, what is the statutory penalty for assaulting a woman and stripping her of her clothes in a public place?

### Options

- **A.** Imprisonment up to seven years, or fine, or both
- **B.** Imprisonment up to ten years, and fine
- **C.** Imprisonment for life, and shall also be liable to fine ✅
- **D.** Rigorous imprisonment for fourteen years

### Proposed Gold Answer

**C** — Imprisonment for life, and shall also be liable to fine

### Expected Citations

- `ppc-354A` — [PPC] Section/Article 354-A: Assault or use of criminal force to woman and stripping her of her clothes

### Required Reasoning Points

- Under Section 354A PPC, assaulting a woman and stripping her of clothes to public view prescribes imprisonment for life and liability to fine.
- Reference: Criminal Laws (Amendment) Act, 2025 (Act No. XXVII of 2025), Section 2; chunk ppc-354A.

### Statutory Excerpts from Frozen Corpus

#### `ppc-354A` — Assault or use of criminal force to woman and stripping her of her clothes

```
Assault or use of criminal force to woman and stripping her of her clothes._ Whoever assaults or uses criminal force to any women and strips her of her clothes and, in that condition, exposes her to the public view, shall be punished with imprisonment for life, and shall also be liable to fine.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-354A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 12: `dev_rule_ppc_012`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 193 of the Pakistan Penal Code, what is the maximum imprisonment for giving false evidence in a judicial proceeding?

### Options

- **A.** Three years, and fine
- **B.** Five years, and fine
- **C.** Seven years, and shall also be liable to fine ✅
- **D.** Ten years, or fine

### Proposed Gold Answer

**C** — Seven years, and shall also be liable to fine

### Expected Citations

- `ppc-193` — [PPC] Section/Article 193: Punishment for false evidence

### Required Reasoning Points

- Section 193 PPC provides imprisonment up to seven years, and shall also be liable to fine for judicial proceedings.

### Statutory Excerpts from Frozen Corpus

#### `ppc-193` — Punishment for false evidence

```
Punishment for false evidence. Whoever intentionally gives false evidence in any stage of a judicial proceeding, or fabricates false evidence for the purpose of being used in any stage of a judicial proceeding, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine ; and whoever intentionally gives or fabricates false evidence in any other case, shall be punished with imprisonment of either description for a term which may extend to three years, and shall also be liable to fine.
Explanation 1. A trial before a Court-martial 1 is a judicial proceeding.
Explanation 2. An investigation directed by law preliminary to a proceeding before a Court of Justice, is a stage of a judicial proceeding, though that investigation may not take place before a Court of Justice. 2* * * * * * *
Explanation 3. An investigation directed by a Court of Justice according to law, and conducted under the authority of a Court of Justice, is a stage of a judicial proceeding, though that investigation may not take place before a Court of Justice.
Illustration A, in an enquiry before an officer deputed by a Court of Justice to ascertain on the spot the boundaries of land, makes on oath a statement which he knows to be false. As this enquiry is a stage of a judicial proceeding, A has given false evidence.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-193`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 13: `dev_rule_ppc_013`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 365-A of the Pakistan Penal Code, what is the punishment for kidnapping or abducting for extorting property or ransom?

### Options

- **A.** Rigorous imprisonment up to ten years, and fine
- **B.** Death or imprisonment for life, and forfeiture of property ✅
- **C.** Imprisonment for fourteen years, and fine
- **D.** Imprisonment up to seven years, or fine

### Proposed Gold Answer

**B** — Death or imprisonment for life, and forfeiture of property

### Expected Citations

- `ppc-365A` — [PPC] Section/Article 365-A: Kidnapping or abducting for extorting property, valuable security, etc

### Required Reasoning Points

- Section 365-A PPC provides death or imprisonment for life, and shall also be liable to forfeiture of property.

### Statutory Excerpts from Frozen Corpus

#### `ppc-365A` — Kidnapping or abducting for extorting property, valuable security, etc

```
Kidnapping or abducting for extorting property, valuable security, etc. Whoever kidnaps or abducts any person for the purpose of extorting from the person kidnapped or abducted, or from any person interested in the person kidnapped or abducted, any property, whether movable or immovable, or valuable security, or to compel any person to comply with any other demand, whether in cash or otherwise, for obtaining release of the person kidnapped or abducted, shall be punished with death or imprisonment for life and shall also be liable to forfeiture of property.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-365A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 14: `dev_rule_ppc_014`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 302(a) of the Pakistan Penal Code, what is the prescribed punishment for qatl-i-amd committed with premeditation as qisas?

### Options

- **A.** Punished with death as qisas ✅
- **B.** Imprisonment for life as ta'zir
- **C.** Imprisonment up to twenty-five years
- **D.** Payment of diyat only

### Proposed Gold Answer

**A** — Punished with death as qisas

### Expected Citations

- `ppc-302` — [PPC] Section/Article 302: Punishment of qatl-i-amd

### Required Reasoning Points

- Section 302(a) PPC provides punishment with death as qisas.

### Statutory Excerpts from Frozen Corpus

#### `ppc-302` — Punishment of qatl-i-amd

```
Punishment of qatl-i-amd. Whoever commits qatl-e-amd shall, subject to the provisions of this Chapter be
(a) punished with death as qisas;
(b) punished with death for imprisonment for life as ta'zir having regard to the facts and circumstances of the case, if the proof in either of the forms specified in section 304 is not available; or
(c) punished with imprisonment of either description for a term which may extend to twenty-five years, where according to the Injunctions of Islam the punishment of qisas is not applicable :
Provided that nothing in clause (c) shall apply where the principle of fasad-fil-arz is attracted and in such cases only clause (a) or clause (b) shall apply.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-302`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 15: `dev_rule_const_015`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 25A of the Constitution of Pakistan, the State is obligated to provide free and compulsory education to children of which age group?

### Options

- **A.** Four to fourteen years
- **B.** Five to sixteen years ✅
- **C.** Six to fifteen years
- **D.** Five to eighteen years

### Proposed Gold Answer

**B** — Five to sixteen years

### Expected Citations

- `constitution-25A` — [CONSTITUTION] Section/Article 25A: Right to education

### Required Reasoning Points

- Article 25A provides free and compulsory education to all children of the age of five to sixteen years.

### Statutory Excerpts from Frozen Corpus

#### `constitution-25A` — Right to education

```
Right to education. The State shall provide free and compulsory education to all children of the age of five to sixteen years in such manner as may be determined by law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-25A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 16: `dev_rule_const_016`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 51(1) of the Constitution of Pakistan, what is the total number of seats specified for members in the National Assembly?

### Options

- **A.** Three hundred and twenty-six seats
- **B.** Three hundred and thirty-six seats ✅
- **C.** Three hundred and forty-two seats
- **D.** Three hundred and fifty seats

### Proposed Gold Answer

**B** — Three hundred and thirty-six seats

### Expected Citations

- `constitution-51` — [CONSTITUTION] Section/Article 51: National Assembly

### Required Reasoning Points

- Article 51(1) specifies there shall be 336 seats for members in the National Assembly.

### Statutory Excerpts from Frozen Corpus

#### `constitution-51` — National Assembly

```
National Assembly. (1) There shall be three hundred and thirty-six seats for members in the National Assembly, including seats reserved for women and non-Muslims.
(2) A person shall be entitled to vote if
(a) he is a citizen of Pakistan;
(b) he is not less than eighteen years of age;
(c) his name appears on the electoral roll; and
(d) he is not declared by a competent court to be of unsound mind.
(3) The seats in the National Assembly referred to in clause (1), except the seats mentioned in clause (4), shall be allocated to each Province and the Federal Capital as under: General Seats Women Seats Total Seats Balochistan 16 4 20 Khyber Pakhtunkhwa 45 10 55 Punjab 141 32 173 Sindh 61 14 75 Federal Capital 3 - 3 Total 266 60 326
(3A) Notwithstanding anything contained in clause (3) or any other law for the time being in force, the members of the National Assembly from the Federally Administered Tribal Areas to be elected in the general elections, 2018 shall continue till dissolution of the National Assembly and thereafter this clause shall stand omitted.
(4) In addition to the number of seats referred to in clause (3), there shall be, in the National Assembly, ten seats reserved for non- Muslims.
(5) The seats in the National Assembly shall be allocated to each province and the Federal Capital on the basis of population in accordance with the last preceding census officially published:
Provided that for purposes of the next general elections to be held in 2018 and bye-elections related thereto, the allocation shall be made on the basis of provisional results of the 2017 census which shall be published by the Federal Government.
(6) For the purpose of election to the National Assembly,
(a) the constituencies for the general seats shall be single member territorial constituencies and the members to fill such seats shall be elected by direct and free vote in accordance with law;
(b) each Province shall be a single constituency for all seats reserved for women which are al
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-51`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 17: `dev_rule_const_017`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 175E of the Constitution of Pakistan (inserted by the 27th Amendment Act, 2025), which court has exclusive original jurisdiction in disputes between two or more Governments?

### Options

- **A.** The Supreme Court of Pakistan
- **B.** The Federal Constitutional Court ✅
- **C.** The High Court of the capital territory
- **D.** The Federal Shariat Court

### Proposed Gold Answer

**B** — The Federal Constitutional Court

### Expected Citations

- `constitution-175E` — [CONSTITUTION] Section/Article 175E: Original jurisdiction of Federal Constitutional Court

### Required Reasoning Points

- Article 175E(1) gives original jurisdiction to the Federal Constitutional Court to the exclusion of every other court in inter-governmental disputes.

### Statutory Excerpts from Frozen Corpus

#### `constitution-175E` — Original jurisdiction of Federal Constitutional Court

```
Original jurisdiction of Federal Constitutional Court. (1) The Federal Constitutional Court shall, to the exclusion of every other court, have original jurisdiction in any dispute between any two or more Governments.
Explanation.- In this clause, “Governments” means the Federal Government and the Provincial Governments.
(2) In the exercise of the jurisdiction conferred on it by clause (1), the Federal Constitutional Court shall pronounce declaratory judgments only.
(3) Without prejudice to the provisions of Article 199, the Federal Constitutional Court shall, if it considers that a question of public importance with reference to the enforcement of any of the Fundamental Rights conferred by Chapter 1 of Part II is involved, have the power to make an order of the nature mentioned in the said Article:
Provided that, subject to the satisfaction of the Federal Constitutional Court, the jurisdiction under this clause shall only be exercised if an application is filed by a person in that Court.
(4) All petitions which fall under this Article and appeals or review applications against judgments rendered or orders passed under this Article, pending or filed before the Supreme Court or its Constitutional Benches, prior to commencement of the Constitution (Twenty-seventh Amendment) Act, 2025, shall forthwith stand transferred to the Federal Constitutional Court and shall only be heard and decided by the Federal Constitutional Court.
(5) The Federal Constitutional Court may, on its own motion or otherwise, if it considers that the case involves a substantial question of law as to the interpretation of the Constitution, call for the record of any case pending before any court and make such order in the case as it thinks fit.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-175E`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 18: `dev_rule_const_018`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 9 of the Constitution of Pakistan, on what condition can a person be deprived of life or liberty?

### Options

- **A.** Under an executive decree during an emergency
- **B.** Save in accordance with law ✅
- **C.** By judicial discretion without statutory sanction
- **D.** Under public interest guidelines

### Proposed Gold Answer

**B** — Save in accordance with law

### Expected Citations

- `constitution-9` — [CONSTITUTION] Section/Article 9: Security of person

### Required Reasoning Points

- Article 9 provides: No person shall be deprived of life or liberty save in accordance with law.

### Statutory Excerpts from Frozen Corpus

#### `constitution-9` — Security of person

```
Security of person. No person shall be deprived of life or liberty save in accordance with law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-9`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 19: `dev_rule_const_019`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 10(1) of the Constitution of Pakistan, an arrested person cannot be denied which fundamental safeguard?

### Options

- **A.** Immediate release on personal bond
- **B.** The right to consult and be defended by a legal practitioner of his choice ✅
- **C.** Trial within twenty-four hours before a magistrate
- **D.** Immunity from interrogation

### Proposed Gold Answer

**B** — The right to consult and be defended by a legal practitioner of his choice

### Expected Citations

- `constitution-10` — [CONSTITUTION] Section/Article 10: Safeguards as to arrest and detention

### Required Reasoning Points

- Article 10(1) guarantees the right to be informed of grounds and to consult/be defended by legal practitioner.

### Statutory Excerpts from Frozen Corpus

#### `constitution-10` — Safeguards as to arrest and detention

```
Safeguards as to arrest and detention. (1) No person who is arrested shall be detained in custody without being informed, as soon as may be, of the grounds for such arrest, nor shall he be denied the right to consult and be defended by a legal practitioner of his choice.
(2) Every person who is arrested and detained in custody shall be produced before a magistrate within a period of twenty-four hours of such arrest, excluding the time necessary for the journey from the place of arrest to the court of the nearest magistrate, and no such person shall be detained in custody beyond the said period without the authority of a magistrate.
(3) Nothing in clauses (1) and (2) shall apply to any person who is arrested or detained under any law providing for preventive detention.
(4) No law providing for preventive detention shall be made except to deal with persons acting in a manner prejudicial to the integrity, security or defence of Pakistan or any part thereof, or external affairs of Pakistan, or public order, or the maintenance of supplies or services, and no such law shall authorise the detention of a person for a period exceeding three months unless the appropriate Review Board has, after affording him an opportunity of being heard in person, reviewed his case and reported, before the expiration of the said period, that there is, in its opinion, sufficient cause for such detention, and, if the detention is continued after the said period of three months, unless the appropriate Review Board has reviewed his case and reported, before the expiration of each period of three months, that there is, in its opinion, sufficient cause for such detention.
Explanation I. In this Article, “the appropriate Review Board” means,
(i) in the case of a person detained under a Federal law, a Board appointed by the Chief Justice of Supreme Court of Pakistan and consisting of a Chairman and two other persons, each of whom is or has been a Judge of the Supreme Court or a High Court; and
(ii) 
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-10`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 20: `dev_rule_const_020`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Which fundamental right is specifically codified under Article 10A of the Constitution of Pakistan?

### Options

- **A.** Protection against retrospective punishment
- **B.** Right to fair trial for civil rights and criminal charges ✅
- **C.** Inviolability of dignity of man
- **D.** Freedom of assembly

### Proposed Gold Answer

**B** — Right to fair trial for civil rights and criminal charges

### Expected Citations

- `constitution-10A` — [CONSTITUTION] Section/Article 10A: Right to fair trial

### Required Reasoning Points

- Article 10A provides right to fair trial and due process for determination of civil rights or criminal charge.

### Statutory Excerpts from Frozen Corpus

#### `constitution-10A` — Right to fair trial

```
Right to fair trial. For the determination of his civil rights and obligations or in any criminal charge against him a person shall be entitled to a fair trial and due process.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-10A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 21: `dev_rule_const_021`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 14(2) of the Constitution of Pakistan, which specific prohibition is explicitly enacted regarding the extraction of evidence?

### Options

- **A.** No confessions can be recorded by police officers
- **B.** No person shall be subjected to torture for the purpose of extracting evidence ✅
- **C.** Wiretapping is completely prohibited in all cases
- **D.** Search warrants must be issued within two hours

### Proposed Gold Answer

**B** — No person shall be subjected to torture for the purpose of extracting evidence

### Expected Citations

- `constitution-14` — [CONSTITUTION] Section/Article 14: Inviolability of dignity of man, etc

### Required Reasoning Points

- Article 14(2) provides: No person shall be subjected to torture for the purpose of extracting evidence.

### Statutory Excerpts from Frozen Corpus

#### `constitution-14` — Inviolability of dignity of man, etc

```
Inviolability of dignity of man, etc. (1) The dignity of man and, subject to law, the privacy of home, shall be inviolable.
(2) No person shall be subjected to torture for the purpose of extracting evidence.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-14`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 22: `dev_rule_const_022`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 25(2) of the Constitution of Pakistan, discrimination against citizens is prohibited on which specific grounds?

### Options

- **A.** Sex alone ✅
- **B.** Language and province alone
- **C.** Political affiliation
- **D.** Financial status

### Proposed Gold Answer

**A** — Sex alone

### Expected Citations

- `constitution-25` — [CONSTITUTION] Section/Article 25: Equality of citizens

### Required Reasoning Points

- Article 25(2) provides: There shall be no discrimination on the basis of sex alone.

### Statutory Excerpts from Frozen Corpus

#### `constitution-25` — Equality of citizens

```
Equality of citizens. (1) All citizens are equal before law and are entitled to equal protection of law.
(2) There shall be no discrimination on the basis of sex *.
(3) Nothing in this Article shall prevent the State from making any special provision for the protection of women and children.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-25`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 23: `dev_rule_const_023`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 203D of the Constitution of Pakistan, the Federal Shariat Court is empowered to examine laws to determine if they are repugnant to which standard?

### Options

- **A.** International human rights conventions
- **B.** The Injunctions of Islam as laid down in the Holy Quran and Sunnah ✅
- **C.** Common law principles of equity and good conscience
- **D.** Directives of the Council of Common Interests

### Proposed Gold Answer

**B** — The Injunctions of Islam as laid down in the Holy Quran and Sunnah

### Expected Citations

- `constitution-203D` — [CONSTITUTION] Section/Article 203D: Powers, jurisdiction and functions of the Court

### Required Reasoning Points

- Article 203D empowers Court to examine whether any law is repugnant to the Injunctions of Islam as laid down in the Holy Quran and Sunnah.

### Statutory Excerpts from Frozen Corpus

#### `constitution-203D` — Powers, jurisdiction and functions of the Court

```
Powers, jurisdiction and functions of the Court. (1) The Court may, either of its own motion or on the petition of a citizen of Pakistan or the Federal Government or a Provincial Government, examine and decide the question whether or not any law or provision of law is repugnant to the Injunctions of Islam, as laid down in the Holy Quran and the Sunnah of the Holy Prophet, hereinafter referred to as the Injunctions of Islam.
(1A) Where the Court takes up the examination of any law or provision of law under clause
(1) and such law or provision of law appears to it to be repugnant to the Injunctions of Islam, the Court shall cause to be given to the Federal Government in the case of a law with respect to a matter in the Federal Legislative List or to the Provincial Government in the case of a law with respect to a matter not enumerated in the Federal Legislative List, a notice specifying the particular provisions that appear to it to be so repugnant, and afford to such Government adequate opportunity to have its point of view placed before the Court.
(2) If the Court decides that any law or provision of law is repugnant to the Injunctions of Islam, it shall set out in its decision :
(a) the reasons for its holding that opinion; and
(b) the extent to which such law or provision is so repugnant; and specify the day on which the decision shall take effect :
Provided that no such decision shall be deemed to take effect before the expiration of the period within which an appeal therefrom may be preferred to the Supreme Court or, where an appeal has been so preferred, before the disposal of such appeal :
Provided further that appeal against decision given after the commencement of the Constitution (Twenty-sixth Amendment) Act, 2024 (XXVI of 2024) shall be disposed of within twelve months whereafter the decision shall take effect unless suspended by the Supreme Court.
(3) If any law or provision of law is held by the Court to be repugnant to the Injunctions of Islam,
(a) the 
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-203D`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 24: `dev_rule_const_024`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Article 19A of the Constitution of Pakistan, what condition regulates the citizen's fundamental right to have access to information in matters of public importance?

### Options

- **A.** Subject to executive pleasure and ministerial assent
- **B.** Subject to regulation and reasonable restrictions imposed by law ✅
- **C.** Available only to registered media practitioners
- **D.** Applicable only during parliamentary sessions

### Proposed Gold Answer

**B** — Subject to regulation and reasonable restrictions imposed by law

### Expected Citations

- `constitution-19A` — [CONSTITUTION] Section/Article 19A: Right to information

### Required Reasoning Points

- Article 19A provides right to information subject to regulation and reasonable restrictions imposed by law.

### Statutory Excerpts from Frozen Corpus

#### `constitution-19A` — Right to information

```
Right to information. Every citizen shall have the right to have access to information in all matters of public importance subject to regulation and reasonable restrictions imposed by law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-19A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 25: `dev_rule_peca_025`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 3 of PECA 2016, what is the punishment for gaining unauthorized access to an information system or data with dishonest intention?

### Options

- **A.** Imprisonment up to three months, or fine up to fifty thousand rupees, or both ✅
- **B.** Imprisonment up to six months, or fine up to one hundred thousand rupees, or both
- **C.** Imprisonment up to one year, or fine up to two hundred thousand rupees
- **D.** Fine only up to twenty-five thousand rupees

### Proposed Gold Answer

**A** — Imprisonment up to three months, or fine up to fifty thousand rupees, or both

### Expected Citations

- `peca-3` — [PECA] Section/Article 3: Unauthorized access to information system or data

### Required Reasoning Points

- Section 3 PECA provides imprisonment up to three months or with fine up to fifty thousand rupees or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-3` — Unauthorized access to information system or data

```
Unauthorized access to information system or data.— Whoever with dishonest intention gains unauthorized access to any information system or data shall be punished with imprisonment for a term which may extend to three months or with fine which may extend to fifty thousand rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-3`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 26: `dev_rule_peca_026`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 11 of PECA 2016, what is the maximum term of imprisonment for preparing or disseminating information that advances interfaith, sectarian or racial hatred?

### Options

- **A.** Three years, or fine, or both
- **B.** Five years, or fine, or both
- **C.** Seven years, or fine, or both ✅
- **D.** Ten years, and fine

### Proposed Gold Answer

**C** — Seven years, or fine, or both

### Expected Citations

- `peca-11` — [PECA] Section/Article 11: Hate speech

### Required Reasoning Points

- Section 11 PECA provides imprisonment up to seven years or with fine or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-11` — Hate speech

```
Hate speech.— Whoever prepares or disseminates information, through any information system or device, that advances or is likely to advance interfaith, sectarian or racial hatred, shall be punished with imprisonment for a term which may extend to seven years or with fine or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-11`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 27: `dev_rule_peca_027`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 10 of PECA 2016, what is the maximum term of imprisonment prescribed for the offence of cyber terrorism?

### Options

- **A.** Seven years, and fine up to ten million rupees
- **B.** Ten years, or fine up to twenty-five million rupees
- **C.** Fourteen years, or fine up to fifty million rupees, or both ✅
- **D.** Life imprisonment, without fine

### Proposed Gold Answer

**C** — Fourteen years, or fine up to fifty million rupees, or both

### Expected Citations

- `peca-10` — [PECA] Section/Article 10: Cyber terrorism

### Required Reasoning Points

- Section 10 PECA prescribes imprisonment up to fourteen years or with fine up to fifty million rupees or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-10` — Cyber terrorism

```
Cyber terrorism.— Whoever commits or threatens to commit any of the offences under sections 6, 7, 8 or 9, where the commission or threat is with the intent to,—
(a) coerce, intimidate, create a sense of fear, panic or insecurity in the Government or the public or a section of the public or community or sect or create a sense of fear or insecurity in society; or
(b) advance inter-faith, sectarian or ethnic hatred; or
(c) advance the objectives of organizations or individuals or groups proscribed under the law, shall be punished with imprisonment of either description for a term which may extend to fourteen years or with fine which may extend to fifty million rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-10`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 28: `dev_rule_peca_028`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 14 of PECA 2016, what is the maximum penalty for committing electronic fraud with intent for wrongful gain?

### Options

- **A.** Imprisonment up to two years, or fine up to ten million rupees, or both ✅
- **B.** Imprisonment up to three years, or fine up to five million rupees
- **C.** Imprisonment up to five years, and mandatory fine
- **D.** Imprisonment up to seven years, or fine up to one million rupees

### Proposed Gold Answer

**A** — Imprisonment up to two years, or fine up to ten million rupees, or both

### Expected Citations

- `peca-14` — [PECA] Section/Article 14: Electronic fraud

### Required Reasoning Points

- Section 14 PECA provides imprisonment up to two years or with fine up to ten million rupees or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-14` — Electronic fraud

```
Electronic fraud.—Whoever with the intent for wrongful gain interferes with or uses any information system, device or data or induces any person to enter into a relationship or deceives any person, which act or omission is likely to cause damage or harm to that person or any other person shall be punished with imprisonment for a term which may extend to two years or with fine which may extend to ten million rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-14`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 29: `dev_rule_peca_029`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 16 of PECA 2016, what is the maximum punishment for obtaining, selling or transmitting identity information without authorization?

### Options

- **A.** Imprisonment up to one year, or fine up to one million rupees
- **B.** Imprisonment up to three years, or fine up to five million rupees, or both ✅
- **C.** Imprisonment up to five years, and fine
- **D.** Imprisonment up to seven years, without fine

### Proposed Gold Answer

**B** — Imprisonment up to three years, or fine up to five million rupees, or both

### Expected Citations

- `peca-16` — [PECA] Section/Article 16: Unauthorized use of identity information

### Required Reasoning Points

- Section 16 PECA provides imprisonment up to three years or with fine up to five million rupees, or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-16` — Unauthorized use of identity information

```
Unauthorized use of identity information.— (1) Whoever obtains, sells, possesses, transmits or uses another person’s identity information without authorization shall be punished with imprisonment for a term which may extend to three years or with fine which may extend to five million rupees, or with both.
(2) Any person whose identity information is obtained, sold, possessed, used or transmitted may apply to the Authority for securing, destroying, blocking access or preventing transmission of identity information referred to in sub-section (1) and the Authority on receipt of such application may take such measures as deemed appropriate for securing, destroying or preventing transmission of such identity information.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-16`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 30: `dev_rule_peca_030`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | easy |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Under Section 4 of PECA 2016, what is the punishment for copying or transmitting data without authorization and with dishonest intention?

### Options

- **A.** Imprisonment up to six months, or fine up to one hundred thousand rupees, or both ✅
- **B.** Imprisonment up to one year, or fine up to two hundred thousand rupees
- **C.** Imprisonment up to two years, and fine
- **D.** Fine only up to fifty thousand rupees

### Proposed Gold Answer

**A** — Imprisonment up to six months, or fine up to one hundred thousand rupees, or both

### Expected Citations

- `peca-4` — [PECA] Section/Article 4: Unauthorized copying or transmission of data

### Required Reasoning Points

- Section 4 PECA provides imprisonment up to six months or with fine up to one hundred thousand rupees or with both.

### Statutory Excerpts from Frozen Corpus

#### `peca-4` — Unauthorized copying or transmission of data

```
Unauthorized copying or transmission of data.— Whoever with dishonest intention and without authorization copies or otherwise transmits or causes to be transmitted any data shall be punished with imprisonment for a term which may extend to six months, or with fine which may extend to one hundred thousand rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-4`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 31: `dev_scen_mcq_031` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A store employee entrusted with the company vault cash removes PKR 500,000 for his personal investments without authorization, intending to return it later. Which offence under the Pakistan Penal Code has been committed, and what section applies?

### Options

- **A.** Theft under Section 379 PPC
- **B.** Criminal breach of trust under Section 405/406 PPC ✅
- **C.** Cheating under Section 415/420 PPC
- **D.** Extortion under Section 384 PPC

### Proposed Gold Answer

**B** — Criminal breach of trust under Section 405/406 PPC

### Expected Citations

- `ppc-405` — [PPC] Section/Article 405: Criminal breach of trust
- `ppc-406` — [PPC] Section/Article 406: Punishment for criminal breach of trust

### Required Reasoning Points

- Employee was entrusted with dominion over company cash; dishonest misappropriation or conversion to personal use constitutes criminal breach of trust under Section 405 PPC, punishable under Section 406 PPC.
- Under Explanation 1 to Section 403 (applicable via Section 405), a dishonest temporary conversion or misappropriation is sufficient to constitute the offence, so the intention to return the money later does not negate criminal liability.

### Statutory Excerpts from Frozen Corpus

#### `ppc-405` — Criminal breach of trust

```
Criminal breach of trust. Whoever, being in any manner entrusted with property or with any dominion over property, dishonestly misappropriates or converts to his own use that property, or dishonestly uses or disposes of that property in violation of any direction of law prescribing the mode in which such trust is to be discharged, or of any legal contract, express or implied, which he has made touching the discharge of such trust, or wilfully suffers any other person so to do, commits “criminal breach of trust”.
Illustrations
(a) A, being executor to the will of a deceased person, dishonestly disobeys the law which directs him to divide the effects according to the will, and appropriates them to his own use. A has committed criminal breach of trust.
(b) A is a warehouse-keeper. Z, going on a journey, entrusts his furniture to A, under a contract that it shall be returned on payment of a stipulated sum for warehouse-room. A dishonestly sells the goods. A has committed criminal breach of trust.
(c) A, residing in Dacca, is agent for Z, residing at Lahore. There is an express or implied contract between A and Z, that all sums remitted by Z to A shall be invested by A, according to Z’s direction. Z, remits a lakh of rupees to A, with directions to A to invest the same in Company’s paper. A dishonestly disobeys the directions and employs the money in his own business. A has committed criminal breach of trust.
(d) But if A, in the last illustration, not dishonestly but in good faith, believing that it will be more for Z’s advantage to hold shares in the Bank of Bengal, disobeys Z’s directions, and buys shares in the Bank of Bengal, for Z, instead of buying Company’s paper, here, though Z should suffer loss, and should be entitled to bring a civil action against A, on account of that loss, yet A, not having acted dishonestly, has not committed criminal breach of trust.
(e) A, a revenue-officer, is entrusted with public money and is either directed by law, or bound by a con
[... excerpt truncated for review package; full text in chunks.json ...]
```

#### `ppc-406` — Punishment for criminal breach of trust

```
Punishment for criminal breach of trust. Whoever commits criminal breach of trust shall be punished with imprisonment of either description for a term which may extend to seven years, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-405`
- file: `raw/ppc.txt`, chunk_id: `ppc-406`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 32: `dev_scen_mcq_032` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> Three armed individuals enter a residence at night, restrain the occupants at gunpoint, and seize cash and gold. Which offence under the Pakistan Penal Code is committed?

### Options

- **A.** Dacoity under Section 391/395 PPC
- **B.** Robbery under Section 390/392 PPC ✅
- **C.** Theft in a dwelling house under Section 380 PPC only
- **D.** Extortion under Section 383/384 PPC only

### Proposed Gold Answer

**B** — Robbery under Section 390/392 PPC

### Expected Citations

- `ppc-390` — [PPC] Section/Article 390: Robbery When theft is robbery When extortion is robbery
- `ppc-392` — [PPC] Section/Article 392: Punishment for robbery

### Required Reasoning Points

- Because only three persons participated, it does not reach the five-person threshold for dacoity under Section 391; it constitutes robbery under Section 390/392.

### Statutory Excerpts from Frozen Corpus

#### `ppc-390` — Robbery When theft is robbery When extortion is robbery

```
Robbery. In all robbery there is either theft or extortion. When theft is robbery. Theft is “robbery” if, in order to the committing of the theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft, the offender, for that end, voluntarily causes or attempts to cause to any person death or hurt or wrongful restraint, or fear of instant death or of instant hurt, or of instant wrongful restraint. When extortion is robbery. Extortion is “robbery” if the offender, at the time of committing the extortion, is in the presence of the person put in fear, and commits the extortion by putting that lSubs. by the Law Reforms Ordinance, 1972 (12 of 1972), s. 2 and Sch., for “transportation”. person in fear of instant death, of instant hurt, or of instant wrongful restraint to that person, or to some other person, and, by so putting in fear, induces the person so put in fear then and there to deliver up the thing extorted.
Explanation. The offender is said to be present if he is sufficiently near to put the other person in fear of instant death, of instant hurt, or of instant wrongful restraint.
Illustrations
(a) A holds Z down, and fraudulently takes Z’s money and jewels from Z’s clothes, without Z’s consent. Here A has committed theft, and, in order to the committing of that theft, has voluntarily caused wrongful restraint to Z. A has therefore committed robbery.
(b) A meets Z on the high-road, shows a pistol, and demands Z’s purse. Z, in consequence, surrenders his purse. Here A has extorted the purse from Z by putting him in fear of instant hurt, and being at the time of committing the extortion in his presence. A has therefore committed robbery.
(c) A meets Z and Z’s child on the high-road. A takes the child, and threatens to fling it down a precipice, unless Z deliver his purse. Z, in consequence, delivers his purse. Here A has extorted the purse from Z, by causing Z to be in fear of instant hurt to the child who is ther
[... excerpt truncated for review package; full text in chunks.json ...]
```

#### `ppc-392` — Punishment for robbery

```
Punishment for robbery. Whoever commits robbery shall be punished with rigorous imprisonment for a term which shall not be less than three years nor more than ten years, and shall also be liable to fine ; and, if the robbery be committed on the highway the imprisonment may be extended to fourteen years.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-390`
- file: `raw/ppc.txt`, chunk_id: `ppc-392`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 33: `dev_scen_mcq_033` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A borrower issues a bank cheque for PKR 2,000,000 to settle an existing loan, knowing his account holds insufficient funds. The cheque is dishonoured on presentation. Which provision of the Pakistan Penal Code is directly invoked?

### Options

- **A.** Section 420 PPC (Cheating)
- **B.** Section 489-F PPC (Dishonestly issuing a cheque) ✅
- **C.** Section 406 PPC (Criminal breach of trust)
- **D.** Section 468 PPC (Forgery for purpose of cheating)

### Proposed Gold Answer

**B** — Section 489-F PPC (Dishonestly issuing a cheque)

### Expected Citations

- `ppc-489F` — [PPC] Section/Article 489-F: Dishonestly issuing a cheque

### Required Reasoning Points

- Section 489-F specifically penalizes dishonestly issuing a cheque towards repayment of a loan or fulfillment of an obligation.

### Statutory Excerpts from Frozen Corpus

#### `ppc-489F` — Dishonestly issuing a cheque

```
Dishonestly issuing a cheque. Whoever dishonestly issues a cheque towards re-payment of a loan or fulfillment of an obligation which is dishonoured on presentation, shall be punishable with imprisonment which may extend to three years, or with fine, or with both, unless he can establish, for which the burden of proof shall rest on him, that he had made arrangements with his bank to ensure that the cheque would be honoured and that the bank was at fault in not honouring the cheque.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-489F`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 34: `dev_scen_mcq_034` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> An individual superimposes a woman's face over sexually explicit photographs and publicly disseminates them on social media without her consent. Under PECA 2016, which specific offence is committed and what is the maximum term of imprisonment?

### Options

- **A.** Offences against dignity under Section 20, maximum three years
- **B.** Offences against modesty under Section 21(1), maximum five years ✅
- **C.** Cyber stalking under Section 24, maximum three years
- **D.** Electronic forgery under Section 13, maximum seven years

### Proposed Gold Answer

**B** — Offences against modesty under Section 21(1), maximum five years

### Expected Citations

- `peca-21` — [PECA] Section/Article 21: Offences against modesty of a natural person and minor

### Required Reasoning Points

- Superimposing face over explicit imagery falls squarely under Section 21(1)(a) PECA, punishable with imprisonment up to five years or fine up to five million rupees.

### Statutory Excerpts from Frozen Corpus

#### `peca-21` — Offences against modesty of a natural person and minor

```
Offences against modesty of a natural person and minor.—(1) Whoever intentionally and publicly exhibits or displays or transmits any information which,—
(a) superimposes a photograph of the face of a natural person over any sexually explicit image or video; or
(b) includes a photograph or a video of a natural person in sexually explicit conduct; or
(c) intimidates a natural person with any sexual act, or any sexually explicit image or video of a natural person; or
(d) cultivates, entices or induces a natural person to engage in a sexually explicit act, through an information system to harm a natural person or his reputation, or to take revenge, or to create hatred or to blackmail, shall be punished with imprisonment for a term which may extend to five years or with fine which may extend to five million rupees or with both.
(2) Whoever commits an offence under sub-section (1) with respect to a minor shall be punished with imprisonment for a term which may extend to seven years and with fine which may extend to five million rupees:
Provided that in case of a person who has been previously convicted of an offence under sub- section (1) with respect to a minor shall be punished with imprisonment for a term of ten years and with fine.
(3) Any aggrieved person or his guardian, where such person is a minor, may apply to the Authority for removal, destruction of or blocking access to such information referred to in sub-section
(1) and the Authority, on receipt of such application, shall forthwith pass such orders as deemed reasonable in the circumstances including an order for removal, destruction, preventing transmission of or blocking access to such information and the Authority may also direct any of its licensees to secure such information including traffic data.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-21`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 35: `dev_scen_mcq_035` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A perpetrator repeatedly sends threatening and intimidating direct messages and emails to a former colleague, tracking her online activities and causing severe fear of safety. Which provision of PECA 2016 directly applies?

### Options

- **A.** Section 3 (Unauthorized access)
- **B.** Section 20 (Offences against dignity)
- **C.** Section 24 (Cyber stalking) ✅
- **D.** Section 26 (Spoofing)

### Proposed Gold Answer

**C** — Section 24 (Cyber stalking)

### Expected Citations

- `peca-24` — [PECA] Section/Article 24: Cyber stalking

### Required Reasoning Points

- Repeatedly following or communicating with intent to coerce, intimidate or harass constitutes cyber stalking under Section 24 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-24` — Cyber stalking

```
Cyber stalking.— (1) A person commits the offence of cyber stalking who, with the intent to coerce or intimidate or harass any person, uses information system, information system network, the Internet, website, electronic mail or any other similar means of communication to—
(a) follow a person or contacts or attempts to contact such person to foster personal interaction repeatedly despite a clear indication of disinterest by such person;
(b) monitor the use by a person of the internet, electronic mail, text message or any other form of electronic communication;
(c) watch or spy upon a person in a manner that results in fear of violence or serious alarm or distress, in the mind of such person; or
(d) take a photograph or make a video of any person and displays or distributes it without his consent in a manner that harms a person.
(2) Whoever commits the offence specified in sub-section (1) shall be punished with imprisonment for a term which may extend to three years or with fine which may extend to one million rupees or with both:
Provided that if victim of the cyber stalking under sub-section (1) is a minor the punishment may extend to five years or with fine which may extend to ten million rupees or with both.
(3) Any aggrieved person or his guardian, where such person is a minor, may apply to the Authority for removal, destruction of or blocking access to such information referred to in sub-section
(1) and the Authority, on receipt of such application, shall forthwith pass such orders as deemed reasonable in the circumstances including an order for removal, destruction, preventing transmission of or blocking access to such information and the Authority may also direct any of its licensees to secure such information including traffic data.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-24`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 36: `dev_scen_mcq_036` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A hacker breaches the database of a telecom provider and steals customer CNIC and biometric verification data, subsequently offering it for sale on online forums. Which section of PECA 2016 directly penalizes this sale and transmission of identity data?

### Options

- **A.** Section 4 (Unauthorized copying)
- **B.** Section 14 (Electronic fraud)
- **C.** Section 16 (Unauthorized use of identity information) ✅
- **D.** Section 25 (Spamming)

### Proposed Gold Answer

**C** — Section 16 (Unauthorized use of identity information)

### Expected Citations

- `peca-16` — [PECA] Section/Article 16: Unauthorized use of identity information

### Required Reasoning Points

- Obtaining, selling, possessing or transmitting identity information of another person without authorization is penalized under Section 16 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-16` — Unauthorized use of identity information

```
Unauthorized use of identity information.— (1) Whoever obtains, sells, possesses, transmits or uses another person’s identity information without authorization shall be punished with imprisonment for a term which may extend to three years or with fine which may extend to five million rupees, or with both.
(2) Any person whose identity information is obtained, sold, possessed, used or transmitted may apply to the Authority for securing, destroying, blocking access or preventing transmission of identity information referred to in sub-section (1) and the Authority on receipt of such application may take such measures as deemed appropriate for securing, destroying or preventing transmission of such identity information.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-16`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 37: `dev_scen_mcq_037` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A citizen is arrested by law enforcement officers and detained in a police facility for 48 hours without being informed of the grounds of arrest or produced before a magistrate. Which constitutional guarantees are violated?

### Options

- **A.** Article 9 and Article 10 only ✅
- **B.** Article 14 and Article 19 only
- **C.** Article 25 and Article 25A only
- **D.** Article 18 and Article 23 only

### Proposed Gold Answer

**A** — Article 9 and Article 10 only

### Expected Citations

- `constitution-9` — [CONSTITUTION] Section/Article 9: Security of person
- `constitution-10` — [CONSTITUTION] Section/Article 10: Safeguards as to arrest and detention

### Required Reasoning Points

- Article 9 guarantees liberty save in accordance with law; Article 10 requires informing grounds and producing within 24 hours.

### Statutory Excerpts from Frozen Corpus

#### `constitution-9` — Security of person

```
Security of person. No person shall be deprived of life or liberty save in accordance with law.
```

#### `constitution-10` — Safeguards as to arrest and detention

```
Safeguards as to arrest and detention. (1) No person who is arrested shall be detained in custody without being informed, as soon as may be, of the grounds for such arrest, nor shall he be denied the right to consult and be defended by a legal practitioner of his choice.
(2) Every person who is arrested and detained in custody shall be produced before a magistrate within a period of twenty-four hours of such arrest, excluding the time necessary for the journey from the place of arrest to the court of the nearest magistrate, and no such person shall be detained in custody beyond the said period without the authority of a magistrate.
(3) Nothing in clauses (1) and (2) shall apply to any person who is arrested or detained under any law providing for preventive detention.
(4) No law providing for preventive detention shall be made except to deal with persons acting in a manner prejudicial to the integrity, security or defence of Pakistan or any part thereof, or external affairs of Pakistan, or public order, or the maintenance of supplies or services, and no such law shall authorise the detention of a person for a period exceeding three months unless the appropriate Review Board has, after affording him an opportunity of being heard in person, reviewed his case and reported, before the expiration of the said period, that there is, in its opinion, sufficient cause for such detention, and, if the detention is continued after the said period of three months, unless the appropriate Review Board has reviewed his case and reported, before the expiration of each period of three months, that there is, in its opinion, sufficient cause for such detention.
Explanation I. In this Article, “the appropriate Review Board” means,
(i) in the case of a person detained under a Federal law, a Board appointed by the Chief Justice of Supreme Court of Pakistan and consisting of a Chairman and two other persons, each of whom is or has been a Judge of the Supreme Court or a High Court; and
(ii) 
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-9`
- file: `raw/constitution.txt`, chunk_id: `constitution-10`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 38: `dev_scen_mcq_038` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> During an interrogation, police investigators subject an accused suspect to physical torture to compel a confession regarding an unsolved robbery. Which constitutional provision is explicitly violated by this act?

### Options

- **A.** Article 9 (Security of person)
- **B.** Article 14(2) (Inviolability of dignity of man / prohibition of torture for extracting evidence) ✅
- **C.** Article 10(2) (Detention safeguards)
- **D.** Article 13 (Protection against double jeopardy)

### Proposed Gold Answer

**B** — Article 14(2) (Inviolability of dignity of man / prohibition of torture for extracting evidence)

### Expected Citations

- `constitution-14` — [CONSTITUTION] Section/Article 14: Inviolability of dignity of man, etc

### Required Reasoning Points

- Article 14(2) specifically and explicitly mandates: No person shall be subjected to torture for the purpose of extracting evidence.

### Statutory Excerpts from Frozen Corpus

#### `constitution-14` — Inviolability of dignity of man, etc

```
Inviolability of dignity of man, etc. (1) The dignity of man and, subject to law, the privacy of home, shall be inviolable.
(2) No person shall be subjected to torture for the purpose of extracting evidence.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-14`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 39: `dev_scen_mcq_039` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> A government authority refuses to provide a citizen with certified copies of public procurement evaluation records, asserting unchecked executive discretion. The citizen invokes the Constitution. Which fundamental right directly secures access to such records?

### Options

- **A.** Article 19 (Freedom of speech)
- **B.** Article 19A (Right to information) ✅
- **C.** Article 24 (Protection of property rights)
- **D.** Article 18 (Freedom of trade)

### Proposed Gold Answer

**B** — Article 19A (Right to information)

### Expected Citations

- `constitution-19A` — [CONSTITUTION] Section/Article 19A: Right to information

### Required Reasoning Points

- Article 19A provides every citizen the right to have access to information in all matters of public importance.

### Statutory Excerpts from Frozen Corpus

#### `constitution-19A` — Right to information

```
Right to information. Every citizen shall have the right to have access to information in all matters of public importance subject to regulation and reasonable restrictions imposed by law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-19A`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 40: `dev_scen_mcq_040` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | MCQ (4 options) |
| **Answerable** | True |

### Question

> An armed gang of six persons storms a bank branch, threatens the cashier with handguns, and loots PKR 10,000,000 from the cash counter before escaping. Because six persons acted conjointly, which offence is committed under the Pakistan Penal Code?

### Options

- **A.** Extortion under Section 384 PPC
- **B.** Dacoity under Section 391/395 PPC ✅
- **C.** Theft under Section 379 PPC only
- **D.** Criminal breach of trust under Section 406 PPC

### Proposed Gold Answer

**B** — Dacoity under Section 391/395 PPC

### Expected Citations

- `ppc-391` — [PPC] Section/Article 391: Dacoity
- `ppc-395` — [PPC] Section/Article 395: Punishment for dacoity

### Required Reasoning Points

- When five or more persons conjointly commit robbery, the offence is dacoity under Section 391, punishable under Section 395 PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-391` — Dacoity

```
Dacoity. When five or more persons conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more every person so committing, attempting or aiding, is said to commit “dacoity”.
```

#### `ppc-395` — Punishment for dacoity

```
Punishment for dacoity. Whoever commits dacoity shall be punished with imprisonment for life, or with rigorous imprisonment for a term which shall not be less than four years nor more than ten years, and shall also be liable to fine.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-391`
- file: `raw/ppc.txt`, chunk_id: `ppc-395`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 41: `dev_scen_ft_041` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> A man falsely represents to an investor that he owns commercial real estate in Islamabad, showing forged title deeds, and thereby induces the investor to transfer PKR 15,000,000 into his personal account. Analyze the offence committed under the Pakistan Penal Code and cite the applicable provision and maximum penalty.

### Proposed Gold Answer

This act constitutes the offence of cheating and dishonestly inducing delivery of property under Section 420 of the Pakistan Penal Code. Section 420 prescribes imprisonment of either description for a term which may extend to seven years, and the offender shall also be liable to fine. [PPC Section 420]

### Expected Citations

- `ppc-420` — [PPC] Section/Article 420: Cheating and dishonestly inducing delivery of property

### Required Reasoning Points

- Identifies dishonest inducement and delivery of property
- Cites Section 420 PPC
- Identifies 7-year imprisonment and liability to fine

### Statutory Excerpts from Frozen Corpus

#### `ppc-420` — Cheating and dishonestly inducing delivery of property

```
Cheating and dishonestly inducing delivery of property. Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security, or anything which is signed or sealed, and which is capable of being converted into a valuable security, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-420`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 42: `dev_scen_ft_042` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> A political activist creates a website designed to cause panic among the public by threatening mass cyber-attacks on the federal electric power grid critical infrastructure unless certain prisoners are released. Under PECA 2016, what offence is committed, what section applies, and what is the maximum imprisonment?

### Proposed Gold Answer

Under PECA 2016, this act constitutes Cyber Terrorism under Section 10. Threatening attacks on critical infrastructure to advance political objectives or create public terror is punishable under Section 10 with imprisonment which may extend to fourteen years, or with fine up to fifty million rupees, or with both. [PECA Section 10]

### Expected Citations

- `peca-10` — [PECA] Section/Article 10: Cyber terrorism

### Required Reasoning Points

- Identifies threat to critical infrastructure
- Cites Section 10 PECA (Cyber Terrorism)
- Identifies 14 years imprisonment and/or 50 million rupees fine

### Statutory Excerpts from Frozen Corpus

#### `peca-10` — Cyber terrorism

```
Cyber terrorism.— Whoever commits or threatens to commit any of the offences under sections 6, 7, 8 or 9, where the commission or threat is with the intent to,—
(a) coerce, intimidate, create a sense of fear, panic or insecurity in the Government or the public or a section of the public or community or sect or create a sense of fear or insecurity in society; or
(b) advance inter-faith, sectarian or ethnic hatred; or
(c) advance the objectives of organizations or individuals or groups proscribed under the law, shall be punished with imprisonment of either description for a term which may extend to fourteen years or with fine which may extend to fifty million rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-10`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 43: `dev_scen_ft_043` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> A provincial education department restricts admissions to state-funded secondary schools exclusively to children whose families pay provincial property taxes, denying free schooling to poor children. Explain which constitutional fundamental right is violated and cite the exact article.

### Proposed Gold Answer

This policy violates Article 25A of the Constitution of Pakistan (Right to education). Article 25A mandates that the State shall provide free and compulsory education to all children aged five to sixteen years in such manner as determined by law, without discriminatory financial prerequisites. [Constitution Article 25A]

### Expected Citations

- `constitution-25A` — [CONSTITUTION] Section/Article 25A: Right to education

### Required Reasoning Points

- Identifies breach of State duty to provide free and compulsory education
- Cites Article 25A
- Identifies ages 5 to 16 years

### Statutory Excerpts from Frozen Corpus

#### `constitution-25A` — Right to education

```
Right to education. The State shall provide free and compulsory education to all children of the age of five to sixteen years in such manner as may be determined by law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-25A`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 44: `dev_scen_ft_044` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> A mob of seven villagers armed with sticks and axes enters an disputed agricultural field to forcibly harvest crops belonging to their neighbor, threatening to kill anyone who intervenes. Analyze this collective action under the Pakistan Penal Code: state the specific offence, cite the section defining the assembly, and cite the section prescribing the punishment.

### Proposed Gold Answer

This collective action constitutes the offence of being a member of an unlawful assembly under the Pakistan Penal Code. Section 141 PPC defines an unlawful assembly as an assembly of five or more persons whose common object is to enforce any right or supposed right by means of criminal force. Section 143 PPC prescribes the punishment, providing that whoever is a member of an unlawful assembly shall be punished with imprisonment of either description for a term which may extend to six months, or with fine, or with both. [PPC Section 141] [PPC Section 143]

### Expected Citations

- `ppc-141` — [PPC] Section/Article 141: Unlawful assembly
- `ppc-143` — [PPC] Section/Article 143: Punishment

### Required Reasoning Points

- Identifies the gathering as an unlawful assembly of five or more persons enforcing a supposed right by criminal force.
- Cites Section 141 PPC as the defining section.
- Cites Section 143 PPC as the penalizing section (imprisonment up to 6 months, or fine, or both).

### Statutory Excerpts from Frozen Corpus

#### `ppc-141` — Unlawful assembly

```
Unlawful assembly. An assembly of five or more persons is designated an “unlawful assembly,” if the common object of the persons composing that assembly is First. To overawe by criminal force, or show of criminal force, the Federal or any Provincial Government or Legislature, or any public servant in the exercise of the lawful power of such public servant ; or Second. To resist the execution of any law, or of any legal process ; or Third. To commit any mischief or criminal trespass, or other offence ; or Fourth. By means of criminal force, or show of criminal force, to any person to take or obtain possession of any property, or to deprive any person of the enjoyment of a right of way, or of the use of water or other incorporeal right of which he is in possession or enjoyment, or to enforce any right or supposed right ; or Fifth. By means of criminal force, or show of criminal force, to compel any person to do what he is not legally bound to do, or to omit to do what he is legally entitled to do.
Explanation. An assembly which was not unlawful when it assembled, may subsequently become an unlawful assembly.
```

#### `ppc-143` — Punishment

```
Punishment. Whoever is a member of an unlawful assembly, shall be punished with imprisonment of either description for a term which may extend to six months, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-141`
- file: `raw/ppc.txt`, chunk_id: `ppc-143`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 45: `dev_scen_ft_045` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Factual Legal Scenario |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> An employee of an IT firm copies confidential proprietary software code and client databases to an external USB drive without authorization and with dishonest intent. Identify the offence committed under PECA 2016, cite the provision, and state the statutory penalty.

### Proposed Gold Answer

This act constitutes the offence of unauthorized copying or transmission of data under Section 4 of PECA 2016. Section 4 provides that whoever with dishonest intention and without authorization copies or transmits data shall be punished with imprisonment for a term which may extend to six months, or with fine up to one hundred thousand rupees, or with both. [PECA Section 4]

### Expected Citations

- `peca-4` — [PECA] Section/Article 4: Unauthorized copying or transmission of data

### Required Reasoning Points

- Identifies unauthorized copying of data with dishonest intention
- Cites Section 4 PECA
- States penalty: up to 6 months imprisonment and/or 100,000 rupees fine

### Statutory Excerpts from Frozen Corpus

#### `peca-4` — Unauthorized copying or transmission of data

```
Unauthorized copying or transmission of data.— Whoever with dishonest intention and without authorization copies or otherwise transmits or causes to be transmitted any data shall be punished with imprisonment for a term which may extend to six months, or with fine which may extend to one hundred thousand rupees or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-4`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 46: `dev_mhop_ft_046` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> How does PECA 2016 interact with the Pakistan Penal Code when an electronic crime also constitutes an offence under the Penal Code? Cite the statutory bridge section in PECA.

### Proposed Gold Answer

Under Section 28 of PECA 2016, the provisions of the Pakistan Penal Code, 1860 (Act XLV of 1860) apply to offences provided in PECA to the extent that they are not inconsistent with anything provided in PECA. Thus, the PPC serves as a supplementary substantive penal framework unless expressly overridden by PECA special provisions. [PECA Section 28]

### Expected Citations

- `peca-28` — [PECA] Section/Article 28: Pakistan Penal Code, 1860 (Act XLV of 1860) to apply

### Required Reasoning Points

- Cites Section 28 PECA
- Explains that PPC applies to the extent not inconsistent with PECA

### Statutory Excerpts from Frozen Corpus

#### `peca-28` — Pakistan Penal Code, 1860 (Act XLV of 1860) to apply

```
Pakistan Penal Code, 1860 (Act XLV of 1860) to apply.— The provisions of the Pakistan Penal Code, 1860 (Act XLV of 1860), to the extent not inconsistent with anything provided in this Act, shall apply to the offences provided in this Act.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-28`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 47: `dev_mhop_ft_047` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Under the Constitution of Pakistan as amended by the 27th Amendment Act, 2025, which forum has exclusive original jurisdiction to resolve a dispute between the Federal Government and a Provincial Government regarding provincial autonomy? Cite the governing article.

### Proposed Gold Answer

Under Article 175E(1) of the Constitution (inserted by the 27th Amendment Act, 2025), the Federal Constitutional Court has original jurisdiction to the exclusion of every other court in any dispute between two or more Governments. Consequently, inter-governmental constitutional disputes fall exclusively under the Federal Constitutional Court rather than the Supreme Court or High Courts. [Constitution Article 175E]

### Expected Citations

- `constitution-175E` — [CONSTITUTION] Section/Article 175E: Original jurisdiction of Federal Constitutional Court

### Required Reasoning Points

- Identifies the Federal Constitutional Court as possessing exclusive original jurisdiction
- Cites Article 175E of the Constitution
- Distinguishes from Supreme Court jurisdiction under revised Chapter 1A

### Statutory Excerpts from Frozen Corpus

#### `constitution-175E` — Original jurisdiction of Federal Constitutional Court

```
Original jurisdiction of Federal Constitutional Court. (1) The Federal Constitutional Court shall, to the exclusion of every other court, have original jurisdiction in any dispute between any two or more Governments.
Explanation.- In this clause, “Governments” means the Federal Government and the Provincial Governments.
(2) In the exercise of the jurisdiction conferred on it by clause (1), the Federal Constitutional Court shall pronounce declaratory judgments only.
(3) Without prejudice to the provisions of Article 199, the Federal Constitutional Court shall, if it considers that a question of public importance with reference to the enforcement of any of the Fundamental Rights conferred by Chapter 1 of Part II is involved, have the power to make an order of the nature mentioned in the said Article:
Provided that, subject to the satisfaction of the Federal Constitutional Court, the jurisdiction under this clause shall only be exercised if an application is filed by a person in that Court.
(4) All petitions which fall under this Article and appeals or review applications against judgments rendered or orders passed under this Article, pending or filed before the Supreme Court or its Constitutional Benches, prior to commencement of the Constitution (Twenty-seventh Amendment) Act, 2025, shall forthwith stand transferred to the Federal Constitutional Court and shall only be heard and decided by the Federal Constitutional Court.
(5) The Federal Constitutional Court may, on its own motion or otherwise, if it considers that the case involves a substantial question of law as to the interpretation of the Constitution, call for the record of any case pending before any court and make such order in the case as it thinks fit.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-175E`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 48: `dev_mhop_ft_048` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> A Provincial Government files a constitutional writ petition before a Provincial High Court challenging a decision of the Federal Government regarding natural resource royalties. Can the High Court exercise jurisdiction under Article 199 of the Constitution of Pakistan in light of Article 175E? Synthesize both provisions.

### Proposed Gold Answer

No, the High Court cannot exercise jurisdiction. Under Article 199 of the Constitution, the High Court writ jurisdiction is subject to the Constitution and conditional on no other adequate remedy being provided by law. Under Article 175E(1) of the Constitution (inserted by the 27th Amendment Act, 2025), the Federal Constitutional Court has original jurisdiction to the exclusion of every other court in any dispute between two or more Governments (defined as the Federal Government and Provincial Governments). Because Article 175E explicitly excludes all other courts in inter-governmental disputes, the High Court Article 199 jurisdiction is constitutionally ousted in favor of the exclusive original jurisdiction of the Federal Constitutional Court. [Constitution Article 199] [Constitution Article 175E]

### Expected Citations

- `constitution-199` — [CONSTITUTION] Section/Article 199: Jurisdiction of High Court
- `constitution-175E` — [CONSTITUTION] Section/Article 175E: Original jurisdiction of Federal Constitutional Court

### Required Reasoning Points

- Analyzes Article 199(1) as being expressly subject to the Constitution.
- Analyzes Article 175E(1) granting exclusive original jurisdiction to the Federal Constitutional Court in inter-governmental disputes.
- Concludes that Article 175E ousts the High Court Article 199 writ jurisdiction in disputes between the Federal Government and a Provincial Government.

### Statutory Excerpts from Frozen Corpus

#### `constitution-199` — Jurisdiction of High Court

```
Jurisdiction of High Court. (1) Subject to the Constitution, a High Court may, if it is satisfied that no other adequate remedy is provided by law,
(a) on the application of any aggrieved party, make an order—
(i) directing a person performing, within the territorial jurisdiction of the Court, functions in connection with the affairs of the Federation, a Province or a local authority, to refrain from doing anything he is not permitted by law to do, or to do anything he is required by law to do; or
(ii) declaring that any act done or proceeding taken within the territorial jurisdiction of the Court by a person performing functions in connection with the affairs of the Federation, a Province or a local authority has been done or taken without lawful authority and is of no legal effect; or
(b) on the application of any person, make an order—
(i) directing that a person in custody within the territorial jurisdiction of the Court be brought before it so that the Court may satisfy itself that he is not being held in custody without lawful authority or in an unlawful manner; or
(ii) requiring a person within the territorial jurisdiction of the Court holding or purporting to hold a public office to show under what authority of law he claims to hold that office; or
(c) on the application of any aggrieved person, make an order giving such directions to any person or authority, including any Government exercising any power or performing any function in, or in relation to, any territory within the jurisdiction of that Court as may be appropriate for the enforcement of any of the Fundamental Rights conferred by Chapter 1 of Part II.
(1A) For removal of doubt, the High Court shall not make an order or give direction or make a declaration on its own or in the nature of suo motu exercise of jurisdiction beyond the contents of any application filed under clause (1).
(2) Subject to the Constitution, the right to move a High Court for the enforcement of any of the Fundamental Rights c
[... excerpt truncated for review package; full text in chunks.json ...]
```

#### `constitution-175E` — Original jurisdiction of Federal Constitutional Court

```
Original jurisdiction of Federal Constitutional Court. (1) The Federal Constitutional Court shall, to the exclusion of every other court, have original jurisdiction in any dispute between any two or more Governments.
Explanation.- In this clause, “Governments” means the Federal Government and the Provincial Governments.
(2) In the exercise of the jurisdiction conferred on it by clause (1), the Federal Constitutional Court shall pronounce declaratory judgments only.
(3) Without prejudice to the provisions of Article 199, the Federal Constitutional Court shall, if it considers that a question of public importance with reference to the enforcement of any of the Fundamental Rights conferred by Chapter 1 of Part II is involved, have the power to make an order of the nature mentioned in the said Article:
Provided that, subject to the satisfaction of the Federal Constitutional Court, the jurisdiction under this clause shall only be exercised if an application is filed by a person in that Court.
(4) All petitions which fall under this Article and appeals or review applications against judgments rendered or orders passed under this Article, pending or filed before the Supreme Court or its Constitutional Benches, prior to commencement of the Constitution (Twenty-seventh Amendment) Act, 2025, shall forthwith stand transferred to the Federal Constitutional Court and shall only be heard and decided by the Federal Constitutional Court.
(5) The Federal Constitutional Court may, on its own motion or otherwise, if it considers that the case involves a substantial question of law as to the interpretation of the Constitution, call for the record of any case pending before any court and make such order in the case as it thinks fit.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-199`
- file: `raw/constitution.txt`, chunk_id: `constitution-175E`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 49: `dev_mhop_ft_049` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> How do Articles 175A, 175B, and 175C of the Constitution of Pakistan conjointly govern the establishment, judicial strength, and appointment of Judges to the Federal Constitutional Court? Synthesize these provisions.

### Proposed Gold Answer

Under Article 175B, the Federal Constitutional Court is established consisting of a Chief Justice and as many other Judges as determined by Act of Parliament or fixed by the President. Under Article 175C(1), the Chief Justice and each Judge of the Federal Constitutional Court are appointed by the President in accordance with the procedure laid down in Article 175A. Under Article 175A, nominations are initiated and processed through the Judicial Commission of Pakistan before appointment. Together, these three provisions establish the court (Art. 175B), require presidential appointment under constitutional procedure (Art. 175C), and mandate nomination via the Judicial Commission (Art. 175A). [Constitution Article 175A] [Constitution Article 175B] [Constitution Article 175C]

### Expected Citations

- `constitution-175A` — [CONSTITUTION] Section/Article 175A: Appointment of Judges to the Federal Constitutional Court, the Supreme Court, High Courts and the Federal Shariat Court
- `constitution-175B` — [CONSTITUTION] Section/Article 175B: Constitution of Federal Constitutional Court
- `constitution-175C` — [CONSTITUTION] Section/Article 175C: Appointment of Federal Constitutional Court Judges

### Required Reasoning Points

- Synthesizes Article 175B (constitution and judicial strength of Federal Constitutional Court).
- Synthesizes Article 175C (presidential appointment governed by Article 175A).
- Synthesizes Article 175A (nomination process through the Judicial Commission of Pakistan).

### Statutory Excerpts from Frozen Corpus

#### `constitution-175A` — Appointment of Judges to the Federal Constitutional Court, the Supreme Court, High Courts and the Federal Shariat Court

```
Appointment of Judges to the Federal Constitutional Court, the Supreme Court, High Courts and the Federal Shariat Court. (1) There shall be a Judicial Commission of Pakistan, hereinafter in this Article referred to as the Commission, for appointment of Judges of the Federal Constitutional Court, the Supreme Court, High Courts and the Federal Shariat Court, and for performance evaluation of Judges of the High Courts, as hereinafter provided.
(2) For appointment of Judges of the Federal Constitutional Court and the Supreme Court, the Commission shall consist of
(i) Chief Justice of the Federal Constitutional Court;
(ii) Chief Justice of the Supreme Court;
(iii) one next most senior Judge each of the Federal Constitutional Court and the Supreme Court; Members
(iiia) a Judge of the Federal Constitutional Court or the Supreme Court jointly and nominated by the Chief Justice of the Federal Constitutional Court and the Chief Justice of the Supreme Court, for a period of two years; Member;
(iv) Federal Minister for Law and Justice; Member
(v) Attorney-General for Pakistan; Member
(vi) an advocate having not less than fifteen years of practice in the Supreme Court to be nominated by the Pakistan Bar Council for a term of two years; Member
(vii) two members from the Senate and two members from the National Assembly of whom two shall be from the Treasury Benches, one from each House, and two from the Opposition Benches, one from each House. The nomination from the Treasury Benches shall be made by the Leader of the House and from the Opposition Benches by the Leader of the Opposition:
Provided that during the time when the National Assembly stands dissolved, the remaining two members, for the purpose of this paragraph, shall be nominated from the Senate in the manner as aforesaid, for such period; Members
(viii) a woman or non Muslim or a technocrat, other than a member of Majlis- e-Shoora (Parliament), who is qualified to be member of the Majlis-e- Shoora (Parliament), to be 
[... excerpt truncated for review package; full text in chunks.json ...]
```

#### `constitution-175B` — Constitution of Federal Constitutional Court

```
Constitution of Federal Constitutional Court. (1) The Federal Constitutional Court shall consist of a Chief Justice to be known as the Chief Justice of the Federal Constitutional Court of Pakistan hereinafter referred to as the Chief Justice of the Federal Constitutional Court and as many other Judges as may be determined by Act of Majlis-e-Shoora (Parliament) or, until so determined, as may be fixed by the President:
Provided that the Federal Constitutional Court shall have equal number of Judges from each Province and at least one Judge from Islamabad High Court.
Explanation.- In no case the number of Judges from the Islamabad High Court shall exceed the numbers of Judges from a Province:
Provided further that nothing contained in the first proviso shall effect the functioning of the Federal Constitutional Court.
(2) The President may, by Order, make necessary provisions for the matters consequential or ancillary to the establishment and functioning of the Federal Constitutional Court.
```

#### `constitution-175C` — Appointment of Federal Constitutional Court Judges

```
Appointment of Federal Constitutional Court Judges.- (1) The Chief Justice of the Federal Constitutional Court and each of the other Judges thereof shall be appointed by the President in accordance with Article 175A.
(2) A person shall not be appointed as Judge of the Federal Constitutional Court unless he is a citizen of Pakistan and-
(a) is or has been a Judge of the Supreme Court; or
(b) has, for a period of not less than five years, been a Judge of a High Court; or
(c) has, for a period of not less than twenty years, been an advocate of a High Court and is an advocate of the Supreme Court.
(3) The inter se seniority of Judges appointed under this Article shall be reckoned from the date they enter upon the office and in case that date is same then on the basis of their age:
Provided that a Judge of the Supreme Court, who holds the said office on the commencement of the Constitution (Twenty-seventh Amendment) Act, 2025, shall retain his inter se seniority among Judges other than the Chief Justice of the Federal Constitutional Court.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-175A`
- file: `raw/constitution.txt`, chunk_id: `constitution-175B`
- file: `raw/constitution.txt`, chunk_id: `constitution-175C`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 50: `dev_mhop_ft_050`

| Field | Value |
|:---|:---|
| **Category** | Statutory Rule |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which offences under PECA 2016 are explicitly classified as cognizable and non-bailable under Section 43, in exception to the general rule that PECA offences are non-cognizable and bailable?

### Proposed Gold Answer

Under Section 43 of PECA 2016, the general rule is that all offences under the Act, and abetment thereof, are non-cognizable, bailable and compoundable (Section 43(1)), subject to specific statutory exceptions:
1. Under Section 43(2), offences under sections 10 (Cyber terrorism), 13 (Electronic forgery), 14 (Electronic fraud), 20 (Offences against dignity), 21 (Offences against modesty), 22 (Child pornography), 22A (Online grooming), 22B (Commercial sexual exploitation of children), 22C (Use of information system for kidnapping/trafficking of minor) and 26A (Punishment for false and fake information), as well as abetment thereof, are explicitly non-bailable, non-compoundable and cognizable by the investigation agency.
2. Under the Proviso to Section 43(1), offences under section 17 (Unauthorized issuance of SIM cards) are cognizable by the investigation agency on a written complaint by the Authority (Pakistan Telecommunication Authority). [PECA Section 43]

### Expected Citations

- `peca-43` — [PECA] Section/Article 43: Offences to be compoundable and non-cognizable

### Required Reasoning Points

- Identifies general rule under Section 43(1): PECA offences are non-cognizable, bailable, and compoundable.
- Identifies Section 43(2) exceptions as non-bailable, non-compoundable and cognizable: sections 10, 13, 14, 20, 21, 22, 22A, 22B, 22C, and 26A.
- Identifies Proviso to Section 43(1): section 17 offences are cognizable on written complaint by the Authority, without making it non-bailable.

### Statutory Excerpts from Frozen Corpus

#### `peca-43` — Offences to be compoundable and non-cognizable

```
Offences to be compoundable and non-cognizable.— (1) All offences under this Act, except the offences under sections 10, 13, 14, 20, 21, 22 and 26A and abetment thereof, shall be non-cognizable, bailable and compoundable:
Provided that offences under section 17 shall be cognizable by the investigation agency on a written complaint by the Authority.
(2) Offences under sections 10, 21 13, 14, 20, 22, 22A, 22B, 22C and 26A and abetment thereof shall be non-bailable, non-compoundable and cognizable by the investigation agency.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-43`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 51: `dev_mhop_ft_051` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> When does the offence of theft under Section 378 of the Pakistan Penal Code become the aggravated offence of robbery? Cite the statutory bridge section.

### Proposed Gold Answer

Under Section 390 of the Pakistan Penal Code, theft is robbery if, in order to the committing of the theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft, the offender, for that end, voluntarily causes or attempts to cause to any person death or hurt or wrongful restraint, or fear of instant death, instant hurt, or instant wrongful restraint. [PPC Section 390]

### Expected Citations

- `ppc-390` — [PPC] Section/Article 390: Robbery When theft is robbery When extortion is robbery

### Required Reasoning Points

- Cites Section 390 PPC
- Explains transformation of theft into robbery via causing or threatening instant death, hurt, or wrongful restraint

### Statutory Excerpts from Frozen Corpus

#### `ppc-390` — Robbery When theft is robbery When extortion is robbery

```
Robbery. In all robbery there is either theft or extortion. When theft is robbery. Theft is “robbery” if, in order to the committing of the theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft, the offender, for that end, voluntarily causes or attempts to cause to any person death or hurt or wrongful restraint, or fear of instant death or of instant hurt, or of instant wrongful restraint. When extortion is robbery. Extortion is “robbery” if the offender, at the time of committing the extortion, is in the presence of the person put in fear, and commits the extortion by putting that lSubs. by the Law Reforms Ordinance, 1972 (12 of 1972), s. 2 and Sch., for “transportation”. person in fear of instant death, of instant hurt, or of instant wrongful restraint to that person, or to some other person, and, by so putting in fear, induces the person so put in fear then and there to deliver up the thing extorted.
Explanation. The offender is said to be present if he is sufficiently near to put the other person in fear of instant death, of instant hurt, or of instant wrongful restraint.
Illustrations
(a) A holds Z down, and fraudulently takes Z’s money and jewels from Z’s clothes, without Z’s consent. Here A has committed theft, and, in order to the committing of that theft, has voluntarily caused wrongful restraint to Z. A has therefore committed robbery.
(b) A meets Z on the high-road, shows a pistol, and demands Z’s purse. Z, in consequence, surrenders his purse. Here A has extorted the purse from Z by putting him in fear of instant hurt, and being at the time of committing the extortion in his presence. A has therefore committed robbery.
(c) A meets Z and Z’s child on the high-road. A takes the child, and threatens to fling it down a precipice, unless Z deliver his purse. Z, in consequence, delivers his purse. Here A has extorted the purse from Z, by causing Z to be in fear of instant hurt to the child who is ther
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-390`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 52: `dev_mhop_ft_052` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What legal effect follows under Article 203D of the Constitution when the Federal Shariat Court declares a statutory provision to be repugnant to the Injunctions of Islam and that decision takes effect?

### Proposed Gold Answer

Under Article 203D(3) of the Constitution, if any law or provision is held by the Federal Shariat Court to be repugnant to the Injunctions of Islam, the President or Governor shall take steps to amend the law to bring it into conformity with Islam, and such law or provision ceases to have effect on the day on which the decision of the Court takes effect. [Constitution Article 203D]

### Expected Citations

- `constitution-203D` — [CONSTITUTION] Section/Article 203D: Powers, jurisdiction and functions of the Court

### Required Reasoning Points

- Cites Article 203D(3) of the Constitution
- Identifies duty of executive to amend law
- States that law ceases to have effect upon date decision takes effect

### Statutory Excerpts from Frozen Corpus

#### `constitution-203D` — Powers, jurisdiction and functions of the Court

```
Powers, jurisdiction and functions of the Court. (1) The Court may, either of its own motion or on the petition of a citizen of Pakistan or the Federal Government or a Provincial Government, examine and decide the question whether or not any law or provision of law is repugnant to the Injunctions of Islam, as laid down in the Holy Quran and the Sunnah of the Holy Prophet, hereinafter referred to as the Injunctions of Islam.
(1A) Where the Court takes up the examination of any law or provision of law under clause
(1) and such law or provision of law appears to it to be repugnant to the Injunctions of Islam, the Court shall cause to be given to the Federal Government in the case of a law with respect to a matter in the Federal Legislative List or to the Provincial Government in the case of a law with respect to a matter not enumerated in the Federal Legislative List, a notice specifying the particular provisions that appear to it to be so repugnant, and afford to such Government adequate opportunity to have its point of view placed before the Court.
(2) If the Court decides that any law or provision of law is repugnant to the Injunctions of Islam, it shall set out in its decision :
(a) the reasons for its holding that opinion; and
(b) the extent to which such law or provision is so repugnant; and specify the day on which the decision shall take effect :
Provided that no such decision shall be deemed to take effect before the expiration of the period within which an appeal therefrom may be preferred to the Supreme Court or, where an appeal has been so preferred, before the disposal of such appeal :
Provided further that appeal against decision given after the commencement of the Constitution (Twenty-sixth Amendment) Act, 2024 (XXVI of 2024) shall be disposed of within twelve months whereafter the decision shall take effect unless suspended by the Supreme Court.
(3) If any law or provision of law is held by the Court to be repugnant to the Injunctions of Islam,
(a) the 
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-203D`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 53: `dev_mhop_ft_053` ⚠️ **EXPERT REVIEW REQUIRED**

| Field | Value |
|:---|:---|
| **Category** | Complex Multi-Hop |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> How does Article 19 of the Constitution of Pakistan qualify the fundamental right to freedom of speech and expression regarding state security and morality?

### Proposed Gold Answer

Under Article 19 of the Constitution, freedom of speech, expression, and press is expressly "subject to any reasonable restrictions imposed by law in the interest of the glory of Islam or the integrity, security or defence of Pakistan or any part thereof, friendly relations with foreign States, public order, decency or morality, or in relation to contempt of court, commission of or incitement to an offence". [Constitution Article 19]

### Expected Citations

- `constitution-19` — [CONSTITUTION] Section/Article 19: Freedom of speech, etc

### Required Reasoning Points

- Cites Article 19 of the Constitution
- Identifies reasonable restrictions imposed by law
- Lists interests: glory of Islam, security/defence, public order, morality

### Statutory Excerpts from Frozen Corpus

#### `constitution-19` — Freedom of speech, etc

```
Freedom of speech, etc. Every citizen shall have the right to freedom of speech and expression, and there shall be freedom of the press, subject to any reasonable restrictions imposed by law in the interest of the glory of Islam or the integrity, security or defence of Pakistan or any part thereof, friendly relations with foreign States, public order, decency or morality, or in relation to contempt of court, commission of or incitement to an offence.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-19`

### Expert Review Notes

> This question applies statutory provisions to a hypothetical factual scenario
> or requires synthesis across multiple provisions. The proposed answer has been
> verified against the literal statutory text, but the legal characterisation
> requires confirmation by a qualified Pakistani legal advocate.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 54: `dev_refusal_054`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Unsupported Provision (legal claim has no basis in corpus) |

### Question

> What offence and punishment are provided under Section 999 of the Pakistan Penal Code?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Section 999 does not exist in the Pakistan Penal Code (Code ends at Section 511).

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 55: `dev_refusal_055`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | peca |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Missing Context (information exists in corpus but absent from supplied excerpt) |

### Question

> CONTEXT:
[PECA Section 21 - Offences against modesty of a natural person and minor]
(1) Whoever intentionally and publicly exhibits or displays or transmits any information which superimposes a photograph of the face of a natural person over any sexually explicit image... shall be punished with imprisonment for a term which may extend to five years or with fine.

QUESTION:
Based only on the provided context, what specific penalty is prescribed if the offence against modesty is committed with respect to a minor?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- The question asks about subsection (2) regarding offences with respect to a minor.
- The provided context excerpt contains only subsection (1) and omits subsection (2).
- Under strict grounding rules, the model must refuse because the provided context lacks the answer.

### Supplied Context Excerpt (embedded in question)

The context excerpt is embedded in the question text above. The reviewer should
verify that the requested information is **genuinely absent** from this excerpt,
even though the full provision exists elsewhere in the corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 56: `dev_refusal_056`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | constitution |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Unsupported Provision (legal claim has no basis in corpus) |

### Question

> Explain the fundamental rights guaranteed under Article 400 of the Constitution of Pakistan.

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Article 400 does not exist in the Constitution of Pakistan (Constitution ends at Article 280).

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 57: `dev_refusal_057`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Missing Context (information exists in corpus but absent from supplied excerpt) |

### Question

> CONTEXT:
[PPC Section 302 - Punishment of qatl-i-amd]
Whoever commits qatl-e-amd shall, subject to the provisions of this Chapter be (a) punished with death as qisas; (b) punished with death or imprisonment for life as ta'zir...

QUESTION:
Based only on the provided context, what is the maximum imprisonment term prescribed under clause (c) of Section 302 for qatl-i-amd when not punishable under clause (a) or (b)?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- The question asks about clause (c) of Section 302 PPC (twenty-five years imprisonment where principle of fasad-fil-arz applies).
- The provided context excerpt truncates Section 302 after clause (b) and omits clause (c).
- Under strict grounding rules, the model must refuse because the provided context does not contain clause (c).

### Supplied Context Excerpt (embedded in question)

The context excerpt is embedded in the question text above. The reviewer should
verify that the requested information is **genuinely absent** from this excerpt,
even though the full provision exists elsewhere in the corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 58: `dev_refusal_058`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | peca |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Unsupported Provision (legal claim has no basis in corpus) |

### Question

> What powers does Section 95 of the Prevention of Electronic Crimes Act 2016 grant to investigators?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Section 95 does not exist in PECA 2016 (PECA concludes at Section 56).

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 59: `dev_refusal_059`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | other_law |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Out-of-Corpus Law (statute excluded from frozen experimental corpus) |

### Question

> What is the time limit for filing a statutory criminal appeal under Section 410 of the Code of Criminal Procedure (CrPC), 1898?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- CrPC is outside the project's frozen statutory corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 60: `dev_refusal_060`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | other_law |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Out-of-Corpus Law (statute excluded from frozen experimental corpus) |

### Question

> What rules govern the admissibility of electronic evidentiary documents under Article 164 of the Qanun-e-Shahadat Order, 1984?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Qanun-e-Shahadat Order 1984 is outside the project's statutory corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 61: `dev_refusal_061`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Missing Context (information exists in corpus but absent from supplied excerpt) |

### Question

> CONTEXT:
[Constitution Article 199 - Jurisdiction of High Court]
(1) Subject to the Constitution, a High Court may, if it is satisfied that no other adequate remedy is provided by law, (a) on the application of any aggrieved party, make an order directing a person performing functions in connection with the affairs of the Federation... to refrain from doing that which he is not permitted by law to do...

QUESTION:
Based only on the provided context, what limitation does clause (4A) of Article 199 place on the duration of an interim stay order involving state revenues?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- The question asks about the six-month time limit on interim revenue orders under clause (4A) of Article 199.
- The provided context excerpt includes only clause (1)(a) and omits clause (4A).
- Under strict grounding rules, the model must refuse because the answer is missing from the provided text.

### Supplied Context Excerpt (embedded in question)

The context excerpt is embedded in the question text above. The reviewer should
verify that the requested information is **genuinely absent** from this excerpt,
even though the full provision exists elsewhere in the corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 62: `dev_refusal_062`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | other_law |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Out-of-Corpus Law (statute excluded from frozen experimental corpus) |

### Question

> What specific acts constitute terrorism under Section 6 of the Anti-Terrorism Act, 1997, and what punishment is prescribed under Section 7 of the Act?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- The question asks about Section 6 and Section 7 of the Anti-Terrorism Act, 1997 (Act No. XXVII of 1997).
- The Anti-Terrorism Act, 1997 is a Pakistani federal statute that is excluded from the project's frozen baseline corpus (which comprises only the Constitution, PPC, and PECA).
- Under strict out-of-corpus boundary rules, the model must refuse to answer substantive statutory questions from excluded domestic legislation.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 63: `dev_refusal_063`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | foreign_law |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Foreign Jurisdiction (non-Pakistani law) |

### Question

> What is the statutory penalty for theft under Section 378 of the Indian Bharatiya Nyaya Sanhita (BNS)?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Indian Bharatiya Nyaya Sanhita is a foreign penal code and outside the statutory corpus.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 64: `dev_refusal_064`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | foreign_law |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Foreign Jurisdiction (non-Pakistani law) |

### Question

> What protections are established under the First Amendment of the United States Constitution?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- US Constitution is foreign jurisdiction.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 65: `dev_refusal_065`

| Field | Value |
|:---|:---|
| **Category** | Negative / Refusal |
| **Law** | non_legal |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | False |
| **Refusal Type** | Non-Legal Query |

### Question

> What are the recommended medical clinical therapies for treating adult type 2 diabetes mellitus?

### Proposed Gold Answer

I don't know - this is not in the provided text.

### Expected Citations

- None (refusal question — no citation expected)

### Required Reasoning Points

- Non-legal inquiry.

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 66: `dev_ret_066`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What statutory provision penalizes dishonestly signing and delivering a bank cheque that bounces due to lack of funds?

### Proposed Gold Answer

Section 489-F of the Pakistan Penal Code. [PPC Section 489-F]

### Expected Citations

- `ppc-489F` — [PPC] Section/Article 489-F: Dishonestly issuing a cheque

### Required Reasoning Points

- Retrieves Section 489-F PPC without verbatim heading matching.

### Statutory Excerpts from Frozen Corpus

#### `ppc-489F` — Dishonestly issuing a cheque

```
Dishonestly issuing a cheque. Whoever dishonestly issues a cheque towards re-payment of a loan or fulfillment of an obligation which is dishonoured on presentation, shall be punishable with imprisonment which may extend to three years, or with fine, or with both, unless he can establish, for which the burden of proof shall rest on him, that he had made arrangements with his bank to ensure that the cheque would be honoured and that the bank was at fault in not honouring the cheque.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-489F`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 67: `dev_ret_067`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Where does Pakistani criminal law define the collective offence of five or more armed persons looting property together?

### Proposed Gold Answer

Section 391 of the Pakistan Penal Code. [PPC Section 391]

### Expected Citations

- `ppc-391` — [PPC] Section/Article 391: Dacoity

### Required Reasoning Points

- Retrieves Section 391 PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-391` — Dacoity

```
Dacoity. When five or more persons conjointly commit or attempt to commit a robbery, or where the whole number of persons conjointly committing or attempting to commit a robbery, and persons present and aiding such commission or attempt, amount to five or more every person so committing, attempting or aiding, is said to commit “dacoity”.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-391`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 68: `dev_ret_068`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | easy |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What section provides the general legal penalty for taking someone's movable belongings dishonestly without their consent?

### Proposed Gold Answer

Section 379 of the Pakistan Penal Code. [PPC Section 379]

### Expected Citations

- `ppc-379` — [PPC] Section/Article 379: Punishment for theft

### Required Reasoning Points

- Retrieves Section 379 PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-379` — Punishment for theft

```
Punishment for theft. Whoever commits theft shall be punished with imprisonment of either description for a term which may extend to three years, or with fine or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-379`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 69: `dev_ret_069`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which statutory section punishes a fiduciary or agent who dishonestly misappropriates funds entrusted to their custody?

### Proposed Gold Answer

Section 406 of the Pakistan Penal Code. [PPC Section 406]

### Expected Citations

- `ppc-406` — [PPC] Section/Article 406: Punishment for criminal breach of trust

### Required Reasoning Points

- Retrieves Section 406 PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-406` — Punishment for criminal breach of trust

```
Punishment for criminal breach of trust. Whoever commits criminal breach of trust shall be punished with imprisonment of either description for a term which may extend to seven years, or with fine, or with both.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-406`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 70: `dev_ret_070`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What provision governs the severe capital offence of abducting a person to extort ransom or valuable property?

### Proposed Gold Answer

Section 365-A of the Pakistan Penal Code. [PPC Section 365-A]

### Expected Citations

- `ppc-365A` — [PPC] Section/Article 365-A: Kidnapping or abducting for extorting property, valuable security, etc

### Required Reasoning Points

- Retrieves Section 365-A PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-365A` — Kidnapping or abducting for extorting property, valuable security, etc

```
Kidnapping or abducting for extorting property, valuable security, etc. Whoever kidnaps or abducts any person for the purpose of extorting from the person kidnapped or abducted, or from any person interested in the person kidnapped or abducted, any property, whether movable or immovable, or valuable security, or to compel any person to comply with any other demand, whether in cash or otherwise, for obtaining release of the person kidnapped or abducted, shall be punished with death or imprisonment for life and shall also be liable to forfeiture of property.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-365A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 71: `dev_ret_071`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | ppc |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which section of the penal code defines what constitutes an unlawful gathering of citizens with a common prohibited goal?

### Proposed Gold Answer

Section 141 of the Pakistan Penal Code. [PPC Section 141]

### Expected Citations

- `ppc-141` — [PPC] Section/Article 141: Unlawful assembly

### Required Reasoning Points

- Retrieves Section 141 PPC.

### Statutory Excerpts from Frozen Corpus

#### `ppc-141` — Unlawful assembly

```
Unlawful assembly. An assembly of five or more persons is designated an “unlawful assembly,” if the common object of the persons composing that assembly is First. To overawe by criminal force, or show of criminal force, the Federal or any Provincial Government or Legislature, or any public servant in the exercise of the lawful power of such public servant ; or Second. To resist the execution of any law, or of any legal process ; or Third. To commit any mischief or criminal trespass, or other offence ; or Fourth. By means of criminal force, or show of criminal force, to any person to take or obtain possession of any property, or to deprive any person of the enjoyment of a right of way, or of the use of water or other incorporeal right of which he is in possession or enjoyment, or to enforce any right or supposed right ; or Fifth. By means of criminal force, or show of criminal force, to compel any person to do what he is not legally bound to do, or to omit to do what he is legally entitled to do.
Explanation. An assembly which was not unlawful when it assembled, may subsequently become an unlawful assembly.
```

### Source References

- file: `raw/ppc.txt`, chunk_id: `ppc-141`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 72: `dev_ret_072`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Under cybercrime legislation, which provision penalizes spreading online material designed to incite religious hatred or sectarian strife?

### Proposed Gold Answer

Section 11 of the Prevention of Electronic Crimes Act 2016. [PECA Section 11]

### Expected Citations

- `peca-11` — [PECA] Section/Article 11: Hate speech

### Required Reasoning Points

- Retrieves Section 11 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-11` — Hate speech

```
Hate speech.— Whoever prepares or disseminates information, through any information system or device, that advances or is likely to advance interfaith, sectarian or racial hatred, shall be punished with imprisonment for a term which may extend to seven years or with fine or with both.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-11`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 73: `dev_ret_073`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What section of electronic crime law penalizes distributing sexually morphed or explicit imagery of an individual to violate personal dignity?

### Proposed Gold Answer

Section 21 of the Prevention of Electronic Crimes Act 2016. [PECA Section 21]

### Expected Citations

- `peca-21` — [PECA] Section/Article 21: Offences against modesty of a natural person and minor

### Required Reasoning Points

- Retrieves Section 21 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-21` — Offences against modesty of a natural person and minor

```
Offences against modesty of a natural person and minor.—(1) Whoever intentionally and publicly exhibits or displays or transmits any information which,—
(a) superimposes a photograph of the face of a natural person over any sexually explicit image or video; or
(b) includes a photograph or a video of a natural person in sexually explicit conduct; or
(c) intimidates a natural person with any sexual act, or any sexually explicit image or video of a natural person; or
(d) cultivates, entices or induces a natural person to engage in a sexually explicit act, through an information system to harm a natural person or his reputation, or to take revenge, or to create hatred or to blackmail, shall be punished with imprisonment for a term which may extend to five years or with fine which may extend to five million rupees or with both.
(2) Whoever commits an offence under sub-section (1) with respect to a minor shall be punished with imprisonment for a term which may extend to seven years and with fine which may extend to five million rupees:
Provided that in case of a person who has been previously convicted of an offence under sub- section (1) with respect to a minor shall be punished with imprisonment for a term of ten years and with fine.
(3) Any aggrieved person or his guardian, where such person is a minor, may apply to the Authority for removal, destruction of or blocking access to such information referred to in sub-section
(1) and the Authority, on receipt of such application, shall forthwith pass such orders as deemed reasonable in the circumstances including an order for removal, destruction, preventing transmission of or blocking access to such information and the Authority may also direct any of its licensees to secure such information including traffic data.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-21`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 74: `dev_ret_074`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | peca |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which statutory provision establishes criminal liability for persistently harassing, monitoring, or intimidating someone across social networks?

### Proposed Gold Answer

Section 24 of the Prevention of Electronic Crimes Act 2016. [PECA Section 24]

### Expected Citations

- `peca-24` — [PECA] Section/Article 24: Cyber stalking

### Required Reasoning Points

- Retrieves Section 24 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-24` — Cyber stalking

```
Cyber stalking.— (1) A person commits the offence of cyber stalking who, with the intent to coerce or intimidate or harass any person, uses information system, information system network, the Internet, website, electronic mail or any other similar means of communication to—
(a) follow a person or contacts or attempts to contact such person to foster personal interaction repeatedly despite a clear indication of disinterest by such person;
(b) monitor the use by a person of the internet, electronic mail, text message or any other form of electronic communication;
(c) watch or spy upon a person in a manner that results in fear of violence or serious alarm or distress, in the mind of such person; or
(d) take a photograph or make a video of any person and displays or distributes it without his consent in a manner that harms a person.
(2) Whoever commits the offence specified in sub-section (1) shall be punished with imprisonment for a term which may extend to three years or with fine which may extend to one million rupees or with both:
Provided that if victim of the cyber stalking under sub-section (1) is a minor the punishment may extend to five years or with fine which may extend to ten million rupees or with both.
(3) Any aggrieved person or his guardian, where such person is a minor, may apply to the Authority for removal, destruction of or blocking access to such information referred to in sub-section
(1) and the Authority, on receipt of such application, shall forthwith pass such orders as deemed reasonable in the circumstances including an order for removal, destruction, preventing transmission of or blocking access to such information and the Authority may also direct any of its licensees to secure such information including traffic data.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-24`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 75: `dev_ret_075`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | peca |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What clause in electronic crime law establishes that provisions of the Pakistan Penal Code remain applicable alongside cyber offences?

### Proposed Gold Answer

Section 28 of the Prevention of Electronic Crimes Act 2016. [PECA Section 28]

### Expected Citations

- `peca-28` — [PECA] Section/Article 28: Pakistan Penal Code, 1860 (Act XLV of 1860) to apply

### Required Reasoning Points

- Retrieves Section 28 PECA.

### Statutory Excerpts from Frozen Corpus

#### `peca-28` — Pakistan Penal Code, 1860 (Act XLV of 1860) to apply

```
Pakistan Penal Code, 1860 (Act XLV of 1860) to apply.— The provisions of the Pakistan Penal Code, 1860 (Act XLV of 1860), to the extent not inconsistent with anything provided in this Act, shall apply to the offences provided in this Act.
```

### Source References

- file: `raw/peca.txt`, chunk_id: `peca-28`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 76: `dev_ret_076`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Where in the Constitution is the State mandated to provide compulsory educational schooling to young children without tuition fees?

### Proposed Gold Answer

Article 25A of the Constitution of Pakistan. [Constitution Article 25A]

### Expected Citations

- `constitution-25A` — [CONSTITUTION] Section/Article 25A: Right to education

### Required Reasoning Points

- Retrieves Article 25A of the Constitution.

### Statutory Excerpts from Frozen Corpus

#### `constitution-25A` — Right to education

```
Right to education. The State shall provide free and compulsory education to all children of the age of five to sixteen years in such manner as may be determined by law.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-25A`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 77: `dev_ret_077`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which constitutional provision creates the Federal Constitutional Court and defines the office of its Chief Justice?

### Proposed Gold Answer

Article 175B of the Constitution of Pakistan. [Constitution Article 175B]

### Expected Citations

- `constitution-175B` — [CONSTITUTION] Section/Article 175B: Constitution of Federal Constitutional Court

### Required Reasoning Points

- Retrieves Article 175B of the Constitution.

### Statutory Excerpts from Frozen Corpus

#### `constitution-175B` — Constitution of Federal Constitutional Court

```
Constitution of Federal Constitutional Court. (1) The Federal Constitutional Court shall consist of a Chief Justice to be known as the Chief Justice of the Federal Constitutional Court of Pakistan hereinafter referred to as the Chief Justice of the Federal Constitutional Court and as many other Judges as may be determined by Act of Majlis-e-Shoora (Parliament) or, until so determined, as may be fixed by the President:
Provided that the Federal Constitutional Court shall have equal number of Judges from each Province and at least one Judge from Islamabad High Court.
Explanation.- In no case the number of Judges from the Islamabad High Court shall exceed the numbers of Judges from a Province:
Provided further that nothing contained in the first proviso shall effect the functioning of the Federal Constitutional Court.
(2) The President may, by Order, make necessary provisions for the matters consequential or ancillary to the establishment and functioning of the Federal Constitutional Court.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-175B`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 78: `dev_ret_078`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> What constitutional article vests the Federal Shariat Court with authority to strike down statutory legislation found repugnant to Islamic injunctions?

### Proposed Gold Answer

Article 203D of the Constitution of Pakistan. [Constitution Article 203D]

### Expected Citations

- `constitution-203D` — [CONSTITUTION] Section/Article 203D: Powers, jurisdiction and functions of the Court

### Required Reasoning Points

- Retrieves Article 203D of the Constitution.

### Statutory Excerpts from Frozen Corpus

#### `constitution-203D` — Powers, jurisdiction and functions of the Court

```
Powers, jurisdiction and functions of the Court. (1) The Court may, either of its own motion or on the petition of a citizen of Pakistan or the Federal Government or a Provincial Government, examine and decide the question whether or not any law or provision of law is repugnant to the Injunctions of Islam, as laid down in the Holy Quran and the Sunnah of the Holy Prophet, hereinafter referred to as the Injunctions of Islam.
(1A) Where the Court takes up the examination of any law or provision of law under clause
(1) and such law or provision of law appears to it to be repugnant to the Injunctions of Islam, the Court shall cause to be given to the Federal Government in the case of a law with respect to a matter in the Federal Legislative List or to the Provincial Government in the case of a law with respect to a matter not enumerated in the Federal Legislative List, a notice specifying the particular provisions that appear to it to be so repugnant, and afford to such Government adequate opportunity to have its point of view placed before the Court.
(2) If the Court decides that any law or provision of law is repugnant to the Injunctions of Islam, it shall set out in its decision :
(a) the reasons for its holding that opinion; and
(b) the extent to which such law or provision is so repugnant; and specify the day on which the decision shall take effect :
Provided that no such decision shall be deemed to take effect before the expiration of the period within which an appeal therefrom may be preferred to the Supreme Court or, where an appeal has been so preferred, before the disposal of such appeal :
Provided further that appeal against decision given after the commencement of the Constitution (Twenty-sixth Amendment) Act, 2024 (XXVI of 2024) shall be disposed of within twelve months whereafter the decision shall take effect unless suspended by the Supreme Court.
(3) If any law or provision of law is held by the Court to be repugnant to the Injunctions of Islam,
(a) the 
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-203D`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 79: `dev_ret_079`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | constitution |
| **Difficulty** | medium |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Where does the Constitution explicitly protect individuals against being subjected to torture to obtain confessions during investigations?

### Proposed Gold Answer

Article 14(2) of the Constitution of Pakistan. [Constitution Article 14]

### Expected Citations

- `constitution-14` — [CONSTITUTION] Section/Article 14: Inviolability of dignity of man, etc

### Required Reasoning Points

- Retrieves Article 14 of the Constitution.

### Statutory Excerpts from Frozen Corpus

#### `constitution-14` — Inviolability of dignity of man, etc

```
Inviolability of dignity of man, etc. (1) The dignity of man and, subject to law, the privacy of home, shall be inviolable.
(2) No person shall be subjected to torture for the purpose of extracting evidence.
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-14`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Question 80: `dev_ret_080`

| Field | Value |
|:---|:---|
| **Category** | Retrieval |
| **Law** | constitution |
| **Difficulty** | hard |
| **Format** | Free-text |
| **Answerable** | True |

### Question

> Which article establishes the extraordinary judicial review and writ jurisdiction of Provincial High Courts when no other adequate remedy exists?

### Proposed Gold Answer

Article 199 of the Constitution of Pakistan. [Constitution Article 199]

### Expected Citations

- `constitution-199` — [CONSTITUTION] Section/Article 199: Jurisdiction of High Court

### Required Reasoning Points

- Retrieves Article 199 of the Constitution.

### Statutory Excerpts from Frozen Corpus

#### `constitution-199` — Jurisdiction of High Court

```
Jurisdiction of High Court. (1) Subject to the Constitution, a High Court may, if it is satisfied that no other adequate remedy is provided by law,
(a) on the application of any aggrieved party, make an order—
(i) directing a person performing, within the territorial jurisdiction of the Court, functions in connection with the affairs of the Federation, a Province or a local authority, to refrain from doing anything he is not permitted by law to do, or to do anything he is required by law to do; or
(ii) declaring that any act done or proceeding taken within the territorial jurisdiction of the Court by a person performing functions in connection with the affairs of the Federation, a Province or a local authority has been done or taken without lawful authority and is of no legal effect; or
(b) on the application of any person, make an order—
(i) directing that a person in custody within the territorial jurisdiction of the Court be brought before it so that the Court may satisfy itself that he is not being held in custody without lawful authority or in an unlawful manner; or
(ii) requiring a person within the territorial jurisdiction of the Court holding or purporting to hold a public office to show under what authority of law he claims to hold that office; or
(c) on the application of any aggrieved person, make an order giving such directions to any person or authority, including any Government exercising any power or performing any function in, or in relation to, any territory within the jurisdiction of that Court as may be appropriate for the enforcement of any of the Fundamental Rights conferred by Chapter 1 of Part II.
(1A) For removal of doubt, the High Court shall not make an order or give direction or make a declaration on its own or in the nature of suo motu exercise of jurisdiction beyond the contents of any application filed under clause (1).
(2) Subject to the Constitution, the right to move a High Court for the enforcement of any of the Fundamental Rights c
[... excerpt truncated for review package; full text in chunks.json ...]
```

### Source References

- file: `raw/constitution.txt`, chunk_id: `constitution-199`

### Reviewer Decision

| Field | Response |
|:---|:---|
| **Decision** | ☐ Approved / ☐ Correction Required / ☐ Disputed |
| **Reviewer Name** | |
| **Date** | |
| **Comments / Proposed Corrections** | |

---

## Appendix A: Review Summary Table

| # | ID | Category | Law | Format | Expert Review | Decision |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | `dev_rule_ppc_001` | Statutory Rule | ppc | MCQ | No | ☐ |
| 2 | `dev_rule_ppc_002` | Statutory Rule | ppc | MCQ | No | ☐ |
| 3 | `dev_rule_ppc_003` | Statutory Rule | ppc | MCQ | No | ☐ |
| 4 | `dev_rule_ppc_004` | Statutory Rule | ppc | MCQ | No | ☐ |
| 5 | `dev_rule_ppc_005` | Statutory Rule | ppc | MCQ | No | ☐ |
| 6 | `dev_rule_ppc_006` | Statutory Rule | ppc | MCQ | No | ☐ |
| 7 | `dev_rule_ppc_007` | Statutory Rule | ppc | MCQ | No | ☐ |
| 8 | `dev_rule_ppc_008` | Statutory Rule | ppc | MCQ | No | ☐ |
| 9 | `dev_rule_ppc_009` | Statutory Rule | ppc | MCQ | No | ☐ |
| 10 | `dev_rule_ppc_010` | Statutory Rule | ppc | MCQ | No | ☐ |
| 11 | `dev_rule_ppc_011` | Statutory Rule | ppc | MCQ | No | ☐ |
| 12 | `dev_rule_ppc_012` | Statutory Rule | ppc | MCQ | No | ☐ |
| 13 | `dev_rule_ppc_013` | Statutory Rule | ppc | MCQ | No | ☐ |
| 14 | `dev_rule_ppc_014` | Statutory Rule | ppc | MCQ | No | ☐ |
| 15 | `dev_rule_const_015` | Statutory Rule | constitution | MCQ | No | ☐ |
| 16 | `dev_rule_const_016` | Statutory Rule | constitution | MCQ | No | ☐ |
| 17 | `dev_rule_const_017` | Statutory Rule | constitution | MCQ | No | ☐ |
| 18 | `dev_rule_const_018` | Statutory Rule | constitution | MCQ | No | ☐ |
| 19 | `dev_rule_const_019` | Statutory Rule | constitution | MCQ | No | ☐ |
| 20 | `dev_rule_const_020` | Statutory Rule | constitution | MCQ | No | ☐ |
| 21 | `dev_rule_const_021` | Statutory Rule | constitution | MCQ | No | ☐ |
| 22 | `dev_rule_const_022` | Statutory Rule | constitution | MCQ | No | ☐ |
| 23 | `dev_rule_const_023` | Statutory Rule | constitution | MCQ | No | ☐ |
| 24 | `dev_rule_const_024` | Statutory Rule | constitution | MCQ | No | ☐ |
| 25 | `dev_rule_peca_025` | Statutory Rule | peca | MCQ | No | ☐ |
| 26 | `dev_rule_peca_026` | Statutory Rule | peca | MCQ | No | ☐ |
| 27 | `dev_rule_peca_027` | Statutory Rule | peca | MCQ | No | ☐ |
| 28 | `dev_rule_peca_028` | Statutory Rule | peca | MCQ | No | ☐ |
| 29 | `dev_rule_peca_029` | Statutory Rule | peca | MCQ | No | ☐ |
| 30 | `dev_rule_peca_030` | Statutory Rule | peca | MCQ | No | ☐ |
| 31 | `dev_scen_mcq_031` | Factual Legal Scenario | ppc | MCQ | ⚠️ Yes | ☐ |
| 32 | `dev_scen_mcq_032` | Factual Legal Scenario | ppc | MCQ | ⚠️ Yes | ☐ |
| 33 | `dev_scen_mcq_033` | Factual Legal Scenario | ppc | MCQ | ⚠️ Yes | ☐ |
| 34 | `dev_scen_mcq_034` | Factual Legal Scenario | peca | MCQ | ⚠️ Yes | ☐ |
| 35 | `dev_scen_mcq_035` | Factual Legal Scenario | peca | MCQ | ⚠️ Yes | ☐ |
| 36 | `dev_scen_mcq_036` | Factual Legal Scenario | peca | MCQ | ⚠️ Yes | ☐ |
| 37 | `dev_scen_mcq_037` | Factual Legal Scenario | constitution | MCQ | ⚠️ Yes | ☐ |
| 38 | `dev_scen_mcq_038` | Factual Legal Scenario | constitution | MCQ | ⚠️ Yes | ☐ |
| 39 | `dev_scen_mcq_039` | Factual Legal Scenario | constitution | MCQ | ⚠️ Yes | ☐ |
| 40 | `dev_scen_mcq_040` | Factual Legal Scenario | ppc | MCQ | ⚠️ Yes | ☐ |
| 41 | `dev_scen_ft_041` | Factual Legal Scenario | ppc | FT | ⚠️ Yes | ☐ |
| 42 | `dev_scen_ft_042` | Factual Legal Scenario | peca | FT | ⚠️ Yes | ☐ |
| 43 | `dev_scen_ft_043` | Factual Legal Scenario | constitution | FT | ⚠️ Yes | ☐ |
| 44 | `dev_scen_ft_044` | Factual Legal Scenario | ppc | FT | ⚠️ Yes | ☐ |
| 45 | `dev_scen_ft_045` | Factual Legal Scenario | peca | FT | ⚠️ Yes | ☐ |
| 46 | `dev_mhop_ft_046` | Complex Multi-Hop | peca | FT | ⚠️ Yes | ☐ |
| 47 | `dev_mhop_ft_047` | Complex Multi-Hop | constitution | FT | ⚠️ Yes | ☐ |
| 48 | `dev_mhop_ft_048` | Complex Multi-Hop | constitution | FT | ⚠️ Yes | ☐ |
| 49 | `dev_mhop_ft_049` | Complex Multi-Hop | constitution | FT | ⚠️ Yes | ☐ |
| 50 | `dev_mhop_ft_050` | Statutory Rule | peca | FT | No | ☐ |
| 51 | `dev_mhop_ft_051` | Complex Multi-Hop | ppc | FT | ⚠️ Yes | ☐ |
| 52 | `dev_mhop_ft_052` | Complex Multi-Hop | constitution | FT | ⚠️ Yes | ☐ |
| 53 | `dev_mhop_ft_053` | Complex Multi-Hop | constitution | FT | ⚠️ Yes | ☐ |
| 54 | `dev_refusal_054` | Negative / Refusal | ppc | FT | No | ☐ |
| 55 | `dev_refusal_055` | Negative / Refusal | peca | FT | No | ☐ |
| 56 | `dev_refusal_056` | Negative / Refusal | constitution | FT | No | ☐ |
| 57 | `dev_refusal_057` | Negative / Refusal | ppc | FT | No | ☐ |
| 58 | `dev_refusal_058` | Negative / Refusal | peca | FT | No | ☐ |
| 59 | `dev_refusal_059` | Negative / Refusal | other_law | FT | No | ☐ |
| 60 | `dev_refusal_060` | Negative / Refusal | other_law | FT | No | ☐ |
| 61 | `dev_refusal_061` | Negative / Refusal | constitution | FT | No | ☐ |
| 62 | `dev_refusal_062` | Negative / Refusal | other_law | FT | No | ☐ |
| 63 | `dev_refusal_063` | Negative / Refusal | foreign_law | FT | No | ☐ |
| 64 | `dev_refusal_064` | Negative / Refusal | foreign_law | FT | No | ☐ |
| 65 | `dev_refusal_065` | Negative / Refusal | non_legal | FT | No | ☐ |
| 66 | `dev_ret_066` | Retrieval | ppc | FT | No | ☐ |
| 67 | `dev_ret_067` | Retrieval | ppc | FT | No | ☐ |
| 68 | `dev_ret_068` | Retrieval | ppc | FT | No | ☐ |
| 69 | `dev_ret_069` | Retrieval | ppc | FT | No | ☐ |
| 70 | `dev_ret_070` | Retrieval | ppc | FT | No | ☐ |
| 71 | `dev_ret_071` | Retrieval | ppc | FT | No | ☐ |
| 72 | `dev_ret_072` | Retrieval | peca | FT | No | ☐ |
| 73 | `dev_ret_073` | Retrieval | peca | FT | No | ☐ |
| 74 | `dev_ret_074` | Retrieval | peca | FT | No | ☐ |
| 75 | `dev_ret_075` | Retrieval | peca | FT | No | ☐ |
| 76 | `dev_ret_076` | Retrieval | constitution | FT | No | ☐ |
| 77 | `dev_ret_077` | Retrieval | constitution | FT | No | ☐ |
| 78 | `dev_ret_078` | Retrieval | constitution | FT | No | ☐ |
| 79 | `dev_ret_079` | Retrieval | constitution | FT | No | ☐ |
| 80 | `dev_ret_080` | Retrieval | constitution | FT | No | ☐ |

---

## Appendix B: Certification

By signing below, the reviewer certifies that they have reviewed all questions
in this package and recorded their decisions above.

| Field | Value |
|:---|:---|
| **Reviewer Name** | |
| **Professional Qualification** | |
| **Bar Council Enrollment (if applicable)** | |
| **Date of Review** | |
| **Signature** | |

> **Disclaimer:** This review package was prepared by an AI system for the purpose
> of facilitating human legal expert review. The proposed answers, citations, and
> reasoning points represent AI-generated analysis verified against statutory text.
> They do not constitute legal advice or expert legal opinion. Final determination
> of legal correctness rests solely with the qualified human reviewer.