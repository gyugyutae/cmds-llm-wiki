---
type: query-result
aliases:
  - Upbit 금융 의사결정 추적성 프로젝트
  - WhyBuy 프로젝트
description: "A distinctive 12-week Upbit project that traces user intent, strategy versions, market evidence, AI actions, risk approvals, and simulated order outcomes into replayable decision receipts."
author:
  - Codex
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - query
  - upbit
  - fintech
  - decision-provenance
  - agent-observability
source:
  - "[[2026-09-01-Q-software-engineering-semester-project-selection]]"
  - "[[2026-09-01-Q-emerging-traceability-technology-selection]]"
  - "[[김규태 금융 시스템 개발자 취업 로드맵]]"
  - "[[백테스트 과적합과 편향]]"
  - https://docs.upbit.com/kr/docs/upbit-strategy-toolkit-reference
  - https://docs.upbit.com/kr/reference/order-test
  - https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
  - https://arxiv.org/abs/2601.20727
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 백엔드/성능/금융 시스템
  - 프로젝트 증거
confidence: high
status: active
---

# WhyBuy — Upbit 금융 의사결정 추적성 프로젝트

## 재판단

금융·Upbit는 부적합하지 않다. 오히려 사용자의 금융권 Java 백엔드·주문 시스템 관심과 더 직접 연결된다. 다만 자연어 전략 생성, 백테스트, 자동매매 자체는 이미 흔하고 Upbit도 2026년 Strategy Toolkit을 제공하므로 차별점이 되기 어렵다.

새 핵심 문제:

> AI 또는 적립식 전략이 왜 그 시점에 매수·보류를 결정했고, 어떤 사용자 의도·전략 버전·시장 데이터·위험 규칙·승인을 거쳐 어떤 주문 결과가 나왔는지 정확히 재구성할 수 있는가?

제품 정의:

> **WhyBuy는 Upbit 기반 적립식 매매의 모든 결정을 재현 가능한 `Decision Receipt`로 남기는 AI 매매 블랙박스다.**

## 차별성

일반 자동매매 시스템:

```text
가격 → 전략 → 주문
```

WhyBuy:

```text
사용자 의도
→ Strategy JSON version
→ point-in-time 시장 snapshot
→ 계산된 지표
→ AI/규칙의 제안
→ deterministic risk gate
→ 사람 승인
→ Upbit test/paper order
→ 주문 결과
→ hash-linked Decision Receipt
→ 동일 상태 replay / counterfactual 비교
```

독창성은 개별 기술이 아니라 다음 결합에 있다.

1. **Intent-to-order traceability:** 사용자 의도부터 주문 결과까지 연결한다.
2. **Agent observability:** OpenTelemetry GenAI conventions로 모델·prompt·tool call·latency를 기록한다.
3. **Decision Receipt:** 결정에 사용된 사실과 버전을 구조화된 영수증으로 만든다.
4. **Tamper evidence:** receipt를 이전 hash와 연결해 사후 수정 여부를 검출한다. 블록체인은 사용하지 않는다.
5. **Deterministic replay:** 동일 snapshot과 전략 버전으로 같은 규칙 결과를 재현한다.
6. **Counterfactual replay:** 특정 위험 규칙이나 전략 버전을 바꿨다면 결과가 어떻게 달라졌는지 비교한다.

## 사용자 시나리오

사용자가 다음 정책을 등록한다.

> 매주 5만 원을 매수하되 20일 이동평균선 아래면 5만 원을 추가하고, 하루 변동성이 8%를 넘거나 월 예산을 초과하면 매수를 보류한다.

시스템은 `2026-10-12 09:00`의 결정에 대해 다음 receipt를 남긴다.

```json
{
  "decision": "HOLD",
  "strategyVersion": "dca-v3",
  "marketSnapshot": "sha256:...",
  "facts": {"price": 123, "ma20": 130, "volatility24h": 0.091},
  "triggeredRules": ["BELOW_MA20", "VOLATILITY_HALT"],
  "riskGate": "REJECTED",
  "humanApproval": null,
  "orderTestId": null,
  "previousReceiptHash": "sha256:..."
}
```

사용자는 `왜 추가 매수를 하지 않았지?`를 조회하고, 시스템은 생성형 설명이 아니라 저장된 사실과 규칙을 근거로 답한다. 이어 `변동성 중단 규칙이 10%였다면?`을 replay하여 비교한다.

## 12주 MVP

필수:

- 자연어가 아닌 versioned Strategy JSON과 정책 편집 UI
- Upbit 공개 캔들·ticker 수집과 point-in-time snapshot
- 적립식 매수·추가 매수·예산·변동성 중단 규칙 엔진
- paper order 또는 Upbit 주문 생성 테스트
- append-only Decision Receipt와 hash chain 검증
- 결정 타임라인과 `왜 매수/보류했는가` 화면
- 동일 입력 replay와 한 가지 counterfactual 비교
- 핵심 주문·규칙 상태의 단위·통합·회귀 테스트

선택:

- LLM이 사용자 의도를 Strategy JSON 후보로 변환
- OpenTelemetry GenAI span과 tool-call trace
- 사람 승인 후에만 test order 실행
- receipt 기반 자연어 감사 보고서

제외:

- 실제 자금 자동매매
- 수익률 예측 모델
- 멀티 에이전트 토론
- GraphRAG와 vector DB
- 블록체인
- 수익 보장 또는 투자 추천

## 수업 적합성

| 강의 요소 | WhyBuy 산출물 |
|---|---|
| 실질적 사용자 가치 | 개인 알고리즘 투자자·개발자의 결정 재현과 오류 조사 |
| 요구사항 | 안전 한도, 승인, 재현성, 무결성, 주문 중복 방지 |
| UML | 결정 생성·승인·주문 테스트·replay sequence |
| SOLID | Strategy, RiskPolicy, ExecutionAdapter, ReceiptStore 분리 |
| 디자인 패턴 | Strategy, State, Adapter, Chain of Responsibility |
| 테스트 | 동일 snapshot 재현, 미래 데이터 누수, 중복 주문, hash 변조 탐지 |
| CI | 규칙 회귀 테스트와 고정 snapshot replay |
| AI 보고 | 모델·prompt·tool call과 사람 승인 trace |

## 완수 가능성

팀 프로젝트로는 충분히 가능하고, 개인 프로젝트도 필수 범위만 지키면 가능하다. 8주차 데모는 `정책 등록 → 과거 시점 snapshot → BUY/HOLD 결정 → receipt 생성 → 이유 조회 → rule 변경 counterfactual`로 고정한다. 실제 주문, LLM agent, OpenTelemetry는 핵심 규칙 엔진과 receipt가 완성된 뒤 추가한다.

## 평가

- 동일 snapshot·strategy version의 결정 재현율 100%
- 잘못된 전략 version 또는 미래 데이터 사용 차단
- 동일 decision key의 중복 order 0건
- receipt 한 필드 변조 시 hash 검증 탐지율 100%
- 결정부터 receipt 저장까지 p95 latency
- 저장된 사실과 화면 설명의 일치 여부
- 사용자 3~5명이 과거 결정 원인을 찾는 데 걸린 시간

> [!note] Bias Check
> Decision Receipt와 hash chain은 감사 가능성을 높이지만 금융 규제 준수나 보안을 자동 보장하지 않는다. LLM 설명은 독립적 증거가 아니므로 저장된 시장 snapshot과 deterministic rule 결과를 근거로 삼는다. Upbit Strategy Toolkit이 이미 전략 생성·백테스트를 제공하므로 이를 복제하지 않고 결정 provenance와 replay에 범위를 집중한다.

## Sources

- Upbit Strategy Toolkit: https://docs.upbit.com/kr/docs/upbit-strategy-toolkit-reference
- Upbit order test: https://docs.upbit.com/kr/reference/order-test
- Upbit MyOrder WebSocket: https://docs.upbit.com/kr/reference/websocket-myorder
- OpenTelemetry GenAI attributes: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
- Audit Trails for Accountability in LLMs: https://arxiv.org/abs/2601.20727
- TS-Agent, ICAIF 2025: https://doi.org/10.1145/3768292.3771251

이 답변은 강의/수업/교육과 백엔드/성능/금융 시스템에 활용 가능합니다 — 흔한 자동매매를 사용자 의도부터 주문 결과까지 재현 가능한 금융 결정 provenance 문제로 전환합니다.

## Selected Emerging Fintech Technology

최종 headline 신기술은 [[2026-09-01-Q-whybuy-agentic-finance-technology-selection]]의 **AP2-inspired Verifiable Investment Mandate**로 정했다. Decision Receipt와 replay는 핵심 제품 기능으로 유지하고, OpenTelemetry GenAI observability는 stretch goal로 둔다.

## Reassessment — 2026-09-02

사용자가 투자 의도·위임 중심의 WhyBuy가 여전히 추상적이고 프로젝트로 확신하기 어렵다고 판단해 이 안을 보류했다. 새 추천은 [[2026-09-02-Q-upbit-order-traceability-project-redesign]]의 `OrderScope AI`다. 사용자 투자 판단 설명이 아니라 개발자의 주문 장애 추적·재현이라는 더 구체적인 금융 백엔드 문제로 전환했다.
