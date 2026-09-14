---
type: query-result
aliases:
  - 팀 회의용 학기 프로젝트 2안
description: "Two comparable one-page semester project proposals for a team decision: an agentic UAV digital thread and an auditable Upbit decision-provenance system."
author:
  - Codex
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - query
  - team-proposal
  - traceability
  - upbit
  - emerging-technology
source:
  - "[[2026-09-01-Q-emerging-traceability-technology-selection]]"
  - "[[2026-09-01-Q-upbit-financial-decision-traceability-project]]"
  - "[[2026-09-01-Q-software-engineering-semester-project-selection]]"
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 프로젝트 증거
confidence: high
status: active
---

# 팀 회의용 학기 프로젝트 2안

## 공통 원칙

신기술 자체가 주제가 아니다. `새 기술이 없으면 풀기 어려운 구체적인 문제`를 먼저 제시하고, 8주차에는 핵심 흐름이 작동해야 한다. 최신 기술은 한 개를 headline으로, 한 개를 stretch goal로 둔다.

## A안 — TracePilot AI

### 한 문장

> 무인기 요구사항·비행 규칙·시험·텔레메트리의 변경을 시간 순서대로 연결하고, AI agent가 누락된 연결과 변경 영향을 제안하는 Agentic Digital Thread다.

### 문제

무인기 프로젝트 자료가 요구사항 문서, 코드, 시험표, 비행 로그로 흩어져 어떤 요구사항이 검증됐고 변경 시 무엇을 다시 시험해야 하는지 찾기 어렵다.

### 최신 기술

- Headline: **Agentic Digital Thread + Temporal Knowledge Graph**
- 구현 기술: Neo4j 또는 PostgreSQL graph model, embedding/LLM link suggestion, human approval
- Stretch: GraphRAG형 다단계 영향 검색 또는 LangGraph review workflow

### 8주차 데모

`REQ-12 고도 제한` 변경 → 연결된 FlightRule·TestCase·TelemetryEvidence 표시 → AI가 재시험 후보와 근거 제안 → 사용자가 승인 → 시간축 graph 갱신.

### 독창성 질문

> 정적 trace matrix가 아니라, 요구사항이 바뀔 때마다 연결의 버전과 근거를 보존하고 AI가 재시험 범위를 제안할 수 있는가?

### 범위 위험

실제 드론·GNN 학습·완전 자율 agent를 넣으면 실패한다. 연구실 사용자와 데이터에 접근할 수 있을 때만 1순위가 된다.

## B안 — WhyBuy

### 한 문장

> Upbit 적립식 매매에서 사용자 의도부터 당시 시장 데이터·위험 규칙·승인·주문 결과까지 Decision Receipt로 남기고 과거 결정을 재현하는 AI 매매 블랙박스다.

### 문제

자동매매·AI agent는 주문 결과는 남기지만 당시 어떤 전략 버전과 데이터, 위험 기준, 승인 때문에 매수하거나 보류했는지를 정확히 재현하기 어렵다.

### 최신 기술

- Headline: **Decision Provenance + Counterfactual Replay**
- 구현 기술: event-sourced receipt, hash-linked tamper evidence, Upbit point-in-time snapshot
- Stretch: OpenTelemetry GenAI agent/tool-call observability

### 8주차 데모

적립 정책 실행 → 변동성 risk gate로 HOLD → Decision Receipt 생성 → `왜 안 샀지?` 근거 조회 → 변동성 기준 8%를 10%로 바꾼 counterfactual replay에서 BUY와 비교.

### 독창성 질문

> 수익률을 자랑하는 봇이 아니라, 한 금융 결정을 나중에 똑같이 재현하고 정책 하나가 달랐다면 결과가 어떻게 변했는지 증명할 수 있는가?

### 범위 위험

실제 자금 자동매매와 가격 예측을 넣으면 검증·보안 범위가 폭발한다. paper/test order로 제한해야 한다.

## 동일 기준 비교

| 기준 | TracePilot AI | WhyBuy |
|---|---:|---:|
| 최신 기술 인상 | 5 | 5 |
| 12주 완수 가능성 | 3 | 4 |
| 수업 산출물 적합성 | 5 | 5 |
| 실제 사용자 인터뷰 | 연구실 접근 시 5 | 개인 투자자 접근 시 4 |
| 포트폴리오 차별성 | 연구·드론 5 | 금융 백엔드 5 |
| 데이터 준비 난도 | 높음 | 중간 |
| 안전한 데모 | 4 | 5 |
| 김규태 현재 취업 방향 | 4 | 5 |

## 팀 회의 진행

1. 두 안을 각각 90초만 설명한다.
2. 팀원 각자가 `하고 싶은 역할`, `가장 큰 실패 위험`, `인터뷰할 사용자 1명`을 적는다.
3. 사용자 접근성 30, 8주차 데모 가능성 25, 팀 흥미 20, 포트폴리오 15, 신기술 검증 가능성 10으로 익명 점수화한다.
4. 최고점 주제를 선택하고 headline 기술 하나와 stretch 기술 하나만 남긴다.
5. 선택 직후 8주차 데모 문장을 고정하고 나머지 아이디어는 backlog로 보낸다.

## 현재 추천

연구실에서 실제 무인기 요구사항·시험 데이터와 인터뷰 대상자를 확보할 수 있으면 TracePilot AI가 수업의 `실질적 가치·인터뷰 가능한 사용자` 기준에 강하다. 그 접근이 불확실하면 WhyBuy가 구현 가능성과 김규태의 금융 시스템 취업 서사에서 더 강하다.

발표에서 `젊은 패기`는 기술을 많이 넣는 것으로 증명하지 않는다. 최신 기술의 한계를 직접 설정하고 baseline·실패 조건·재현 테스트로 검증하는 태도로 보여준다.

> [!note] Bias Check
> 두 이름과 기능 결합의 독창성은 시장에 동일 제품이 전혀 없다는 뜻이 아니다. 팀 결정 전 관련 제품 3개씩을 추가 조사하고, 인터뷰에서 실제 불편을 확인해야 비즈니스 가치 주장을 할 수 있다.

이 답변은 강의/수업/교육과 취업/포트폴리오에 활용 가능합니다 — 두 후보를 같은 기준과 8주차 데모로 비교해 팀이 기술 취향이 아니라 실행 가능성까지 포함해 결정하게 합니다.

## Reassessment — 2026-09-02

사용자 피드백과 팀 규모 3명을 반영해 두 후보를 [[2026-09-02-Q-three-person-upbit-drone-traceability-proposals]]로 교체했다. 금융안은 투자 의도 추적에서 Upbit 주문 장애 trace·replay로, 무인기안은 외부 데이터에 의존하는 GraphRAG 추천에서 PX4 SIH가 직접 시험 증거를 만드는 Executable Digital Thread로 변경했다.
