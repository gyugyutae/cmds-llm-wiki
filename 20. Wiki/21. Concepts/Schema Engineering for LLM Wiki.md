---
type: wiki-page
aliases:
  - LLM Wiki Schema Engineering
  - 스키마 엔지니어링
  - Schema Engineering
description: Schema engineering for LLM Wiki is the practice of designing durable rules, metadata, page types, and operating workflows so agents can maintain a growing markdown knowledge base consistently.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - llm-wiki
  - schema
  - agent-workflow
  - knowledge-management
source:
  - "[[2026-07-16-Q-index-rag-agent-read-write-schema-engineering]]"
  - "[[3-Layer Architecture]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Ingest-Query-Lint Cycle]]"
related:
  - "[[3-Layer Architecture]]"
  - "[[Agent-Readable Metadata]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[RAG vs Compiled Wiki]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: interpretive
evidenceScope: synthesis-only
verificationStatus: unverified
---

# Schema Engineering for LLM Wiki

> [!tip] Key Insight
> LLM Wiki가 커질수록 품질을 결정하는 것은 단순히 "LLM이 똑똑한가"가 아니라, LLM이 어떤 스키마 아래에서 읽고 쓰는가다.

---

## Overview

**Schema Engineering for LLM Wiki**는 agent가 장기적으로 일관된 지식 베이스를 유지보수할 수 있도록 page type, frontmatter, wikilink 규칙, source 보존 규칙, ingest/query/lint workflow를 설계하는 작업이다.

[[3-Layer Architecture]]에서 Schema는 Raw Source와 Wiki 위에 있는 규칙층이다. 이 층이 약하면 LLM은 매번 다른 방식으로 파일을 쓰고, source와 해석이 섞이며, confidence와 verification boundary가 흐려진다. 반대로 스키마가 좋으면 agent는 지루한 유지보수 작업을 반복 가능하게 수행한다.

---

## Why It Matters

기존 인간 위키가 실패하는 이유는 대개 지식 작성이 아니라 유지보수다. 연결 갱신, 중복 제거, 오래된 주장 표시, source 추적, index 업데이트가 누적되면 비용이 가치보다 빨리 커진다. [[LLM Wiki Pattern]]은 이 유지보수를 LLM에게 맡기지만, LLM이 제대로 유지보수하려면 명확한 schema가 필요하다.

Schema engineering은 다음 질문에 답한다.

- Raw Source는 어떤 형식으로 보존하는가?
- Wiki page는 어떤 frontmatter를 가져야 하는가?
- `source`, `related`, `confidence`, `verificationStatus`는 어떤 의미인가?
- Query result는 언제 저장하는가?
- `explored: false`와 `explored: true`는 어떻게 구분하는가?
- Lint는 무엇을 문제로 보고 무엇을 고치지 않는가?

## Schema As Agent Interface

스키마는 사람용 문서 형식이 아니라 agent용 인터페이스다. LLM은 `index.md`, YAML frontmatter, `source`, `related`, MOC 목록을 보고 어떤 파일을 읽고 수정할지 결정한다.

따라서 좋은 schema는 다음 특성을 가진다.

| 특성 | 의미 |
|------|------|
| 명시적 page type | Raw Source, Wiki, Query, MOC의 역할을 구분한다 |
| source trace | 모든 synthesis가 원문으로 돌아갈 수 있게 한다 |
| verification boundary | AI가 정리한 지식과 사용자가 검토한 지식을 분리한다 |
| routing metadata | agent가 전체 본문을 읽기 전에 관련 후보를 찾게 한다 |
| lintable rules | 자동 점검 가능한 형식으로 품질 기준을 만든다 |

## Difference From Prompt Engineering

Prompt engineering은 한 번의 대화를 잘 제어하는 기술에 가깝다. Schema engineering은 여러 번의 ingest, query, lint, verify 사이클이 지나도 agent가 같은 방식으로 지식을 유지하게 만드는 기술이다.

LLM Wiki에서는 prompt보다 schema가 오래 산다. prompt는 대화가 끝나면 사라질 수 있지만, schema는 파일 시스템과 repo 규칙으로 남아 다음 agent 실행에도 영향을 준다.

> [!note] Bias Check
> Counter-argument: 스키마가 너무 복잡하면 ingest 속도가 느려지고 사용자가 위키 운영 자체에 피로를 느낄 수 있다.
> Data gap: 어떤 수준의 schema가 개인 LLM Wiki에서 최적 비용/효과를 가지는지는 아직 이 vault에서 정량 측정하지 않았다.

---

## Related

- [[3-Layer Architecture]] — Schema layer의 구조적 위치
- [[Agent-Readable Metadata]] — frontmatter를 agent routing surface로 쓰는 관점
- [[Human-AI Knowledge Boundary]] — AI가 쓴 지식과 사용자가 아는 지식의 경계
- [[Ingest-Query-Lint Cycle]] — schema가 제어하는 운영 루프
- [[RAG vs Compiled Wiki]] — compiled wiki의 품질이 schema에 의존하는 이유

---

## Sources

- [[2026-07-16-Q-index-rag-agent-read-write-schema-engineering]]
- [[3-Layer Architecture]]
- [[LLM Wiki Pattern]]
- [[Ingest-Query-Lint Cycle]]
