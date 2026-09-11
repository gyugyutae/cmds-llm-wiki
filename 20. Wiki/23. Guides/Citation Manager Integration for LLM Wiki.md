---
type: wiki-page
aliases:
  - Zotero Integration for LLM Wiki
  - Bookends Integration for LLM Wiki
  - Citation Manager Integration
description: A guide stub for connecting LLM Wiki raw sources and wiki pages to citation managers such as Zotero or Bookends for citation-ready academic writing.
author:
  - Codex
date created: 2026-07-07
date modified: 2026-08-29
tags:
  - guide
  - citation-management
  - zotero
  - bookends
  - llm-wiki
source:
  - "[[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]"
related:
  - "[[Agent-Readable Metadata]]"
  - "[[3-Layer Architecture]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
confidence: low
layer: guides
explored: false
claimType: prescriptive
evidenceScope: user-original
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
status: active
---

# Citation Manager Integration for LLM Wiki

> [!tip] Key Insight
> Citation-ready 학술 workflow가 필요하다면 Wiki의 `source` metadata와 Zotero·Bookends 식별자를 연결하는 방식을 검토할 수 있다. 현재는 구현되지 않은 설계안이다.

---

## Purpose

이 페이지는 Zotero 또는 Bookends를 LLM Wiki와 연결하기 위한 guide stub이다. 현재 vault에는 Raw Source와 Wiki page의 source trace는 있지만, citation manager의 서지정보를 직접 여는 필드 표준은 아직 없다.

2026-08-29 현재 `10. Raw Sources/`와 `90. Settings/`에서 아래 제안 필드를 검색했지만 실제 사용 사례를 찾지 못했다. 따라서 필드명, deep link 형식, 검증 workflow는 확정 schema가 아니다.

---

## Proposed Fields

Raw Source frontmatter에 다음 필드를 추가하는 방식을 검토한다.

```yaml
citationKey: ""
doi: ""
bibliographyManager: ""
bibliographyLink: ""
citationStatus: missing
```

| Field | Meaning |
|-------|---------|
| `citationKey` | Zotero Better BibTeX 또는 Bookends citekey |
| `doi` | DOI 또는 안정 식별자 |
| `bibliographyManager` | `zotero`, `bookends`, or `manual` |
| `bibliographyLink` | citation manager deep link |
| `citationStatus` | `missing`, `linked`, `verified` |

---

## Workflow

1. Source를 `00. Inbox/`에 capture한다.
2. `/ingest` 전에 citation manager에서 해당 항목을 만들거나 찾는다.
3. Raw Source에 `citationKey`와 deep link를 기록한다.
4. Wiki page는 Raw Source를 `source`로 참조한다.
5. Query result는 인용 가능한 claim마다 Raw Source와 citekey를 함께 보여준다.

---

## Open Questions

> [!question] Zotero vs Bookends link format
> Zotero와 Bookends의 deep link 형식, Better BibTeX citekey 안정성, Windows/Mac 호환성을 확인해야 한다.

> [!question] Template integration
> `Template_Raw Source.md`에 citation field를 기본 추가할지, Papers category에만 추가할지 결정해야 한다.

> [!question] Verification
> `citationStatus: verified`를 누가, 어떤 기준으로 부여할지 정해야 한다. DOI 확인, title match, author/year match가 최소 기준 후보.

> [!note] Bias Check
> Citation manager 연결은 출처 추적 편의성을 높일 수 있지만 claim 정확성이나 원문 독해를 자동 보장하지 않는다. 실제 Zotero/Bookends link 형식과 cross-platform 동작을 확인하기 전에는 이 예시 필드를 template에 추가하지 않는다.

---

## Related

- [[Agent-Readable Metadata]]
- [[3-Layer Architecture]]
- [[Obsidian Tooling for LLM Wiki]]

---

## Sources

- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
