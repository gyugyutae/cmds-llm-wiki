---
type: wiki-page
aliases:
  - Personalized LLM Context
  - Personal LLM Context Layer
  - 사용자 맥락층
  - 개인 맞춤형 LLM 맥락
description: The LLM Wiki can act as a high-quality personal context layer for LLMs by externalizing the user's projects, goals, beliefs, questions, learning history, and self-knowledge into readable markdown.
author:
  - Codex
date created: 2026-07-16
date modified: 2026-07-16
tags:
  - llm-wiki
  - personalization
  - context-engineering
  - self-knowledge
source:
  - "[[2026-07-16-Q-personal-context-knowledge-compounding-query-feedback]]"
  - "[[Core Context]]"
  - "[[김규태]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Ingest-Query-Lint Cycle]]"
  - "[[Human-AI Knowledge Boundary]]"
related:
  - "[[김규태]]"
  - "[[Core Context]]"
  - "[[LLM Wiki Pattern]]"
  - "[[LLM Wiki as Learning Base]]"
  - "[[Human-AI Knowledge Boundary]]"
  - "[[Agent-Readable Metadata]]"
  - "[[Schema Engineering for LLM Wiki]]"
  - "[[Obsidian Tooling for LLM Wiki]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: interpretive
evidenceScope: synthesis-only
verificationStatus: unverified
---

# Personal Context Layer for LLM Wiki

> [!tip] Key Insight
> LLM Wiki는 일반 지식 검색 도구가 아니라, LLM에게 "나에 대한 고품질 맥락"을 제공하는 개인 context layer가 될 수 있다.

---

## Overview

**Personal Context Layer for LLM Wiki**는 LLM Wiki를 개인 맞춤형 LLM을 위한 맥락 공급층으로 보는 관점이다. 모델 성능이 상향 평준화될수록 차이는 일반 지식보다 사용자의 프로젝트, 목표, 취향, 질문, 판단 기준, 학습 이력 같은 개인 맥락에서 생긴다.

이 vault에서 그 역할은 [[Core Context]], [[김규태]], 프로젝트 entity, 개념 page, Query result가 함께 수행한다. 사용자는 source를 큐레이션하고 질문을 던지며, agent는 그 맥락을 markdown 파일로 구조화한다.

## Why It Matters

일반 LLM은 많은 것을 알지만, 기본 상태에서는 김규태가 어떤 프로젝트를 했는지, 왜 이 자료에 감명받았는지, 어떤 직무와 삶의 방향을 고민하는지 모른다. 따라서 개인 맞춤형 답변의 병목은 모델 지능보다 **사용자 맥락 제공 품질**이 될 수 있다.

LLM Wiki는 이 병목을 다음 방식으로 줄인다.

| 맥락 종류 | Wiki 구현 |
|-----------|-----------|
| 정체성/목표 | [[Core Context]], [[김규태]] |
| 프로젝트 증거 | 프로젝트 entity와 Raw Source |
| 학습 관심사 | concept page, MOC |
| 반복 질문 | `30. Queries/` |
| 판단 기준 | Core Context 운영 원칙, Wiki synthesis |
| 검증 경계 | `explored`, `verificationStatus`, `confidence` |

## Knowledge Compounding

개인 맥락은 한 번에 완성되지 않는다. 좋은 source, 좋은 질문, 좋은 회고가 들어올 때마다 Wiki가 갱신되고, 그 갱신된 Wiki가 다음 Query의 출발점이 된다.

이 때문에 LLM Wiki의 복리는 단순히 파일 수가 늘어나는 것이 아니라, **다음 질문의 시작 위치가 높아지는 것**이다. 어제의 Query가 오늘의 Wiki 링크가 되고, 오늘의 Wiki 링크가 내일의 더 정확한 개인 맞춤 답변으로 돌아온다.

## Self-Knowledge Role

LLM Wiki는 LLM을 더 잘 쓰기 위한 도구인 동시에 자기 이해 도구다. 머릿속에 흩어져 있던 생각을 Wiki page와 wikilink로 외부화하면, Obsidian Graph View에서 반복되는 관심사와 고립된 생각을 볼 수 있다.

이 점에서 Graph View는 "지식의 양"보다 "생각의 구조"를 보여준다. 어떤 프로젝트가 어떤 개념과 연결되는지, 어떤 질문이 반복되는지, 어떤 클러스터가 커지는지 보면 사용자는 자기 관심과 판단 기준을 더 명확히 파악할 수 있다.

## Operational Criteria

Query에서 나온 생각을 Wiki에 반영할지는 다음 기준으로 판단한다.

| 기준 | Wiki 반영 방식 |
|------|----------------|
| 일회성 답변 | `30. Queries/`에만 저장 |
| 기존 개념 보강 | 기존 Wiki page 업데이트 |
| 반복 가능한 새 추상 개념 | 새 Concept page 생성 |
| 사용자의 장기 정체성/운영 원칙 | [[Core Context]] 업데이트 후보 |
| 원문 증거 | Raw Source로 ingest |

이번 개념은 LLM Wiki의 personalization 가치를 설명하는 재사용 가능한 abstraction이므로 독립 Concept page로 둔다.

> [!note] Bias Check
> Counter-argument: 개인 맥락이 많아질수록 답변이 과도하게 자기확증적으로 변할 수 있다.
> Data gap: 개인 Wiki 맥락이 실제 LLM 답변 품질을 얼마나 개선하는지는 이 vault에서 정량 평가하지 않았다.

---

## Related

- [[Core Context]] — 사용자 맥락의 압축본
- [[김규태]] — owner entity
- [[LLM Wiki Pattern]] — source를 persistent wiki로 컴파일하는 기본 패턴
- [[LLM Wiki as Learning Base]] — 관심 있지만 아직 모르는 내용을 학습 가능한 형태로 보존
- [[Human-AI Knowledge Boundary]] — AI가 정리한 지식과 사용자가 아는 지식의 경계
- [[Agent-Readable Metadata]] — 개인 맥락을 agent가 읽을 수 있게 만드는 표면
- [[Schema Engineering for LLM Wiki]] — 맥락층 품질을 유지하는 규칙 설계

---

## Sources

- [[2026-07-16-Q-personal-context-knowledge-compounding-query-feedback]]
- [[Core Context]]
- [[김규태]]
- [[LLM Wiki Pattern]]
- [[Ingest-Query-Lint Cycle]]
- [[Human-AI Knowledge Boundary]]
