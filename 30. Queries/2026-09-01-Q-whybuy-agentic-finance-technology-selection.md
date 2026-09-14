---
type: query-result
aliases:
  - WhyBuy 최신 핀테크 기술 선정
  - Verifiable Investment Mandate
description: "Selection of an AP2-inspired signed investment mandate as the primary emerging fintech technology for the WhyBuy Upbit decision-traceability project."
author:
  - Codex
date created: 2026-09-01
date modified: 2026-09-01
tags:
  - query
  - agentic-finance
  - agentic-payments
  - ap2
  - upbit
  - cryptographic-mandate
source:
  - "[[2026-09-01-Q-upbit-financial-decision-traceability-project]]"
  - https://github.com/google-agentic-commerce/AP2
  - https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md
  - https://github.com/x402-foundation/x402
  - https://developer.visa.com/capabilities/trusted-agent-protocol/overview
  - https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai
reusableFor:
  - 강의/수업/교육
  - 취업/포트폴리오
  - 백엔드/성능/금융 시스템
  - 프로젝트 증거
confidence: high
status: active
---

# WhyBuy 최신 핀테크 기술 선정

## 최종 선택

WhyBuy의 headline 신기술은 **Agentic Finance의 Verifiable Investment Mandate**로 정한다.

> 사용자가 AI agent에게 허용한 자산·금액·기간·위험 한도를 구조화된 위임장으로 만들고 서명한 뒤, 모든 매매 제안이 그 위임장 범위 안에 있음을 검증하고 증거를 남긴다.

이는 Google Agent Payments Protocol(AP2)의 cryptographically signed Mandate를 Upbit 투자 의사결정에 맞게 변형한 아이디어다. AP2 호환이나 실제 결제 프로토콜 구현을 주장하지 않고 **AP2-inspired**라고 명시한다.

프로젝트 표현:

> **WhyBuy — Verifiable Investment Mandate와 Decision Receipt로 AI 매매 권한과 결과를 추적하는 Agentic Finance 플랫폼**

## 트렌드 근거

- Google AP2는 agent가 수행하는 결제에서 사용자의 의도와 checkout/payment를 Mandate로 연결하고 암호학적 증거를 제공한다.
- Visa Trusted Agent Protocol은 agent의 정체성과 요청 무결성을 HTTP Message Signatures/JWS 계열 서명으로 검증하는 방향이다.
- Mastercard Agent Pay는 agentic token과 사용자 승인·제어를 강조한다.
- x402는 AI agent와 API 간 HTTP-native 결제 흐름을 제시하지만 stablecoin·on-chain 결제가 중심이라 WhyBuy MVP에는 직접 적용하지 않는다.

2026-09-01 GitHub API 관측 기준 AP2는 3,164 stars, x402는 6,562 stars다. star는 변동하며 기술 효과가 아니라 개발자 관심도 신호다.

## Investment Mandate 예시

```json
{
  "mandateId": "mandate-2026-001",
  "owner": "user-123",
  "allowedMarkets": ["KRW-BTC", "KRW-ETH"],
  "maxPerOrderKrw": 100000,
  "maxMonthlyKrw": 500000,
  "allowedStrategies": ["DCA", "DCA_BELOW_MA20"],
  "volatilityHalt": 0.08,
  "validFrom": "2026-10-01T00:00:00+09:00",
  "validUntil": "2026-12-31T23:59:59+09:00",
  "strategyVersion": "dca-v3",
  "publicKeyId": "user-123-key-1",
  "signature": "base64url(...)"
}
```

## 주문 흐름

```text
사용자가 Investment Mandate 작성·서명
→ Agent가 Upbit 시장 snapshot 조회
→ Strategy가 BUY/HOLD 제안
→ Risk Gate가 Mandate 범위 검증
→ Decision Receipt가 mandate hash와 근거 기록
→ 사람 승인
→ Upbit order test / paper order
→ 결과 receipt 연결
```

검증 실패 예시:

- 허용하지 않은 `KRW-XRP` 주문
- 1회 한도 10만 원을 넘는 15만 원 주문
- 월 누적 한도 초과
- 유효기간이 끝난 mandate
- mandate 작성 후 전략 버전 변경
- 서명 후 금액 필드 변조

## WhyBuy의 차별점

일반 자동매매는 API Key가 가진 넓은 권한 안에서 전략이 주문한다. WhyBuy는 각 결정마다 다음 질문에 답한다.

1. 사용자가 정확히 무엇을 허용했는가?
2. 어떤 서명된 mandate가 근거인가?
3. 당시 데이터와 전략 버전은 무엇인가?
4. 제안이 mandate의 금액·자산·기간·위험 범위를 지켰는가?
5. 누가 승인했고 어떤 test order 결과가 나왔는가?

`권한이 있다`와 `이번 행동이 사용자 의도에 부합한다`를 분리한 것이 핵심이다.

## 12주 구현 경계

필수:

- canonical JSON mandate
- 공개키/개인키 기반 서명과 검증 또는 WebAuthn/passkey 기반 서명 spike
- 자산·금액·월 한도·기간·전략 버전 policy engine
- Upbit point-in-time snapshot
- mandate hash가 포함된 Decision Receipt
- paper/order-test adapter
- mandate 위반·변조 테스트
- 결정 replay

Stretch:

- OpenTelemetry GenAI tool-call trace
- counterfactual replay
- passkey UX
- receipt hash chain

제외:

- AP2 전체 역할·결제 network 구현
- x402 stablecoin payment
- 실제 Upbit 자동 주문
- blockchain
- 자체 암호 알고리즘
- 가격 예측 모델

## 기술 선택 주의

직접 서명 알고리즘을 만들지 않는다. 표준 crypto library를 사용하고 canonicalization·key management·replay attack을 테스트한다. 교육용 prototype이며 금융 보안 인증을 주장하지 않는다. 가장 안전한 8주차 기준은 서버가 생성한 Ed25519 keypair 기반 prototype이고, passkey/WebAuthn은 기술 spike 결과에 따라 stretch로 둔다.

## 데모

1. 사용자가 `KRW-BTC, 1회 10만 원, 월 50만 원` mandate에 서명한다.
2. agent가 8만 원 BTC test order를 제안해 통과한다.
3. 15만 원 주문은 mandate violation으로 차단된다.
4. JSON의 `100000`을 `200000`으로 수정하면 signature 검증이 실패한다.
5. 허용된 주문의 Decision Receipt에서 mandate·시장 snapshot·rule·승인·order-test 결과를 재구성한다.

## 평가

- 정상 mandate 서명 검증 성공률 100%
- 한 필드 변조 탐지율 100%
- 자산·금액·기간·월 한도 위반 차단율 100%
- 동일 mandate/request replay 중복 주문 0건
- 저장된 snapshot으로 결정 재현율 100%
- mandate 검증과 receipt 생성 p95 latency

> [!note] Bias Check
> Agentic payments는 빠르게 성장하는 흐름이지만 AP2·Visa·Mastercard 접근은 주로 commerce/payment에 관한 것이다. 이를 투자 주문에 적용하는 것은 프로젝트의 설계적 추론이지 업계 표준이 아니다. 서명된 mandate도 prompt injection, 잘못된 시장 데이터, 손실 전략, 탈취된 key를 자동 해결하지 않으므로 deterministic risk gate와 사람 승인을 유지한다.

## Sources

- Google AP2 specification: https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md
- Google AP2 repository: https://github.com/google-agentic-commerce/AP2
- Visa Trusted Agent Protocol: https://developer.visa.com/capabilities/trusted-agent-protocol/overview
- Mastercard Agent Pay: https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai
- x402: https://github.com/x402-foundation/x402
- AP2 security analysis: https://arxiv.org/abs/2608.23858

이 답변은 강의/수업/교육과 백엔드/성능/금융 시스템에 활용 가능합니다 — 최신 agentic payment의 사용자 의도 증명 문제를 Upbit 투자 권한·결정 추적 문제로 변환합니다.
