---
type: documentation
aliases:
  - Software Engineering Project Proposals
  - 소프트웨어개발론 프로젝트 제안 2안
description: "Two team-ready semester project proposals combining emerging AI technology with UAV traceability or Upbit-based agentic finance."
author:
  - "[[김규태]]"
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - semester-project
  - team-proposal
  - emerging-technology
status: draft
---

# 소프트웨어개발론 프로젝트 제안 2안

## 우리가 만들고 싶은 프로젝트

평범한 CRUD나 AI 챗봇이 아니라, 2025~2026년에 주목받는 AI Agent 기술을 실제 문제에 적용하고 효과와 한계를 직접 검증한다.

원칙은 두 가지다.

1. 최신 기술은 많이 넣지 않고 **핵심 기술 하나 + 확장 기술 하나**만 선택한다.
2. 기술 이름보다 **실제 사용자 문제와 8주차 작동 데모**를 우선한다.

---

## A안 — TracePilot AI

### 한 문장

> 무인기 요구사항, 비행 규칙, 시험과 비행 로그의 변경 이력을 연결하고 AI Agent가 누락된 연결과 재시험 범위를 제안하는 Agentic Digital Thread다.

### 해결할 문제

무인기 프로젝트 자료는 요구사항 문서, 코드, 시험 계획서, 테스트 결과, 비행 로그와 GitHub Issue에 흩어진다. 프로젝트가 커지면 다음 질문에 답하기 어렵다.

- 이 요구사항은 실제로 구현됐는가?
- 어떤 테스트와 비행 로그로 검증했는가?
- 요구사항이 변경되면 어떤 기능과 테스트를 다시 확인해야 하는가?
- AI가 제안한 추적 관계의 근거와 승인자는 누구인가?

### 핵심 사용자

- 무인기 연구실 연구자와 학생
- 드론 프로젝트 개발팀
- 요구사항·시험 담당자

### 최신 기술

#### 핵심 — Agentic Digital Thread + Temporal Knowledge Graph

- 요구사항부터 시험 증거까지의 관계를 graph로 표현한다.
- 현재 연결뿐 아니라 과거 버전과 변경 시점을 보존한다.
- AI Agent가 변경의 영향을 받아 재검토할 artifact를 근거와 함께 제안한다.
- 사람이 승인한 관계만 확정 graph에 반영한다.

#### 확장 — GraphRAG 또는 LangGraph

- GraphRAG형 검색으로 여러 단계의 관계를 따라 변경 영향을 찾는다.
- LangGraph human-in-the-loop workflow로 AI 제안의 승인·거절 상태를 관리한다.

### 예시

```text
REQ-12 v1: 최대 고도 100m
→ FlightRule-03
→ Test-04
→ FlightLog-21
→ PASS

REQ-12 v2: 최대 고도 80m
→ AI가 FlightRule-03과 Test-04의 재검토 제안
→ 시험 담당자 승인
→ 새로운 trace와 재시험 상태 생성
```

### 8주차 데모

1. 고도 제한 요구사항을 100m에서 80m로 변경한다.
2. 연결된 비행 규칙·테스트·과거 비행 로그를 보여준다.
3. AI가 다시 실행해야 할 테스트와 근거를 제안한다.
4. 사용자가 승인하면 시간축 graph가 갱신된다.
5. 승인 전·후 관계와 변경 이력을 비교한다.

### 12주 MVP

- Requirement·FlightRule·TestCase·TelemetryEvidence 등록
- trace link와 버전·변경 이력 저장
- graph·timeline 시각화
- LLM 기반 변경 영향 후보와 근거 제안
- 승인·거절 workflow와 audit log
- 고정 데이터셋 기반 precision·recall 또는 검토시간 비교
- 단위·통합·회귀 테스트와 CI

### 제외할 것

- 실제 드론 제어
- GNN 직접 학습
- 완전 자율 멀티 에이전트
- GraphRAG 전체 pipeline 재구현
- 규제 준수 제품이라는 주장

### 독창성 질문

> 정적인 trace matrix를 넘어, 요구사항과 시험의 관계가 시간에 따라 어떻게 바뀌었는지 보존하고 AI가 재시험 범위를 제안할 수 있는가?

### 가장 큰 조건

연구실에서 실제 사용자 인터뷰와 무인기 요구사항·시험 자료 또는 현실적인 예제 데이터를 확보할 수 있어야 한다.

---

## B안 — WhyBuy

### 한 문장

> 사용자가 AI에게 허용한 투자 범위를 전자서명된 위임장으로 만들고, Upbit 매매 제안이 그 범위를 지켰는지 검증하며 모든 결정을 재현 가능한 영수증으로 남기는 Agentic Finance 플랫폼이다.

### 해결할 문제

자동매매와 AI Agent는 주문 결과를 남기지만 다음 질문에는 충분히 답하지 못할 수 있다.

- 사용자는 AI에게 정확히 무엇을 허용했는가?
- 왜 이 시점에 매수하거나 보류했는가?
- 당시 어떤 시장 데이터와 전략 버전을 사용했는가?
- 주문이 사용자 금액·종목·위험 한도 안에 있었는가?
- 같은 상황을 나중에 똑같이 재현할 수 있는가?

### 핵심 사용자

- 규칙 기반 적립식 투자를 하는 개인 투자자
- Upbit API로 전략을 실험하는 개발자
- AI Agent의 금융 행동을 검토하는 사용자

### 최신 기술

#### 핵심 — AP2-inspired Verifiable Investment Mandate

Google Agent Payments Protocol(AP2)의 signed Mandate 아이디어를 투자에 맞게 변형한다.

사용자는 다음 내용을 포함한 `Investment Mandate`에 전자서명한다.

```json
{
  "allowedMarkets": ["KRW-BTC", "KRW-ETH"],
  "maxPerOrderKrw": 100000,
  "maxMonthlyKrw": 500000,
  "allowedStrategies": ["DCA", "DCA_BELOW_MA20"],
  "volatilityHalt": 0.08,
  "validUntil": "2026-12-31T23:59:59+09:00",
  "strategyVersion": "dca-v3",
  "signature": "..."
}
```

AI가 주문을 제안해도 deterministic Risk Gate가 서명된 위임장의 종목·금액·기간·위험 범위를 검사한다.

#### 핵심 제품 기능 — Decision Receipt + Replay

```text
사용자 서명 Mandate
→ Upbit point-in-time 시장 snapshot
→ 전략의 BUY/HOLD 제안
→ deterministic Risk Gate
→ 사람 승인
→ Upbit order test 또는 paper order
→ Decision Receipt
→ 동일 상태 replay / 정책 변경 비교
```

#### 확장 — OpenTelemetry GenAI Observability

AI가 사용한 모델, prompt, Upbit 조회, 도구 호출, latency와 오류를 표준 trace로 남긴다.

### 예시

사용자의 위임 범위:

```text
BTC·ETH만 허용
1회 최대 100,000원
월 최대 500,000원
24시간 변동성 8% 초과 시 매수 중단
```

실행 결과:

```text
KRW-BTC 80,000원 → 통과
KRW-BTC 150,000원 → 1회 한도 초과로 차단
KRW-XRP 80,000원 → 허용되지 않은 종목으로 차단
서명 후 한도 필드 변경 → 전자서명 검증 실패
```

### 8주차 데모

1. 사용자가 투자 허용 범위를 작성하고 서명한다.
2. AI 또는 전략이 BTC 8만 원 매수를 제안하고 검증을 통과한다.
3. BTC 15만 원 제안은 한도 초과로 차단된다.
4. 위임장의 금액을 몰래 수정하면 서명 검증이 실패한다.
5. Decision Receipt에서 당시 데이터·전략·규칙·승인 결과를 재구성한다.

### 12주 MVP

- versioned Investment Mandate와 표준 library 기반 서명·검증
- Upbit 공개 캔들·ticker와 point-in-time snapshot
- 적립식 매수·월 예산·변동성 중단 규칙 엔진
- mandate policy/risk 검증
- 사람 승인과 Upbit order-test 또는 paper adapter
- Decision Receipt와 replay
- 위임장 변조·한도 위반·만료·중복 주문·미래 데이터 누수 테스트
- CI와 결정 재현 회귀 테스트

### 제외할 것

- 실제 자금 자동매매
- 가격 예측 모델
- AP2 전체 결제 network 구현
- x402·stablecoin 결제
- 블록체인
- 자체 암호 알고리즘

### 독창성 질문

> AI Agent가 오류나 prompt injection으로 허용 범위를 벗어난 주문을 제안해도, 서명된 투자 위임장과 결정적 Risk Gate가 이를 차단하고 사용자 의도부터 주문 결과까지 재구성할 수 있는가?

### 가장 큰 조건

투자 수익을 보장하거나 실거래 제품으로 주장하지 않는다. 학기 MVP는 Upbit 공개데이터와 주문 테스트·paper execution을 이용한 보안·추적성 prototype이다.

---

## 비교

| 기준 | TracePilot AI | WhyBuy |
|---|---:|---:|
| 핵심 트렌드 | Agentic Digital Thread | Agentic Finance·signed Mandate |
| 12주 완수 가능성 | 3/5 | 4/5 |
| 수업 산출물 적합성 | 5/5 | 5/5 |
| 데이터 준비 난도 | 높음 | 중간 |
| 안전한 8주차 데모 | 4/5 | 5/5 |
| 연구·드론 포트폴리오 | 5/5 | 2/5 |
| 금융·백엔드 포트폴리오 | 3/5 | 5/5 |
| 실제 사용자 | 연구실 접근 시 강함 | 개인 투자자 인터뷰 가능 |
| 핵심 검증 | 변경 영향 추천 정확도 | 권한 위반·변조 차단과 결정 재현 |

## 팀 결정 방법

각자 두 안에 대해 `맡고 싶은 기능`, `가장 큰 실패 위험`, `인터뷰 가능한 사용자 1명`을 적고 다음 배점으로 익명 투표한다.

| 기준 | 배점 |
|---|---:|
| 인터뷰 가능한 사용자와 데이터 | 30 |
| 8주차 데모 가능성 | 25 |
| 팀원 흥미와 역할 적합성 | 20 |
| 취업·포트폴리오 가치 | 15 |
| 신기술을 직접 검증할 수 있는가 | 10 |

선택 직후 핵심 기술 하나와 확장 기술 하나만 남기고, 나머지는 backlog로 이동한다.

## 90초 발표문

### TracePilot AI

> 무인기 프로젝트에서는 요구사항, 비행 규칙, 테스트와 비행 로그가 여러 장소에 흩어져 변경 영향을 찾기 어렵습니다. TracePilot AI는 이 자료의 현재 관계뿐 아니라 과거 버전까지 Temporal Knowledge Graph로 연결하는 Agentic Digital Thread입니다. 고도 제한이 100m에서 80m로 바뀌면 AI Agent가 다시 확인해야 할 규칙과 테스트를 근거와 함께 제안하고, 사람이 승인한 관계만 반영합니다. 8주차에는 요구사항 변경부터 영향 분석·승인·graph 갱신까지 시연하고, 실제 드론 제어와 GNN 학습은 제외하겠습니다.

### WhyBuy

> AI Agent가 돈을 다루는 Agentic Finance가 빠르게 등장하고 있지만, API Key가 있다고 해서 모든 주문이 사용자의 실제 의도에 맞는 것은 아닙니다. WhyBuy는 Google AP2의 signed Mandate 개념을 투자에 변형해 사용자가 허용한 종목·금액·기간·위험 한도를 전자서명된 위임장으로 만듭니다. AI가 주문을 제안하면 deterministic Risk Gate가 위임 범위를 검사하고, 모든 근거를 Decision Receipt로 저장해 나중에 재현합니다. 8주차에는 정상 주문, 한도 초과 차단, 위임장 변조 탐지와 결정 재구성을 Upbit 주문 테스트로 보여주겠습니다.

## 참고 자료

- [Google Agent Payments Protocol](https://github.com/google-agentic-commerce/AP2)
- [Google AP2 specification](https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md)
- [Visa Trusted Agent Protocol](https://developer.visa.com/capabilities/trusted-agent-protocol/overview)
- [Upbit Strategy Toolkit](https://docs.upbit.com/kr/docs/upbit-strategy-toolkit-reference)
- [Upbit 주문 생성 테스트](https://docs.upbit.com/kr/reference/order-test)
- [OpenTelemetry GenAI conventions](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
- [MAVLink Developer Guide](https://mavlink.io/en/)

> 최신 기술을 많이 넣는 것이 도전은 아니다. 최신 기술 하나를 직접 이해하고, 실패 조건과 baseline을 정해 효과와 한계를 검증하는 것이 이 프로젝트의 도전이다.
