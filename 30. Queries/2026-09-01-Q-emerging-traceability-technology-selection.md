---
type: query-result
aliases:
  - 최신 추적성 기술 학기 프로젝트 선정
description: "An evidence-based selection of an emerging traceability technology that is novel, course-aligned, and feasible within a 12-week semester."
author:
  - Codex
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - query
  - traceability
  - graphrag
  - knowledge-graph
  - llm
source:
  - "[[2026-09-01-Q-software-engineering-semester-project-selection]]"
  - "[[Graduation-elasticsearch]]"
  - https://arxiv.org/abs/2602.01253
  - https://arxiv.org/abs/2412.08593
  - https://doi.org/10.1109/APSEC66846.2025.00070
  - https://microsoft.github.io/graphrag/
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 프로젝트 증거
  - 학부연구생/학술
confidence: high
status: active
---

# 최신 추적성 기술 학기 프로젝트 선정

## 최종 판단

한 가지 신기술은 **Human-in-the-loop 경량 GraphRAG형 trace-link 추천**으로 정한다.

정확한 구현은 `도메인 지식 그래프 + embedding 후보 검색 + LLM link 판정·근거 생성 + 사람 승인/거절`이다. Microsoft GraphRAG 전체를 제품 핵심으로 가져오거나 모델을 학습하지 않는다.

프로젝트 이름 후보:

> DroneTrace AI — GraphRAG형 지식 그래프로 무인기 요구사항과 시험 증거를 연결하는 추적성 플랫폼

## 조사 결과

2026-09-01 GitHub API 관측치이며 star는 변동한다.

| 기술 흐름 | 대표 근거 | GitHub stars | 추적성 적합 | 12주 가능성 | 판단 |
|---|---|---:|---:|---:|---|
| Knowledge Graph + GraphRAG | Microsoft GraphRAG, 2024 Graph-RAG traceability 논문 | 35,760 | 5 | 4 | **선정: 경량 구현** |
| LLM trace-link recovery | TraceLLM 2026, doc-code traceability 2025 | 연구 직접성 높음 | 5 | 5 | 선정안의 AI 판정 단계 |
| Agentic AI + human approval | LangGraph | 40,806 | 4 | 2 | 승인 workflow만 선택 적용 |
| Graph DB | Neo4j | 17,173 | 5 | 4 | 데이터가 충분하면 사용 |
| Vector DB | Qdrant | 34,302 | 3 | 4 | PostgreSQL pgvector로 대체 가능 |
| Data lineage | OpenLineage | 2,634 | 3 | 3 | 개념 참고, 무인기에는 직접 적용하지 않음 |
| Heterogeneous GNN | HGTRTracer, APSEC 2025 | 논문 단계 | 5 | 1 | 학습 데이터·평가 부담으로 제외 |
| Artifact provenance | Sigstore cosign | 6,270 | 3 | 3 | CI 산출물 서명 stretch goal |

## 왜 이 기술인가

- TraceLLM은 aerospace·healthcare를 포함한 네 benchmark에서 LLM 기반 trace-link 추천을 평가하고, 분석가가 후보를 검토하는 semi-automated workflow를 제안한다.
- Graph-RAG traceability 연구는 지식 그래프 검색과 LLM을 결합해 aerospace 요구사항의 traceability/compliance를 다뤘다. 다만 비용과 구현 복잡성, 입력 그래프 품질 의존성을 한계로 명시한다.
- HGTRTracer는 LLM의 link 이유 노드와 heterogeneous graph transformer를 결합해 평균 F1 향상을 보고했지만, 한 학기 프로젝트에서 GNN 학습·ground truth 구축까지 수행하기에는 과하다.
- Microsoft GraphRAG는 큰 생태계를 확보했지만 2026-09-01 현재 저장소가 maintenance mode라고 명시한다. 따라서 이름과 구조를 학습하되 패키지 자체에 제품을 종속시키지 않는다.

## MVP 구조

```text
요구사항 REQ
  ↓ embedding top-k 후보 검색
비행 규칙 / 시험 케이스 / MAVLink 로그 이벤트
  ↓ LLM structured output
후보 링크 + confidence + 짧은 근거 + 원문 인용
  ↓ human-in-the-loop
승인 / 거절 / 수정
  ↓
확정 trace graph와 변경 영향 분석
```

### 그래프 노드

- Requirement
- FlightRule
- TestCase
- Mission
- TelemetryEvidence
- Defect

### 그래프 엣지

- `VERIFIED_BY`
- `IMPLEMENTED_BY`
- `VIOLATED_BY`
- `DERIVED_FROM`
- `AFFECTS`

## 범위 고정

필수 기능:

1. 사람이 명시적으로 만든 trace link CRUD와 그래프 시각화
2. 요구사항 한 건에 대해 embedding top-5 후보 검색
3. LLM이 후보별 링크 여부·근거를 JSON으로 반환
4. 사람이 승인·거절하고 그 이력을 보존
5. 요구사항 변경 시 연결된 시험·규칙 영향 표시
6. baseline TF-IDF 또는 embedding-only와 LLM reranking을 precision/recall/F1로 비교

제외:

- GNN 직접 학습
- 완전 자율 에이전트
- Microsoft GraphRAG 전체 indexing/community pipeline
- 실제 비행 제어
- 블록체인
- Remote ID 규제 준수 인증

## 강의 산출물 연결

| 강의 항목 | 프로젝트 증거 |
|---|---|
| 요구분석 | 연구자/시험 담당자 인터뷰, 승인 가능한 trace-link 요구사항 |
| UML | 추천·검토 use case, link approval sequence, graph domain class diagram |
| SOLID | Retriever, LinkPredictor, Reviewer, EvidenceRepository 인터페이스 분리 |
| 디자인 패턴 | Strategy로 TF-IDF/embedding/LLM 추천기 교체, Repository로 저장소 분리 |
| 테스트 | 규칙 단위 테스트, LLM schema contract test, 고정 benchmark 회귀 테스트 |
| CI | unit/integration/evaluation pipeline과 결과 artifact 보존 |
| AI 사용 보고 | prompt/version/model/input/output/사람 결정 audit log |

## 12주 가능성 판단

**조건부 가능**이다. 8주차까지는 명시 링크·embedding 검색·승인 UI가 완성돼야 하며, LLM은 한 번의 structured-output 판정만 담당해야 한다. 30~50개 요구사항과 100~200개 후보 artifact, 사람이 만든 50~100개 gold link면 수업용 비교 실험이 가능하다. 이것은 산업적 일반화 증거가 아니라 학기 MVP 검증 자료다.

성공 기준:

- baseline 대비 F1 또는 후보 검토시간 개선
- 모든 추천에 원문 근거와 모델·prompt version 기록
- 사람이 거절한 link가 확정 graph에 들어가지 않음
- LLM 장애 시 수동 traceability 기능이 계속 동작
- 핵심 도메인 로직을 사용자가 직접 설명·수정·테스트 가능

> [!note] Bias Check
> 높은 GitHub star는 산업 효과나 프로젝트 적합성을 증명하지 않는다. GraphRAG와 agent framework는 인기 신호로만 사용했다. 논문 성능은 데이터셋·prompt·모델에 따라 달라지므로 DroneTrace의 자체 gold set에서 baseline과 재검증해야 한다. GraphRAG라는 이름을 붙이기 위해 불필요한 그래프 community summarization을 구현하지 않는다.

## Sources

- TraceLLM: https://arxiv.org/abs/2602.01253
- Graph-RAG requirement traceability: https://arxiv.org/abs/2412.08593
- HGTRTracer: https://doi.org/10.1109/APSEC66846.2025.00070
- Documentation-to-code evaluation: https://arxiv.org/abs/2506.16440
- Microsoft GraphRAG docs: https://microsoft.github.io/graphrag/
- GitHub repositories: https://github.com/microsoft/graphrag, https://github.com/langchain-ai/langgraph, https://github.com/neo4j/neo4j, https://github.com/qdrant/qdrant, https://github.com/OpenLineage/OpenLineage, https://github.com/sigstore/cosign

이 답변은 강의/수업/교육과 취업/포트폴리오에 활용 가능합니다 — 최신 연구를 과도한 기술 시연이 아니라 측정 가능한 trace-link 추천 기능으로 축소한 실행안입니다.

## Reassessment

사용자가 기존 trace-link 추천 기능의 독창성 부족을 지적하고 금융·Upbit 방향을 선호해, 최종 제품 후보는 [[2026-09-01-Q-upbit-financial-decision-traceability-project]]의 intent-to-order decision provenance로 재설계했다. 이 페이지의 GraphRAG 안은 무인기 traceability를 선택할 경우의 대안으로 유지한다.
