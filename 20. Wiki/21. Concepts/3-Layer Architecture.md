---
type: wiki-page
aliases:
  - Three Layer Architecture
  - Raw Sources Wiki Schema
  - LLM Wiki Architecture
description: The 3-layer architecture of this LLM Wiki — preserved Raw Sources, LLM-maintained Wiki pages, and Codex behavior rules led by AGENTS.md and repo-scoped skills.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - llm-wiki
  - architecture
  - knowledge-management
source:
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - "[[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
  - AGENTS.md
related:
  - "[[LLM Wiki Pattern]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Mothership-Satellite Vault Pattern]]"
  - "[[Human-AI Knowledge Boundary]]"
confidence: high
layer: concepts
status: active
explored: false
claimType: definition
evidenceScope: multi-source-mixed
verificationStatus: verified
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# 3-Layer Architecture

> [!tip] Key Insight
> Raw Sources(불변 원본) → Wiki(LLM 관리 지식) → Schema(행동 규칙). 세 층의 분리가 LLM Wiki의 구조적 핵심이다.

---

## Overview

[[LLM Wiki Pattern]]은 세 개의 명확히 분리된 층(layer)으로 구성된다. 각 층은 고유한 소유자와 규칙을 가진다.

---

## Details

### Layer 1: Raw Sources (원본층)

```
10. Raw Sources/
├── 11. Articles/     # 웹 기사, 블로그 포스트
├── 12. Papers/       # 학술 논문, 기술 보고서
├── 13. Books/        # 도서 노트, 챕터 요약
├── 14. Transcripts/  # 강연, 팟캐스트, 영상 전사
├── 15. Clippings/    # 웹 클리핑, 스크랩
└── 16. AI Research/  # AI-assisted research capture
```

- **소유자**: 인간이 큐레이션
- **규칙**: 원문을 `## Original Content` 아래 보존. 명시적인 ingest/source-update가 아닌 일반 Wiki 작업에서는 재작성하지 않음
- **역할**: Source of truth. 모든 wiki 페이지의 근거
- **Frontmatter**: `type: raw-source`, `date ingested`, `category`

### Layer 2: The Wiki (지식층)

```
20. Wiki/
├── 21. Concepts/     # 추상 개념 (Attention, Transformer, RLHF, ...)
├── 22. Entities/     # 사람, 조직, 제품 (OpenAI, Karpathy, GPT-4, ...)
├── 23. Guides/       # How-to, 튜토리얼, 실전 가이드
└── 24. Maps/         # MOC (Map of Content), 주제별 인덱스
```

- **소유자**: LLM이 전적으로 관리
- **규칙**: 인간은 읽고, LLM이 작성. 모든 주장에 출처 명시
- **역할**: Pre-synthesized, cross-referenced 지식 페이지
- **Frontmatter**: `type: wiki-page`, `source`, `related`, `confidence`

### Layer 3: The Schema (규칙층)

- **파일**: `AGENTS.md` → `.agents/skills/` → `.codex/commands/`가 현재 Codex 정본. `CLAUDE.md`는 legacy mirror
- **소유자**: 인간과 LLM이 공동 진화(co-evolve)
- **규칙**: LLM의 행동을 제어하는 핵심 설정 문서
- **역할**: Wiki의 구조, 컨벤션, 워크플로를 정의. 이것이 LLM을 "규율 있는 wiki 관리자"로 만드는 핵심

### 층 간 관계

```
Schema (AGENTS.md + repo skills)
    │ 제어
    ▼
Wiki ◀──── compile ──── Raw Sources
    │                        ▲
    └── reference ───────────┘
```

- Schema가 LLM의 행동을 **제어**
- Raw Sources를 LLM이 Wiki로 **컴파일**
- Wiki가 Raw Sources를 **역참조** (`source` 프로퍼티)
- Raw Sources의 Original Content는 보존되며, 명시적 source-update만 예외

학습 관점에서 이 구조는 "원본과 해석을 분리한다"는 점이 가장 중요하다. Raw Source는 나중에 다시 확인할 수 있는 근거이고, Wiki는 LLM이 유지보수하는 학습 인터페이스이며, Schema는 그 LLM 편집자의 행동 규칙이다.

### 이 볼트에서의 구현

| Layer | 경로 | 구현 |
|-------|------|------|
| Raw Sources | `10. Raw Sources/` | 6개 하위 폴더 (11.Articles, 12.Papers, 13.Books, 14.Transcripts, 15.Clippings, 16.AI Research) |
| Wiki | `20. Wiki/` | 4개 하위 폴더 (21.Concepts, 22.Entities, 23.Guides, 24.Maps) |
| Schema | `AGENTS.md`, `.agents/skills/`, `.codex/commands/` | Frontmatter 규격, 안전 규칙, Operations 정의 |

> [!note] 개념적 3층 vs 물리적 폴더
> 이 볼트에는 `30. Queries/` 물리 폴더도 있다 (Query 산출물 위치). 하지만 이는 *4번째 구조 레이어가 아니라* [[Ingest-Query-Lint Cycle]] 의 *Query 단계 산출물*이다. **구조 축**은 Raw/Wiki/Schema 3층이 정본이고, `30. Queries` 는 그 위에서 작동하는 **운영 축**의 결과물.

---

## Related

- [[LLM Wiki Pattern]] — 이 아키텍처를 사용하는 전체 패턴
- [[Ingest-Query-Lint Cycle]] — 이 아키텍처 위에서 작동하는 operations

### 볼트 단위 확장

[[Mothership-Satellite Vault Pattern]]은 이 경계 설정을 vault 단위로 확장한다. 사용자가 직접 쓰고 설명할 수 있는 지식은 mothership에, LLM이 source를 읽어 컴파일한 학습용 지식은 satellite LLM Wiki에 둔다. 이는 Raw/Wiki/Schema의 내부 분리와 같은 원리를 더 큰 단위에 적용한 것이다.

> [!note] Bias Check
> 세 층은 원문과 해석의 provenance를 관리하기 위한 이 저장소의 운영 모델이다. 폴더 분리만으로 정확성·최신성·사용자 이해가 보장되지는 않으며 verify와 lint가 별도로 필요하다. `30. Queries/`와 attachments 같은 물리 경로가 추가되어도 역할 모델 자체를 자동으로 네 층 이상으로 재정의하지 않는다.

---

## Sources

- [[2026-04-12-Karpathy-LLM-Wiki]]
- [[2026-07-07-에이전트를-위한-지식-베이스-LLM-Wiki-활용]]
- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
