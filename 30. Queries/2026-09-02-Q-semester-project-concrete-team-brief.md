---
type: query-result
aliases:
  - 소프트웨어공학 학기 프로젝트 구체화
  - WhyBuy TracePilot 팀 설명서
description: "A concrete, beginner-friendly team brief comparing WhyBuy and TracePilot through users, scenarios, architecture, research questions, and a feasible 12-week scope."
author:
  - Codex
date created: 2026-09-02
date modified: 2026-09-02
tags:
  - query
  - semester-project
  - team-proposal
  - upbit
  - traceability
source:
  - "[[2026-09-01-Q-team-meeting-two-project-proposals]]"
  - "[[2026-09-01-Q-upbit-financial-decision-traceability-project]]"
  - "[[2026-09-01-Q-whybuy-agentic-finance-technology-selection]]"
  - "[[2026-09-01-Q-emerging-traceability-technology-selection]]"
  - "[[Graduation-elasticsearch]]"
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 프로젝트 증거
  - 백엔드/성능/금융 시스템
confidence: high
status: active
---

# 소프트웨어공학 학기 프로젝트 구체화

## 먼저 이해해야 할 한 문장

두 후보 모두 넓은 의미에서는 **추적성(traceability)** 프로젝트다.

- `TracePilot`: 무인기 요구사항이 어떤 시험과 비행 증거로 검증됐는지 추적한다.
- `WhyBuy`: 사용자가 AI에게 무엇을 허용했고, AI가 왜 매수·보류를 제안했으며, 어떤 승인과 주문 결과로 이어졌는지 추적한다.

즉 추적성은 단순히 그래프를 그리는 기술이 아니라, **결과가 나오기까지의 원인과 증거를 끊기지 않게 연결하는 것**이다.

## 추천안 — WhyBuy

### 제품 정의

> WhyBuy는 사용자가 AI 투자 도우미에게 허용한 범위를 전자 위임장으로 고정하고, 모든 매수·보류 결정을 나중에 검증하고 재현할 수 있게 만드는 Upbit 기반 의사결정 추적 시스템이다.

이 프로젝트는 수익을 잘 내는 자동매매 봇이 아니다. 핵심 질문은 다음과 같다.

> AI가 내 돈과 관련된 행동을 했을 때, 정말 내가 허용한 범위 안에서 행동했고 왜 그런 판단을 했는지 증명할 수 있는가?

### 실제 사용 장면

사용자 규칙:

> BTC만 매수할 수 있고, 1회 최대 10만 원, 한 달 최대 50만 원이다. 매주 5만 원을 적립식으로 매수하되 하루 변동성이 8%를 넘으면 보류한다.

시스템 동작:

1. 사용자가 위 조건으로 `Investment Mandate`를 만들고 전자서명한다.
2. 시스템이 특정 시점의 Upbit 가격과 변동성을 저장한다.
3. 적립식 전략이 `BTC 8만 원 BUY`를 제안한다.
4. 위험 검사기가 자산·금액·월 한도·유효기간을 검사한다.
5. 사용자가 최종 승인한다.
6. 실제 주문 대신 paper order 또는 Upbit order-test를 실행한다.
7. 시스템이 모든 근거를 `Decision Receipt` 한 장으로 남긴다.

실패 사례도 데모한다.

- AI가 15만 원 매수를 제안하면 1회 한도 위반으로 차단한다.
- BTC만 허용했는데 XRP를 제안하면 차단한다.
- 위임장 금액을 사후에 바꾸면 전자서명 검증이 실패한다.
- 같은 요청이 두 번 들어오면 중복 주문을 막는다.

### 사용자가 보는 화면

MVP 화면은 네 개면 충분하다.

1. `위임장 만들기`: 허용 코인, 1회·월 한도, 기간, 전략을 설정하고 서명
2. `오늘의 결정`: 시장 데이터와 BUY/HOLD 제안, 위반 규칙, 승인 버튼
3. `결정 영수증`: 당시 가격, 전략 버전, 발동 규칙, 승인자, 주문 결과 표시
4. `다시 실행`: 저장된 데이터로 같은 결정이 나오는지 replay하고 규칙 하나를 바꿔 비교

### 신기술이 들어가는 정확한 위치

headline 기술은 **AP2-inspired Verifiable Investment Mandate**다. Google AP2 전체를 구현하는 것이 아니라, AI agent가 사용자의 결제 의도를 서명된 Mandate로 증명한다는 발상을 투자 주문 권한에 적용한다.

- 일반 API Key: 이 계정으로 주문할 권한이 있는가?
- WhyBuy Mandate: **이번 BTC 8만 원 주문이 사용자가 이번 기간에 허용한 구체적 의도 안에 있는가?**

`Decision Receipt`는 그 결과를 저장하는 추적성 장치이고, `replay`는 저장된 증거가 실제로 결정을 재현하는지 시험하는 장치다. LLM은 자연어 정책을 JSON 초안으로 바꾸거나 영수증을 설명하는 보조 기능이며, 주문 허용 여부는 반드시 결정론적 규칙 코드가 판단한다.

### 소프트웨어 구조

```text
React UI
  → Mandate Service: 위임장 생성·서명 검증
  → Market Adapter: Upbit 공개 시세 snapshot 저장
  → Strategy Engine: BUY/HOLD 제안
  → Risk/Policy Engine: 자산·금액·기간·월 한도 검사
  → Approval Service: 사람 승인·거절
  → Order Adapter: paper/order-test 실행
  → Receipt Store: 전체 근거와 결과 저장
  → Replay Service: 과거 결정을 동일 입력으로 재실행
```

백엔드는 팀 역량에 따라 Spring Boot 또는 FastAPI 중 하나만 고른다. PostgreSQL이면 충분하며 blockchain, vector DB, GraphRAG는 넣지 않는다.

## 연구로 만드는 방법

논문 수준의 거대한 새 알고리즘을 발명할 필요는 없다. **설계한 장치가 기존 방식보다 실제로 나은가**를 실험하면 수업 프로젝트에 맞는 연구성이 생긴다.

### 연구 질문

- RQ1. 서명된 투자 위임장이 단순 설정 파일보다 무단·변조된 주문 제안을 더 확실하게 탐지하는가?
- RQ2. Decision Receipt가 일반 실행 로그보다 사용자가 과거 BUY/HOLD 원인을 찾는 시간을 줄이는가?
- RQ3. 저장된 시점 데이터와 전략 버전으로 결정을 100% 재현할 수 있는가?

### 비교 기준선

- Baseline A: 서명 없는 일반 JSON 설정 + 일반 애플리케이션 로그
- Proposed: 서명된 Mandate + 구조화된 Decision Receipt + replay

### 평가 지표

- 자산·금액·기간·월 한도 위반 차단율
- 위임장 한 필드 변조 탐지율
- 같은 요청의 중복 주문 발생 건수
- 고정 snapshot에서 결정 재현율
- 사용자 3~5명이 과거 결정 원인을 찾는 평균 시간과 정답률
- 결정부터 영수증 저장까지 p95 latency

수익률은 핵심 평가 지표로 사용하지 않는다. 수익률을 평가하면 시장 예측과 백테스트 편향이 프로젝트의 본래 문제를 덮는다.

## 12주 구현 계획

| 주차 | 반드시 끝낼 결과 |
|---|---|
| 1~2주 | 개인 투자자 3명 인터뷰, 요구사항과 실패 시나리오 확정 |
| 3~4주 | Upbit 시세 수집, Strategy/Risk Engine, DB walking skeleton |
| 5~6주 | Mandate 생성·서명 검증, BUY/HOLD Decision Receipt |
| 7~8주 | 승인 UI, paper/order-test, 위반 차단까지 중간 데모 |
| 9~10주 | deterministic replay, 일반 로그 baseline 구현 |
| 11주 | 변조·중복·미래 데이터 누수·장애 테스트와 사용자 실험 |
| 12주 | 결과 분석, 시험 보고서, 최종 발표와 데모 영상 |

8주차에 `위임장 → 시장 snapshot → BUY/HOLD → 위험 검사 → 승인 → test order → 영수증`이 작동하지 않으면 LLM과 counterfactual 기능은 삭제한다.

## 팀 역할 예시

4명 기준으로 역할을 기능 단위로 나눈다.

- 백엔드/도메인: Strategy, Risk Policy, 중복 주문 방지
- 데이터/연동: Upbit snapshot, paper/order-test adapter, replay dataset
- 프론트엔드/UX: 위임장, 승인, 영수증, replay 화면
- 품질/DevOps: 요구사항 추적, 테스트 자동화, CI, 성능·사용자 평가

한 사람이 문서만 맡는 방식은 피하고, 각자 핵심 코드와 테스트를 함께 소유한다.

## 대안 — TracePilot

### 제품 정의

> TracePilot은 무인기 요구사항이 어떤 비행 규칙·시험·텔레메트리 증거로 검증됐는지 연결하고, 요구사항 변경 시 다시 시험해야 할 항목을 추천하는 시스템이다.

예를 들어 `최대 고도 120m` 요구사항이 `100m`로 바뀌면 연결된 비행 규칙, 시험 케이스, 과거 비행 로그를 보여주고 재시험 후보를 제안한다. 연구실 구성원이 후보를 승인하면 변경 이력이 추적 그래프에 남는다.

신기술은 `Temporal Knowledge Graph + human-in-the-loop AI impact analysis`다. 정적인 trace matrix와 달리 연결이 언제 만들어지고 변경됐는지 보존한다.

연구 질문은 “AI 추천이 수동 검색보다 누락된 재시험 후보를 더 빨리 찾는가?”이며, baseline은 keyword/TF-IDF 검색이다. 다만 실제 무인기 요구사항·시험 데이터와 연구실 사용자에 접근할 수 없다면 가짜 데이터 제작에 시간이 많이 들어 WhyBuy보다 실패 위험이 크다.

## 팀원에게 말할 90초 설명

### WhyBuy

> 우리가 만들려는 건 수익을 예측하는 자동매매 봇이 아닙니다. AI가 금융 행동을 할 때 사용자가 정확히 무엇을 허용했는지, 왜 매수나 보류를 결정했는지 나중에 증명하기 어려운 문제가 있습니다. 사용자는 BTC만, 1회 10만 원, 월 50만 원 같은 투자 위임장을 만들고 서명합니다. 시스템은 Upbit 시세를 보고 매수를 제안하지만, 규칙 엔진이 위임 범위를 검사하고 사람이 승인해야 test order가 실행됩니다. 당시 가격, 전략 버전, 발동 규칙, 승인과 결과는 Decision Receipt로 남겨 같은 입력으로 다시 재현합니다. 최신 agentic payment의 signed mandate 개념을 투자에 적용한다는 점이 도전 요소이고, 3개월 동안 실제 돈 없이 안전하게 구현하고 테스트할 수 있습니다.

### TracePilot

> 무인기 개발에서는 요구사항, 시험표, 비행 로그가 흩어져 있어서 요구사항 하나가 바뀌었을 때 무엇을 다시 시험해야 하는지 찾기 어렵습니다. TracePilot은 요구사항과 비행 규칙, 시험, 텔레메트리 증거를 시간 정보가 있는 그래프로 연결합니다. 고도 제한이 바뀌면 AI가 영향받는 시험과 로그를 추천하고 연구자가 승인합니다. 핵심은 AI가 자동 결정하는 것이 아니라 변경 근거와 사람의 판단까지 남기는 것입니다. 실제 연구실 데이터와 사용자를 확보할 수 있다면 연구 연계성이 강하지만, 데이터 확보가 안 되면 구현 위험이 큽니다.

## 최종 판단과 선택 조건

현재 기본 추천은 `WhyBuy`다.

- 사용자가 이미 Upbit와 금융 시스템에 흥미가 있어 끝까지 구현할 동기가 높다.
- 공개 시세와 paper/order-test로 데이터와 데모를 준비하기 쉽다.
- 서명, 권한 검사, 중복 방지, audit, replay를 통해 백엔드 취업 포트폴리오가 된다.
- 수익 예측을 제외해도 사용자 문제와 연구 지표가 남는다.

단, SEALAB에서 실제 무인기 요구사항·시험 자료와 매주 피드백을 줄 사용자 2명 이상을 확보할 수 있다면 `TracePilot`을 다시 우선 검토한다. 팀 회의에서는 기술 선호보다 `실제 사용자 확보`, `8주차 데모`, `팀원이 맡고 싶은 핵심 코드` 세 가지를 확인한 뒤 결정한다.

> [!note] Bias Check
> WhyBuy의 signed investment mandate는 agentic payment 개념을 투자에 변형한 설계 가설이며 금융 업계 표준이나 규제 준수 시스템이 아니다. TracePilot의 사업 가치도 실제 연구실 인터뷰 전에는 가설이다. 두 프로젝트의 독창성은 세상에 없는 개별 기술이 아니라, 구체적 문제에 기술을 결합하고 baseline과 실패 조건으로 검증하는 데서 주장해야 한다.

이 답변은 강의/수업/교육, 취업/포트폴리오, 프로젝트 증거에 활용 가능합니다 — 팀이 기술 이름이 아니라 실제 사용자 흐름, 구현 범위, 비교 실험을 보고 한 학기 주제를 결정하도록 돕습니다.
