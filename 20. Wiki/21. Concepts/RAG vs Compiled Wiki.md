---
type: wiki-page
aliases:
  - RAG vs Wiki
  - RAG vs LLM Wiki
  - Retrieval vs Compilation
description: Comparison between query-time retrieval and a maintained compiled Wiki, presented as complementary design choices rather than mutually exclusive systems.
author:
  - Claude
date created: 2026-04-12T00:00
date modified: 2026-08-29
tags:
  - rag
  - llm-wiki
  - knowledge-management
  - comparison
source:
  - "[[2026-04-12-Karpathy-LLM-Wiki]]"
  - "[[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]"
related:
  - "[[LLM Wiki Pattern]]"
confidence: medium
layer: concepts
status: active
explored: false
claimType: mixed
evidenceScope: multi-source-mixed
verificationStatus: partial
verifiedAt: 2026-08-29
verifiedBy: agent
disputed: false
---

# RAG vs Compiled Wiki

> [!tip] Key Insight
> RAG는 매 질문마다 지식을 재발견한다. Compiled Wiki는 지식을 한 번 컴파일하고 계속 업데이트한다. 축적(accumulation)의 유무가 핵심 차이.

---

## Overview

[[LLM Wiki Pattern]]의 출발점은 기존 RAG(Retrieval-Augmented Generation) 방식의 한계 인식이다. 두 접근은 LLM과 문서의 관계를 근본적으로 다르게 설정한다.

---

## Details

### RAG 방식

1. 문서 컬렉션을 chunk로 분할하여 인덱싱
2. 질문이 들어오면 관련 chunk를 검색
3. LLM이 검색된 chunk를 바탕으로 답변 생성
4. 별도 저장 절차가 없다면 답변 자체는 지식 베이스에 반영되지 않음

**기본 한계**: 순수 query-time retrieval만 사용하면 복합 synthesis를 다시 수행할 수 있다. 다만 RAG 시스템도 답변 저장, cache, memory, curated summary를 추가할 수 있으므로 “축적이 본질적으로 불가능하다”는 뜻은 아니다.

학습용 비유로는 RAG는 "단리"에 가깝고, Compiled Wiki는 "복리"에 가깝다. RAG의 답변은 대화가 끝나면 사라지지만, Compiled Wiki의 좋은 답변과 연결은 다시 Wiki에 남아 다음 Query의 출발점이 된다.

### Compiled Wiki 방식

1. 새 source가 들어오면 LLM이 읽고 wiki에 통합
2. 기존 entity/concept 페이지를 업데이트, 모순 플래그, cross-reference 추가
3. 질문이 오면 이미 컴파일된 wiki에서 답변
4. 좋은 답변은 다시 wiki에 저장 — **지식이 축적**

**가능한 장점**: cross-reference와 synthesis를 재사용할 수 있다. 그러나 완전한 연결, 모순 감지, 모든 source 반영은 자동 보장이 아니라 ingest·verify·lint의 품질에 달려 있다.

### 비교 표

| 차원              | RAG                     | Compiled Wiki       |
| --------------- | ----------------------- | ------------------- |
| 지식 처리 시점        | Query time (매번)         | Ingest time (한 번)   |
| 축적              | 기본 retrieval만으로는 없음 | 파일링 절차가 있으면 있음 |
| Cross-reference | 매번 재구성                  | 사전 구축               |
| 모순 감지           | 별도 파이프라인 필요 | lint/verify 절차 필요 |
| 인프라             | 검색 인덱스·retriever가 흔함 | Markdown·검색 도구·버전관리 선택 가능 |
| 탐색 가능성          | 구현 UI에 따라 다름 | Markdown 도구에서 직접 탐색 가능 |
| 확장성             | 검색 품질·인덱스 설계에 의존 | navigation·search·schema 품질에 의존 |

---

## Trade-offs

> [!warning] Contradiction
> RAG가 항상 열등한 것은 아니다. 대규모(수천 source)에서는 index.md 기반 네비게이션이 한계에 도달하며, embedding-based search가 필요해진다. 두 접근은 상호 보완적일 수 있다 — wiki 위에 RAG를 얹는 하이브리드 구조.

> [!note] Bias Check
> 이 비교는 compiled Wiki를 제안한 원문에서 출발하므로 RAG의 단순한 형태를 비교 대상으로 삼는 경향이 있다. 실제 RAG 시스템은 memory·cache·knowledge graph·human curation을 결합할 수 있고, compiled Wiki도 qmd 같은 retrieval을 사용한다. 품질·비용·지연시간 비교 데이터는 이 볼트에 없다.

---

## Related

- [[LLM Wiki Pattern]] — compiled wiki의 전체 패턴

---

## Sources

- [[2026-04-12-Karpathy-LLM-Wiki]]
- [[2026-07-16-WikiDocs-LLM-Wiki-RAG를-넘어서]]
